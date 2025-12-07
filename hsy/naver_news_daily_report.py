from __future__ import annotations

import os
import json
from os import getenv
from datetime import datetime
from typing import TypedDict, List, Dict, Any

from dotenv import load_dotenv
from dateutil import parser as dateparser

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END

from langchain_naver_community.tool import NaverNewsSearch

from keywords import keywords
from prompts.keys import PromptKey
from prompts.registry import load_prompt

load_dotenv()


# -------------------------------------------------------------------
# 1. 타입 정의
# -------------------------------------------------------------------
class NewsState(TypedDict):
    query: str                # 예: "미국 경제" / "연준" / "CPI"
    target_date: str          # "YYYY-MM-DD" 포맷 (예: "2025-03-20")
    raw_news: List[dict]      # NaverNewsSearch 원본 결과
    macro_news: List[dict]    # 날짜 + 거시경제 필터 후 기사
    categorized_news: Dict[str, Dict[str, Dict[str, List[dict]]]]  # 대/중/소
    report_markdown: str      # 최종 Markdown 리포트


# -------------------------------------------------------------------
# 2. 공통 유틸
# -------------------------------------------------------------------
def is_macro_related(text: str) -> bool:
    return any(kw in text for kw in keywords["MACRO_KEYWORDS"])


def is_us_centered(text: str) -> bool:
    return any(kw in text for kw in keywords["US_FOCUS_KEYWORDS"])


# -------------------------------------------------------------------
# 3. 그래프 노드 생성 함수
#    (llm, llm_categorizer를 클로저로 캡쳐해서 스코프 문제 해결)
# -------------------------------------------------------------------
def make_search_news_node() -> Any:
    naver_news_search = NaverNewsSearch(display=100, sort="date")

    def search_news_node(state: NewsState) -> Dict[str, Any]:
        results = naver_news_search.invoke(
            {
                "query": state["query"],
                "target_date": state["target_date"],
                "min_results": 100,
            }
        )

        # naver_news_search가 에러 문자열을 반환할 수도 있다고 가정
        if isinstance(results, str):
            print("[NaverNewsSearch ERROR]", results)
            raise RuntimeError(f"NaverNewsSearch failed: {results}")

        return {"raw_news": results}

    return search_news_node


def make_filter_by_date_and_macro_node() -> Any:
    def filter_by_date_and_macro_node(state: NewsState) -> Dict[str, Any]:
        target_date = state["target_date"]  # "YYYY-MM-DD"
        filtered: List[dict] = []

        for item in state.get("raw_news", []):
            pub = item.get("pubDate")
            if not pub:
                continue

            try:
                dt = dateparser.parse(pub)
                pub_date_str = dt.strftime("%Y-%m-%d")
            except Exception:
                continue

            if pub_date_str != target_date:
                continue

            text = f"{item.get('title', '')} {item.get('description', '')}"

            # 1) 거시경제 관련 필터
            if not is_macro_related(text):
                continue

            # 2) 미국 중심 여부 플래그
            item["_us_focus"] = is_us_centered(text)
            filtered.append(item)

        # 미국 관련 기사가 있으면 우선 사용, 없으면 전체 사용
        us_articles = [it for it in filtered if it.get("_us_focus")]
        macro_news = us_articles if us_articles else filtered

        return {"macro_news": macro_news}

    return filter_by_date_and_macro_node


def make_categorize_news_node(llm_categorizer: ChatOpenAI, revision: str = "REV00") -> Any:
    def categorize_news_node(state: NewsState) -> Dict[str, Any]:
        news_list = state.get("macro_news", [])
        if not news_list:
            return {"categorized_news": {}}

        # LLM 입력용 간단한 목록 구성
        items_for_prompt = []
        for idx, item in enumerate(news_list):
            items_for_prompt.append(
                {
                    "id": idx,
                    "title": item.get("title", ""),
                    "description": item.get("description", ""),
                }
            )

        system_prompt = load_prompt(PromptKey.CATEGORIZE_NEWS, revision)
        human_prompt = "뉴스 기사 목록:\n" + json.dumps(
            items_for_prompt, ensure_ascii=False, indent=2
        )

        resp = llm_categorizer.invoke(
            [
                SystemMessage(content=system_prompt),
                HumanMessage(content=human_prompt),
            ]
        )

        try:
            categories = json.loads(resp.content)
        except Exception as e:
            print("[categorize_news_node] JSON 파싱 실패:", e, resp.content)
            return {"categorized_news": {}}

        categorized: Dict[str, Dict[str, Dict[str, List[dict]]]] = {}

        for cat in categories:
            idx = cat.get("id")
            if idx is None or not isinstance(idx, int) or idx >= len(news_list):
                continue

            major = cat.get("major") or "기타"
            middle = cat.get("middle") or "기타"
            minor = cat.get("minor") or "기타"

            categorized.setdefault(major, {}).setdefault(middle, {}).setdefault(
                minor, []
            ).append(news_list[idx])

        return {"categorized_news": categorized}

    return categorize_news_node


def make_build_markdown_report_node(llm: ChatOpenAI, revision: str = "REV00") -> Any:
    def build_markdown_report_node(state: NewsState) -> Dict[str, Any]:
        categorized = state.get("categorized_news", {}) or {}
        query = state.get("query", "")
        target_date = state.get("target_date", "")

        lines: List[str] = []
        lines.append("# 글로벌 거시경제 데일리 리포트 (미국 중심)")
        lines.append("")
        lines.append(f"- 검색 키워드: **{query}**")
        lines.append(f"- 기준 날짜: **{target_date}**")
        lines.append(f"- 생성 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        lines.append("---")
        lines.append("")

        if not categorized:
            lines.append("> 해당 날짜에 조건을 만족하는 뉴스가 없습니다.")
            return {"report_markdown": "\n".join(lines)}

        for major, middle_dict in categorized.items():
            lines.append(f"## {major}")
            lines.append("")

            for middle, minor_dict in middle_dict.items():
                lines.append(f"### 지역: {middle}")
                lines.append("")

                for minor, articles in minor_dict.items():
                    lines.append(f"#### 주제: {minor}")
                    lines.append("")

                    # 기사 bullet list 구성
                    article_lines = []
                    for a in articles:
                        t = a.get("title", "")
                        d = a.get("description", "")
                        link = a.get("link", "")
                        if link:
                            article_lines.append(
                                f"- **{t}**\n  - {d}\n  - [원문 보기]({link})"
                            )
                        else:
                            article_lines.append(f"- **{t}**\n  - {d}")

                    joined_articles = "\n".join(article_lines)

                    prompt_template = load_prompt(
                        PromptKey.BUILD_MACRO_REPORT, revision
                    )
                    prompt = prompt_template.format(
                        major=major,
                        middle=middle,
                        minor=minor,
                        joined_articles=joined_articles,
                    )

                    resp = llm.invoke(prompt)
                    lines.append(resp.content.strip())
                    lines.append("")

                lines.append("---")
                lines.append("")

        return {"report_markdown": "\n".join(lines)}

    return build_markdown_report_node


# -------------------------------------------------------------------
# 4. 그래프 빌드 함수
# -------------------------------------------------------------------
def build_graph(
    llm: ChatOpenAI,
    llm_categorizer: ChatOpenAI,
    categorize_revision: str = "REV00",
    build_revision: str = "REV00"
):
    workflow = StateGraph(NewsState)

    # 노드 생성 (클로저로 llm 주입)
    search_news = make_search_news_node()
    filter_by_date_and_macro = make_filter_by_date_and_macro_node()
    categorize_news = make_categorize_news_node(llm_categorizer, categorize_revision)
    build_markdown_report = make_build_markdown_report_node(llm, build_revision)

    workflow.add_node("search_news", search_news)
    workflow.add_node("filter_by_date_and_macro", filter_by_date_and_macro)
    workflow.add_node("categorize_news", categorize_news)
    workflow.add_node("build_markdown_report", build_markdown_report)

    workflow.set_entry_point("search_news")
    workflow.add_edge("search_news", "filter_by_date_and_macro")
    workflow.add_edge("filter_by_date_and_macro", "categorize_news")
    workflow.add_edge("categorize_news", "build_markdown_report")
    workflow.add_edge("build_markdown_report", END)

    return workflow.compile()


# -------------------------------------------------------------------
# 5. 통계 출력 함수 (기존 코드 거의 유지)
# -------------------------------------------------------------------
def print_detailed_news_stats(final_state: NewsState) -> None:
    raw_count = len(final_state.get("raw_news", []))
    macro_count = len(final_state.get("macro_news", []))
    categorized = final_state.get("categorized_news", {}) or {}

    categorized_article_count = 0
    for major_dict in categorized.values():
        for middle_dict in major_dict.values():
            for articles in middle_dict.values():
                categorized_article_count += len(articles)

    filter_ratio = (macro_count / raw_count * 100) if raw_count > 0 else 0.0
    classify_ratio = (
        (categorized_article_count / raw_count * 100) if raw_count > 0 else 0.0
    )

    print("\n==================== 뉴스 처리 통계 ====================")
    print("1) 전체 개수 및 비율")
    print("--------------------------------------------------------")
    print(f"{'Raw 뉴스 수':<30} : {raw_count:>5}건")
    print(f"{'거시 필터 후 뉴스 수(macro_news)':<30} : {macro_count:>5}건")
    print(f"{'분류에 사용된 기사 수(categorized)':<30} : {categorized_article_count:>5}건")
    print("--------------------------------------------------------")
    if raw_count > 0:
        print(f"{'필터링 비율 (macro / raw)':<30} : {filter_ratio:>6.2f}%")
        print(f"{'분류 비율 (categorized / raw)':<30} : {classify_ratio:>6.2f}%")
    else:
        print("원본 뉴스(raw_news)가 0건이어서 비율 계산 불가")
    print("========================================================\n")

    print("2) 거시 카테고리 구조")
    print("--------------------------------------------------------")
    if not categorized:
        print("categorized_news가 비어 있습니다.")
        print("========================================================\n")
        return

    for major, middle_dict in categorized.items():
        middle_count = len(middle_dict)
        print(f"[대분류] {major} (중분류 {middle_count}개)")
        for middle, minor_dict in middle_dict.items():
            minor_count = len(minor_dict)
            middle_article_count = sum(len(articles) for articles in minor_dict.values())
            print(
                f"  ├─ [중분류] {middle} (소분류 {minor_count}개, 기사 {middle_article_count}건)"
            )
            for minor, articles in minor_dict.items():
                minor_article_count = len(articles)
                print(f"  │     ├─ [소분류] {minor} (기사 {minor_article_count}건)")
        print("--------------------------------------------------------")
    print("========================================================\n")


# -------------------------------------------------------------------
# 6. 엔트리 포인트
# -------------------------------------------------------------------
def write_report(
    date: str = "2025-11-25",
    query: str = "미국 주식",
    model_name: str = "tngtech/deepseek-r1t2-chimera:free",
    openrouter_url: str = "https://openrouter.ai/api/v1",
    show_stats: bool = False,
    categorize_revision: str = "REV00",
    build_revision: str = "REV00",
) -> None:
    """
    한 날짜(date)에 대해 데일리 리포트를 생성하고 파일로 저장.
    """
    api_key = getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY 환경 변수가 설정되어 있지 않습니다.")

    llm = ChatOpenAI(
        model=model_name,
        api_key=api_key,
        base_url=openrouter_url,
    )

    llm_categorizer = ChatOpenAI(
        model=model_name,
        api_key=api_key,
        base_url=openrouter_url,
        temperature=0,
    )

    app = build_graph(
        llm=llm,
        llm_categorizer=llm_categorizer,
        categorize_revision=categorize_revision,
        build_revision=build_revision,
    )

    initial_state: NewsState = {
        "query": query,
        "target_date": date,
        "raw_news": [],
        "macro_news": [],
        "categorized_news": {},
        "report_markdown": "",
    }

    final_state: NewsState = app.invoke(initial_state)
    report_md = final_state["report_markdown"]

    os.makedirs("./daily_reports", exist_ok=True)
    file_name = f"./daily_reports/daily_report_{date}.md"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(report_md)

    # 통계도 보고 싶으면 아래 호출
    if show_stats:
        print_detailed_news_stats(final_state)


if __name__ == "__main__":
    write_report(
        date="2025-11-30", # 날짜는 변경
        query="미국 주식", # 쿼리는 고정
        model_name="tngtech/deepseek-r1t2-chimera:free",
        openrouter_url="https://openrouter.ai/api/v1",
        show_stats=True, # 통계는 필요하면 True
        categorize_revision="REV00",
        build_revision="REV00",
    )
