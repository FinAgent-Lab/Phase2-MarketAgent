# prompts/registry.py
from pathlib import Path
from .keys import PromptKey

PROMPT_BASE_DIR = Path(__file__).parent  # .../prompts

# 레지스트리에는 "파일 이름"만 저장
PROMPT_REGISTRY = {
    (PromptKey.CATEGORIZE_NEWS, "REV00"): "categorize_news.md",
    (PromptKey.BUILD_MACRO_REPORT, "REV00"): "build_macro_report.md",
}

def load_prompt(key: PromptKey, revision: str = "REV00") -> str:
    file_name = PROMPT_REGISTRY.get((key, revision))
    if file_name is None:
        raise KeyError(f"Prompt not found: key={key}, revision={revision}")

    full_path = PROMPT_BASE_DIR / file_name
    if not full_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {full_path}")

    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()
