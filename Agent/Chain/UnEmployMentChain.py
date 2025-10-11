"""
FRED 실업률 데이터와 S&P 500 섹터 데이터를 분석하여 
향후 유망한 섹터를 예측하는 LangChain 기반 분석 체인
"""

import os
import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser

from Apis.FredApi import get_unemployment_rate
from Apis.YFinace import get_sp500_sectors_data

# 환경 변수 로드
load_dotenv()

# 상수
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_MODEL = "openai/gpt-4o"
RECENT_YEARS = 5  # 최근 5년간 데이터


class UnemploymentAnalyzer:
    """FRED API를 사용한 실업률 데이터 분석 클래스"""
    
    def __init__(self):
        pass
    
    def get_recent_unemployment(self, years: int = RECENT_YEARS) -> pd.Series:
        """최근 N년간의 월별 실업률 데이터 추출
        
        Args:
            years: 조회할 연도 수 (기본값: 5년)
            
        Returns:
            최근 N년간의 월별 실업률 시리즈
        """
        unemployment_data = get_unemployment_rate()
        
        # 최근 N년 날짜 계산
        end_date = datetime.now()
        start_date = end_date - relativedelta(years=years)
        
        # 기간 필터링
        recent_data = unemployment_data[start_date:]
        
        return recent_data


def get_sectors_monthly_close_data(years: int = RECENT_YEARS) -> pd.DataFrame:
    """S&P 500 섹터별 최근 N년간의 월별 종가 데이터 추출
    
    Args:
        years: 데이터 조회 연도 수 (기본값: 5년)
        
    Returns:
        섹터별 월별 종가 데이터프레임
    """
    # 최근 5년치 데이터 가져오기
    sectors_data = get_sp500_sectors_data(period='5y', interval='1mo')
    all_sectors_close = pd.DataFrame()
    
    for sector_name, data in sectors_data.items():
        if len(data) == 0:
            continue
        
        # Close 컬럼 추출
        close_columns = [col for col in data.columns if 'Close' in str(col)]
        if close_columns:
            all_sectors_close[sector_name] = data[close_columns[0]]
    
    return all_sectors_close


# 프롬프트 템플릿 설정
output_parser = CommaSeparatedListOutputParser()

UNEMPLOYMENT_ANALYSIS_PROMPT = PromptTemplate.from_template(
    """너는 최고의 미국 주식 시장 분석가입니다.
    
    아래 제공된 미국 실업률 데이터와 S&P 500 섹터별 가격 데이터를 종합적으로 분석하여,
    향후 가장 유망한 섹터 1개를 예측해주세요.

    ## 미국 실업률 데이터 (월별, 최근 5년)
    {unemployment_data}

    ## S&P 500 섹터별 월별 종가 데이터 (최근 5년)
    {sectors_data}

    분석 시 고려사항:
    1. 실업률 변화와 각 섹터의 역사적 상관관계
    2. 실업률 상승/하락 국면에서 각 섹터의 특성
    3. 고용 시장 강세/약세에 따른 섹터별 민감도
    4. 소비 심리와 실업률의 관계
    5. 과거 흐름을 참고해서 앞으로 1년간 유망한 섹터 예측

    실업률이 낮을수록 경기가 좋고, 높을수록 경기가 나쁜 것을 의미합니다.

    최종 출력에는 섹터명만 출력해주세요.
    예시: "Consumer Discretionary"

    {instructions}
    """
).partial(instructions=output_parser.get_format_instructions())


def create_llm_chain():
    """LangChain 체인 생성"""
    llm = ChatOpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        model_name=DEFAULT_MODEL,
        temperature=0,
    )
    return UNEMPLOYMENT_ANALYSIS_PROMPT | llm | output_parser


def unemployment_analyze_best_sectors() -> list:
    """실업률과 섹터 데이터를 분석하여 유망 섹터 예측
    
    최근 5년간의 월별 데이터를 분석하여 고용 시장 추세를 파악합니다.
    
    Returns:
        예측된 유망 섹터 리스트
    """
    # 데이터 수집
    unemployment_analyzer = UnemploymentAnalyzer()
    
    # 최근 5년 데이터 가져오기
    unemployment_data = unemployment_analyzer.get_recent_unemployment(years=5)
    sectors_data = get_sectors_monthly_close_data(years=5)
    
    # 분석 기간 정보 출력
    start_date = unemployment_data.index[0].strftime('%Y년 %m월')
    end_date = unemployment_data.index[-1].strftime('%Y년 %m월')
    print(f"📅 분석 기간: {start_date} ~ {end_date}\n")
    print(f"📊 최근 실업률: {unemployment_data.iloc[-1]:.1f}%")
    print(f"📊 5년 평균 실업률: {unemployment_data.mean():.1f}%\n")
    
    # LLM 체인 실행
    chain = create_llm_chain()
    result = chain.invoke({
        "unemployment_data": unemployment_data,
        "sectors_data": sectors_data
    })
    
    return result


if __name__ == "__main__":
    print("📊 실업률 기반 S&P 500 섹터 분석을 시작합니다...\n")
    
    predicted_sectors = unemployment_analyze_best_sectors()
    
    print("✅ 분석 완료!")
    print(f"🎯 유망 섹터: {predicted_sectors}")