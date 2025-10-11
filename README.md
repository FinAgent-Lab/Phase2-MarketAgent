# 📊 FinAgent Phase2: Market Agent

> AI 기반 S&P 500 섹터 분석 및 투자 추천 시스템

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.27-green.svg)](https://www.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.6.8-orange.svg)](https://www.langchain.com/langgraph)

## 🎯 프로젝트 개요

**FinAgent Phase2: Market Agent**는 미국 연방준비제도(Fed)의 거시경제 지표를 분석하여 S&P 500 섹터별 투자 전략을 제시하는 AI 에이전트입니다. LangChain과 LangGraph를 활용한 체계적인 워크플로우를 통해 데이터 수집, 분석, 백테스트, 피드백의 전 과정을 자동화합니다.

### ✨ 주요 기능

- 🏦 **FRED API 연동**: 미국 기준금리, GDP, 실업률 등 거시경제 지표 실시간 수집
- 📈 **S&P 500 섹터 분석**: yfinance를 활용한 11개 주요 섹터 데이터 분석
- 🤖 **AI 기반 투자 추천**: LLM을을 활용한 지능형 섹터 추천
- 🔄 **자동 백테스트**: 과거 데이터 기반 추천 성과 검증
- 💡 **피드백 루프**: 백테스트 결과를 반영한 추천 전략 개선
- 🎯 **LangGraph 워크플로우**: 체계적인 분석 파이프라인 구축

## 🏗️ 아키텍처

```
┌─────────────────────────────────────────────────────────┐
│                    LangGraph Workflow                    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  [START] → [First Analysis] → [Backtest]                │
│                                      ↓                   │
│                                 Failed? → [Feedback]     │
│                                      ↓                   │
│                                  Success → [END]         │
│                                                          │
└─────────────────────────────────────────────────────────┘
         ↓                            ↓
    [FRED API]              [Yahoo Finance API]
    (거시경제 지표)          (섹터별 주가 데이터)
```

### 📂 프로젝트 구조

```
Phase2-MarketAgent/
├── Agent/                      # AI 에이전트 핵심 로직
│   ├── Chain/                  # LangChain 체인 구현
│   │   ├── FredChain.py       # 기준금리 기반 분석 체인
│   │   ├── GdpChain.py        # GDP 기반 분석 체인
│   │   └── UnEmployMentChain.py # 실업률 기반 분석 체인
│   ├── Graph/                  # LangGraph 워크플로우
│   │   └── FredGraph.py       # 분석-백테스트-피드백 그래프
│   ├── Prompt/                 # LLM 프롬프트 템플릿
│   │   └── FredPrompt.py      # 분석/백테스트/피드백 프롬프트
│   ├── Util/                   # 유틸리티 함수
│   │   └── util.py            # LLM 생성, 데이터 처리
│   └── main.py                # 메인 실행 파일
├── Apis/                       # 외부 API 연동
│   ├── FredApi.py             # FRED API 래퍼
│   └── YFinace.py             # Yahoo Finance API 래퍼
├── requirements.txt            # 프로젝트 의존성
├── .env.example               # 환경 변수 템플릿
└── README.md                  # 프로젝트 문서
```

## 🚀 시작하기

### 📋 사전 요구사항

- Python 3.12 이상
- [uv](https://docs.astral.sh/uv/) (Python 패키지 관리 도구)
- FRED API Key ([무료 발급](https://fred.stlouisfed.org/docs/api/api_key.html))
- OpenRouter API Key (GPT-4o 사용)

### ⚡ 빠른 시작 (uv 사용)

#### 1️⃣ uv 설치

**Windows (PowerShell)**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### 2️⃣ 프로젝트 클론 및 설정

```bash
# 저장소 클론
git clone https://github.com/Pseudo-Lab/FinAgent-Phase2-MarketAgent.git
cd Phase2-MarketAgent

# Python 3.12 환경 생성 및 의존성 설치
uv venv --python 3.12
uv pip install -r requirements.txt
```

#### 3️⃣ 환경 변수 설정

```bash
# .env 파일 생성
cp .env.example .env
```

`.env` 파일에 API 키를 입력하세요:

```env
# FRED API Key (https://fred.stlouisfed.org/docs/api/api_key.html)
FRED_API_KEY=your_fred_api_key_here

# OpenRouter API Key
OPENROUTER_API_KEY=your_openrouter_api_key_here
```


## 📊 분석 워크플로우

### 1단계: 초기 분석
- 3개월 전까지의 거시경제 지표 분석
- 기준금리, GDP, 실업률 등 종합 고려
- AI가 3개 유망 섹터 추천

### 2단계: 백테스트
- 현재 시점까지의 실제 데이터로 검증
- 추천 섹터의 실제 성과 평가
- Success/Failed 판정

### 3단계: 피드백 (Failed 시)
- 백테스트 실패 원인 분석
- 현재 시장 상황 재평가
- 개선된 추천 섹터 제시


## 🤝 기여하기

프로젝트에 기여를 환영합니다! 다음 절차를 따라주세요:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](./LICENSE) 파일을 참조하세요.

## 👥 팀

**Pseudo Lab - FinAgent Team**

프로젝트 팀장: 손봉균

---

<div align="center">
Made with ❤️ by Pseudo Lab FinAgent Team
</div>
