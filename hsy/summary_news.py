
import os
import argparse
import sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenAI(
    model="tngtech/deepseek-r1t2-chimera:free",
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

def summarize_daily_report(target_date: str):
    """
    특정 날짜의 daily_report 파일을 읽어서 LLM을 이용해 요약합니다.
    
    Args:
        target_date (str): 'YYYY-MM-DD' 형식의 날짜 문자열
    """
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    report_dir = os.path.join(base_dir, "daily_reports")
    summary_dir = os.path.join(base_dir, "summary_news")
    if not os.path.exists(report_dir):
        if os.path.exists(os.path.join(base_dir, "..", "daily_reports")):
            report_dir = os.path.join(base_dir, "..", "daily_reports")
    
    file_path = os.path.join(report_dir, f"daily_report_{target_date}.md")
    
    if not os.path.exists(file_path):
        print(f"Error: 해당 날짜의 리포트 파일이 존재하지 않습니다. ({file_path})")
        return
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        print(f"파일을 성공적으로 읽었습니다: {file_path}")
        print(f"문서 길이: {len(content)} 자")
        
    except Exception as e:
        print(f"파일 읽기 중 오류 발생: {e}")
        return

    print("\n--- 요약 생성 중 ---\n")
    
    prompt = (
        f"당신은 숙련된 투자 분석가입니다. 아래는 {target_date}의 주식 및 경제 뉴스 리포트입니다.\n"
        "이 리포트의 내용을 바탕으로 다음 사항들을 포함하여 핵심을 요약해주세요:\n\n"
        "1. **오늘의 핵심 이슈**: 가장 중요한 시장 이벤트나 뉴스 3가지\n"
        "2. **시장 동향 요약**: 주요 섹터별 흐름 및 특이사항\n"
        "3. **투자 시사점**: 투자자가 주목해야 할 포인트\n\n"
        "리포트 내용:\n"
        f"{content}\n\n"
        "응답은 보기 좋은 마크다운 형식으로 작성해주세요."
    )
    
    try:
        response = llm.invoke([{"role": "user", "content": prompt}])
        summary_file_path = os.path.join(summary_dir, f"summary_news_{target_date}.md")
        with open(summary_file_path, "w", encoding="utf-8") as f:
            f.write(response.content)
        print(f"요약 파일이 저장되었습니다: {summary_file_path}")
    except Exception as e:
        print(f"LLM 요청 중 오류 발생: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Daily News Report Summarizer")
    parser.add_argument("--date", type=str, required=True, help="Target date in YYYY-MM-DD format")
    
    args = parser.parse_args()
    
    summarize_daily_report(args.date)
