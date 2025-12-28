# FinAgent Chat Client

금융 시장 분석을 위한 AI 채팅 인터페이스입니다.

## 기능

- 🤖 GPT 기반 멀티턴 대화
- 🔄 Dify API 지원 (엔드포인트 전환 가능)
- 🌙 다크 테마 UI
- 📱 반응형 디자인
- 💬 대화 히스토리 관리

## 시작하기

### 1. 의존성 설치

```bash
npm install
```

### 2. 환경변수 설정

`.env.example`을 참고하여 `.env` 파일을 생성하세요:

```bash
cp .env.example .env
```

그리고 API 키를 설정하세요:

```env
# OpenAI 사용시
VITE_API_PROVIDER=openai
VITE_OPENAI_API_KEY=sk-your-api-key

# Dify 사용시
VITE_API_PROVIDER=dify
VITE_DIFY_API_KEY=app-your-dify-key
VITE_DIFY_BASE_URL=https://your-dify-instance.com/v1
```

### 3. 개발 서버 실행

```bash
npm run dev
```

http://localhost:5173 에서 앱을 확인할 수 있습니다.

## API 전환

`VITE_API_PROVIDER` 환경변수를 통해 API 제공자를 쉽게 전환할 수 있습니다:

- `openai`: OpenAI Chat Completions API 사용
- `dify`: Dify Workflow/Chatbot API 사용

## 프로젝트 구조

```
src/
├── components/
│   ├── ChatArea/      # 메인 채팅 영역 컴포넌트
│   │   ├── ChatArea.jsx
│   │   ├── ChatInput.jsx
│   │   └── MessageBubble.jsx
│   └── Sidebar/       # 사이드바 컴포넌트
│       └── Sidebar.jsx
├── hooks/
│   └── useChat.js     # 채팅 상태 관리 훅
├── services/
│   └── api.js         # API 추상화 레이어
├── App.jsx
└── main.jsx
```

## 빌드

```bash
npm run build
```

빌드된 파일은 `dist/` 폴더에 생성됩니다.

## 기술 스택

- React 19
- Vite 7
- CSS Variables (다크 테마)
- Pretendard 폰트
