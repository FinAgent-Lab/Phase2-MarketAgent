# 가상환경
uv 설치
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

프로젝트 가상환경 설치
```bash
uv sync
```

# API KEY 설정
```bash
cp .env.example .env
```

.env 파일에 API KEY를 설정합니다.
- NAVER_CLIENT_SECRET
- NAVER_CLIENT_ID
- OPENROUTER_API_KEY


# 실행방법
```bash
uv run main.py --date YYYY-MM-DD # 특정 날짜로 실행

# or

uv run main.py # 어제 날짜로 실행(자동)
```

# 주요 기능
## 1. Naver 뉴스 자동 수집

NaverNewsSearch API를 사용하여 특정 키워드로 뉴스 데이터를 수집

날짜 기준 필터링 (YYYY-MM-DD)

최신순 정렬

## 2. 거시경제 필터링 로직

`keywords.py` 의 `MACRO_KEYWORDS`, `US_FOCUS_KEYWORDS`에 기반해 거시경제성 및 미국 관련성을 분석

## 3. LLM 기반 뉴스 분류

`PromptKey.CATEGORIZE_NEWS` 프롬프트 기반

대분류 → 중분류 → 소분류 구조로 분류

JSON 구조로 LLM에서 결과 반환

## 4. LLM 기반 리포트 생성

`PromptKey.BUILD_MACRO_REPORT` 프롬프트 기반

각 카테고리별 상세 리포트 자동 생성

Markdown 파일로 저장

## 5. Ubuntu 서버에서 자동 실행 가능

매일 1회 자동 실행(cron)

`date` 인자를 자동으로 어제 날짜로 설정 가능

# 폴더 구조

```bash
project-root/
├── main.py
├── naver_news_daily_report.py
├── keywords.py
├── prompts/
│   ├── keys.py
│   ├── registry.py
│   ├── categorize_news.md
│   └── build_macro_report.md
└── daily_reports/
    └── daily_report_YYYY-MM-DD.md (자동 생성)
```


# 프롬프트 수정 및 신규 추가

prompts 폴더에 있는 프롬프트를 수정할 수 있습니다.

- `categorize_news.md` : 뉴스 분류 프롬프트
- `build_macro_report.md` : 리포트 생성 프롬프트

프롬프트를 신규 추가할 경우 `prompts/registry.py`에 추가해야 합니다.

```python
# prompts/registry.py
PROMPT_REGISTRY = {
    (PromptKey.CATEGORIZE_NEWS, "REV00"): "categorize_news.md",
    (PromptKey.BUILD_MACRO_REPORT, "REV00"): "build_macro_report.md",
}
```