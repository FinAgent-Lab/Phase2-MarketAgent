# prompts/keys.py
from enum import Enum

class PromptKey(str, Enum):
    CATEGORIZE_NEWS = "categorize_news"
    BUILD_MACRO_REPORT = "build_macro_report"
