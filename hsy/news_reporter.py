# 파일명: news_reporter.py
from os import getenv
from typing import TypedDict, List, Dict, Any
import uuid
import json
from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
import pytz
from dotenv import load_dotenv

# 기존 사용하던 라이브러리들
from langchain_naver_community.tool import NaverNewsSearch
from langchain_openai import ChatOpenAI

load_dotenv()

# ----------------------------
# 설정 (환경변수 확실히 셋팅)
# ----------------------------
OPENROUTER_API_KEY = getenv("OPENROUTER_API_KEY")
REPORT_OUTPUT_DIR = "./daily_reports"   # 저장 디렉토리 (미리 만들어두기)
TIMEZONE = "Asia/Seoul"
SCHEDULE_HOUR = 8   # 매일 오전 8시에 실행 (서버 시간과 상관없이 Asia/Seoul 타임)

llm = ChatOpenAI(
    model="tngtech/deepseek-r1t2-chimera:free",
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

# ----------------------------
# 상태/데이터 타입 정의
# ----------------------------
class Article(TypedDict):
    title: str
    link: str
    published_at: str  # ISO 날짜 문자열 가능
    content: str

class ReportState(TypedDict):
    query: str
    target_date: str
    articles: List[Article]
    categorized: Dict[str, Dict[str, List[Article]]]  # 중분류 -> 소분류 -> [articles]
    summaries: Dict[str, str]  # 중분류 -> summary

# ----------------------------
# 1) 유틸: 기사 목록 정리 함수
# ----------------------------
def normalize_search_results(raw_results: Any) -> List[Article]:
    """
    naver_search.run()의 결과가 리스트(dict)형태일 수도 있고,
    단순 문자열일 수도 있으니 둘 다 다루도록 안전하게 처리함.
    최종적으로 Article 타입 리스트 반환.
    """
    articles: List[Article] = []

    # 만약 이미 리스트 형태 (예: [{'title':..., 'link':..., 'content':...}, ...])
    if isinstance(raw_results, list):
        for item in raw_results:
            title = item.get("title") or item.get("headline") or ""
            link = item.get("link") or item.get("url") or ""
            content = item.get("content") or item.get("summary") or item.get("description") or ""
            published = item.get("published_at") or item.get("date") or ""
            articles.append({"title": title, "link": link, "published_at": published, "content": content})
        return articles

    # 만약 문자열 덩어리로 왔다면, LLM에게 기사 블록으로 분해해달라 요청
    if isinstance(raw_results, str):
        prompt = (
            "아래 텍스트는 검색결과의 덩어리입니다. "
            "각 기사를 JSON 리스트로 분해해줘. \n"
            "각 항목은 title, link(없으면 빈 문자열), published_at(날짜가 있으면 YYYY-MM-DD), content(본문 또는 요약) 필드를 가져야 합니다.\n\n"
            "텍스트:\n" + raw_results + "\n\n"
            "응답은 반드시 JSON 배열만 제공해줘."
        )
        resp = llm.invoke([{"role":"user","content":prompt}])
        try:
            parsed = json.loads(resp.content)
            for item in parsed:
                articles.append({
                    "title": item.get("title",""),
                    "link": item.get("link",""),
                    "published_at": item.get("published_at",""),
                    "content": item.get("content","")
                })
            return articles
        except Exception as e:
            # 실패하면 원문을 하나의 기사로 처리
            return [{"title":"raw_results_parsed_as_single","link":"","published_at":"","content":raw_results}]

    # 그 밖의 경우 안전 처리
    return []

# ----------------------------
# 2) 분류 노드: LLM에게 중/소분류 매핑 요청
# ----------------------------
# 우리가 만든 분류체계(설명용)
CATEGORY_SCHEMA = {
    "거시지표": ["GDP", "실업률", "CPI(물가)", "산업생산"],
    "금융시장": ["주식시장", "채권/금리", "환율", "원자재(유가)"],
    "정책·정책리스크": ["금리정책", "재정정책", "규제/세제"],
    "기업실적·기업이슈": ["실적발표", "M&A", "구조조정/파산"],
    "글로벌·외교경제": ["미국", "중국", "유럽", "국제무역"],
    "산업·섹터 이슈": ["반도체", "전기차", "에너지", "헬스케어"],
    "소비·물가·수요": ["소비지표", "물가압력", "리테일/소매판매"]
}

def classify_articles(articles: List[Article]) -> Dict[str, Dict[str, List[Article]]]:
    """
    각 기사를 중분류/소분류로 분류한다.
    리턴 형식: {중분류: {소분류: [Article,...], ...}, ...}
    """
    categorized: Dict[str, Dict[str, List[Article]]] = {mid: {} for mid in CATEGORY_SCHEMA.keys()}

    for art in articles:
        # 각 기사에 대해 LLM에게 중/소분류를 물어본다 (간단하고 일관된 응답 포맷 요구)
        prompt = (
            "당신은 투자자 관점의 뉴스 분류사입니다.\n"
            "아래 기사의 제목과 내용을 보고, 가장 알맞은 중분류와 소분류를 JSON으로 반환하세요.\n"
            "가능하면 하나의 중분류와 하나의 소분류만 선택하세요.\n"
            "중분류 후보와 소분류 후보는 다음과 같습니다:\n"
            f"{json.dumps(CATEGORY_SCHEMA, ensure_ascii=False, indent=2)}\n\n"
            f"기사 제목: {art['title']}\n\n"
            f"기사 내용: {art['content']}\n\n"
            "응답 예시:\n"
            '{"mid":"거시지표","sub":"CPI(물가)"}\n\n'
            "반드시 JSON 객체만 응답하세요."
        )
        resp = llm.invoke([{"role":"user","content":prompt}])
        try:
            parsed = json.loads(resp.content.strip())
            mid = parsed.get("mid")
            sub = parsed.get("sub")
        except Exception:
            # 실패 시 간단 규칙 기반(제목 포함 단어로 추정)
            mid = "산업·섹터 이슈"
            sub = "기타"

        if mid not in categorized:
            categorized[mid] = {}

        if sub not in categorized[mid]:
            categorized[mid][sub] = []

        categorized[mid][sub].append(art)

    return categorized

# ----------------------------
# 3) 요약 노드: 중분류별 요약
# ----------------------------
def summarize_category(mid: str, sub: str, articles: List[Article]) -> str:
    """
    특정 중분류·소분류 내 기사들을 요약.
    - 중분류 차원의 요약도 함께 생성 (중분류 전체 요약은 상위에서 합침)
    """
    # 짧은 요약 + 투자 포인트
    articles_text = "\n\n".join([f"제목: {a['title']}\n내용: {a['content']}\n링크: {a['link']}" for a in articles])

    prompt = (
        f"당신은 투자 분석가야. 아래는 [{mid} > {sub}]에 해당하는 기사들이다.\n"
        "1) 핵심 요약(각 기사에서 핵심 문장 1-2개)  \n"
        "2) 이 카테고리(중분류)에서 투자자가 유의할 '핵심 포인트' 3가지\n\n"
        "기사들:\n" + articles_text + "\n\n"
        "응답은 마크다운 형식으로 제공해줘. (제목: 요약, 핵심포인트: ... 형태)"
    )
    resp = llm.invoke([{"role":"user","content":prompt}])
    return resp.content

# ----------------------------
# 4) 리포트 파일 생성
# ----------------------------
import os
def save_report(state: ReportState):
    os.makedirs(REPORT_OUTPUT_DIR, exist_ok=True)
    target_date = state["target_date"]
    filename = f"{REPORT_OUTPUT_DIR}/news_report_{target_date}.md"
    lines = []
    lines.append(f"# 뉴스 요약 리포트 — {target_date}")
    lines.append(f"쿼리: {state['query']}\n")
    lines.append("## 중분류별 요약\n")

    for mid, subs in state["categorized"].items():
        # 중분류 전체 요약 (각 소분류 요약을 합쳐서 만든다)
        lines.append(f"### {mid}\n")
        for sub, arts in subs.items():
            lines.append(f"#### {sub} — 기사 수: {len(arts)}\n")
            # 소분류 내 기사 목록 간단 표
            for a in arts:
                lines.append(f"- [{a['title']}]({a['link']}) — {a['published_at']}")
            lines.append("\n")
            # 소분류 요약 (이미 만들어졌다면 사용)
            key = f"{mid}__{sub}"
            summary = state["summaries"].get(key, "")
            if summary:
                lines.append("요약:\n")
                lines.append(summary + "\n\n")

    # 전체 메타 정보 JSON으로도 저장
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # JSON 메타 저장
    meta_fn = f"{REPORT_OUTPUT_DIR}/news_report_{target_date}.json"
    with open(meta_fn, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

    print(f"Saved report: {filename} and {meta_fn}")

# ----------------------------
# 5) 메인 워크플로우 (한 번 실행하면 하루치 리포트 생성)
# ----------------------------
def run_daily_report(query: str, target_date_str: str):
    """
    query: 예: "미국 경제" 또는 "주식 시장"
    target_date_str: "YYYY-MM-DD" 형식
    """
    naver_search = NaverNewsSearch()

    print(f"[{datetime.now()}] Start fetching news for {target_date_str} / query={query}")

    try:
        raw = naver_search.run(query, target_date=target_date_str, min_results=15)
    except Exception as e:
        raw = f"Search error: {str(e)}"

    articles = normalize_search_results(raw)
    print(f"Fetched {len(articles)} articles (raw->normalized)")

    categorized = classify_articles(articles)
    print("Classification done.")

    summaries: Dict[str, str] = {}
    # 각 소분류별로 요약 생성 (병렬화 가능하지만 여기선 순차)
    for mid, subs in categorized.items():
        for sub, arts in subs.items():
            key = f"{mid}__{sub}"
            if len(arts) == 0:
                continue
            print(f"Summarizing {mid} > {sub} ({len(arts)} articles)")
            summ = summarize_category(mid, sub, arts)
            summaries[key] = summ

    state: ReportState = {
        "query": query,
        "target_date": target_date_str,
        "articles": articles,
        "categorized": categorized,
        "summaries": summaries
    }

    save_report(state)
    print("Daily report generation finished.")

# ----------------------------
# 6) 스케줄러 설정 (매일 지정된 시간에 실행)
# ----------------------------
def start_scheduler():
    tz = pytz.timezone(TIMEZONE)
    scheduler = BackgroundScheduler(timezone=tz)
    # 매일 SCHEDULE_HOUR시에 run_daily_report 호출 (예시는 "미국 경제" 쿼리, 날짜는 '어제'로 설정)
    def job_wrapper():
        # 목표 날짜는 '어제' (예: 오늘 2025-11-20이면 target_date=2025-11-19)
        target = (date.today() - timedelta(days=1)).isoformat()
        # 원하는 쿼리 리스트를 여러개 돌릴 수도 있음
        queries = ["미국 경제", "한국 거시경제", "글로벌 금융시장"]
        for q in queries:
            run_daily_report(q, target)

    scheduler.add_job(job_wrapper, 'cron', hour=SCHEDULE_HOUR, minute=0)
    scheduler.start()
    print(f"Scheduler started. Will run daily at {SCHEDULE_HOUR}:00 {TIMEZONE}")

# ----------------------------
# 스크립트 직접 실행 시
# ----------------------------
if __name__ == "__main__":
    from datetime import timedelta
    # 그냥 한 번 수동 실행해보고 싶으면 아래처럼 직접 호출 가능
    # 예: 수동으로 2025-11-19 리포트 만들기
    run_daily_report("미국 경제", "2025-11-19")

    # 또는 데몬처럼 실행시키고 스케줄러 시작
    # start_scheduler()

    # 메인 스레드가 죽지 않도록 루프 유지 (간단 데몬용)
    # try:
    #     import time
    #     while True:
    #         time.sleep(60)
    # except (KeyboardInterrupt, SystemExit):
    #     print("Shutting down.")
