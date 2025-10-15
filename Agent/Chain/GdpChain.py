"""
FRED GDP 데이터와 S&P 500 섹터 데이터를 분석하여 
향후 유망한 섹터를 예측하는 모델
"""

import os
import sys
import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv
from datetime import datetime
from dateutil.relativedelta import relativedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Agent.Prompt.GdpPrompt import ANALYSIS_PROMPT, BACKTEST_PROMPT, FEEDBACK_PROMPT
from Agent.Prompt.GdpPrompt import first_output_parser, backtest_output_parser, feedback_output_parser

from Agent.Util.util import yfinance_get_sectors_data
from Agent.Util.util import create_llm


load_dotenv()

DEFAULT_START_DATE = "2008-01"

# 환경 변수 로드
class GDPAnalyzer:
    """FRED API를 사용한 GDP 데이터 분석 클래스"""
    
    def __init__(self):
        self.fred = Fred(api_key=os.getenv('FRED_API_KEY'))
    
    def get_gdp_data(self):
        """GDP 원본 데이터 조회"""
        return self.fred.get_series('GDP')
    
    def get_annual_gdp_growth(self) -> pd.DataFrame:
        """연간 GDP 성장률 계산"""
        gdp_data = self.get_gdp_data()
        annual_gdp = gdp_data.resample('YE').mean()
        gdp_growth = annual_gdp.pct_change() * 100
        
        result = pd.DataFrame({
            'GDP': annual_gdp,
            '전년 대비 성장률(%)': gdp_growth
        })
        return result
    
    def get_gdp_data_by_period(self, start_date: str, end_date: str) -> pd.DataFrame:
        """특정 기간의 GDP 데이터 조회"""
        gdp_growth = self.get_annual_gdp_growth()
        return gdp_growth.loc[start_date:end_date]




class GdpSectorAnalyzer:
    """섹터 분석 및 추천 시스템
    
    데이터를 한 번만 로드하고 여러 분석을 효율적으로 수행합니다.
    """
    
    def __init__(self, start_date: str = DEFAULT_START_DATE, end_date: str = None):
        """
        Args:
            start_date: 분석 시작 날짜 (YYYY-MM 형식)
            end_date: 분석 종료 날짜 (YYYY-MM 형식, None이면 현재 날짜)
        """
        self.start_date = start_date
        self.end_date = end_date if end_date else datetime.now().strftime("%Y-%m")
        self.three_months_ago = (datetime.now() - relativedelta(months=3)).strftime("%Y-%m")
        
        # 데이터 캐시
        self._sector_data = None
        self._gdp_data = None
               
        # LLM
        self.llm = create_llm(model="openai/gpt-4o")
    
    def load_data(self):
        """데이터를 로드하고 캐싱 (한 번만 실행)"""
        if self._sector_data is None or self._gdp_data is None:
            print(f"📊 데이터 로딩 중... (start: {self.start_date}, end: {self.end_date})")
            
            # GDP 데이터 수집
            gdp_analyzer = GDPAnalyzer()
            self._gdp_data = gdp_analyzer.get_gdp_data_by_period(self.start_date, self.end_date)
            
            # 섹터 데이터 수집
            int_start_date = int(self.start_date.split('-')[0])
            self._sector_data = yfinance_get_sectors_data(start_year=int_start_date)
            
            print("✅ 데이터 로딩 완료!")
    
    @property
    def sector_data(self):
        """섹터 데이터 (lazy loading)"""
        if self._sector_data is None:
            self.load_data()
        return self._sector_data
    
    @property
    def gdp_data(self):
        """GDP 데이터 (lazy loading)"""
        if self._gdp_data is None:
            self.load_data()
        return self._gdp_data
    
    def get_filtered_data_before_three_months(self):
        """3개월 전까지의 데이터 반환"""
        sector_data = self.sector_data.loc[:self.three_months_ago]
        gdp_data = self.gdp_data.loc[:self.three_months_ago]
        return sector_data, gdp_data
    
    def first_analysis(self):
        """첫 번째 섹터 분석 (3개월 전 데이터 기반)"""
        print("🔍 첫 번째 섹터 분석 중...")
        
        # 3개월 전까지의 데이터로 분석
        sector_data, gdp_data = self.get_filtered_data_before_three_months()
        
        chain = ANALYSIS_PROMPT | self.llm | first_output_parser
        first_result = chain.invoke({
            "before_gdp_data": gdp_data,
            "before_sector_data": sector_data
        })
        
        print(f"✅ 추천 섹터: {first_result['Sectors']}")
        print(f"✅ 추천 섹터 분석: {first_result['Analysis']}")
        return first_result
    
    def backtest_analysis(self, first_result: dict):
        """백테스트 분석 (State 기반)
        
        Args:
            first_result: 첫 번째 분석 결과 (State에서 전달받음)
        """
        print("📈 백테스트 실행 중...")
        
        # 현재 데이터로 백테스트
        chain = BACKTEST_PROMPT | self.llm | backtest_output_parser
        backtest_result = chain.invoke({
            "recommend_sectors": first_result['Sectors'],
            "analysis_data": first_result['Analysis'],
            "now_gdp_data": self.gdp_data,
            "now_sector_data": self.sector_data
        })
        
        print(f"✅ 백테스트 결과: {backtest_result['Result']}")
        print(f"✅ 백테스트 결과 분석: {backtest_result['Feedback']}")
        return backtest_result
    
    def feedback_analysis(self, first_result: dict, backtest_result: dict):
        """피드백 기반 재분석 (State 기반)
        
        Args:
            first_result: 첫 번째 분석 결과 (State에서 전달받음)
            backtest_result: 백테스트 결과 (State에서 전달받음)
        """
        print("🔄 피드백 기반 재분석 중...")
        
        # 피드백 기반 재분석
        chain = FEEDBACK_PROMPT | self.llm | feedback_output_parser
        feedback_result = chain.invoke({
            "first_response": first_result,
            "now_gdp_data": self.gdp_data,
            "now_sector_data": self.sector_data,
            "backtest_response": backtest_result['Feedback']
        })
        
        print(f"✅ 수정된 추천 섹터: {feedback_result['Sectors']}")
        print(f"✅ 수정된 추천 섹터 분석: {feedback_result['Analysis']}")
        return feedback_result
    
    def run_full_analysis(self):
        """전체 분석 파이프라인 실행 (단독 실행용)
        
        Note: LangGraph 사용 시에는 각 메서드를 개별적으로 호출하세요.
        """
        print("🚀 전체 분석 시작...\n")
        
        # 1. 데이터 로드 (한 번만)
        self.load_data()
        
        # 2. 첫 번째 분석
        first_result = self.first_analysis()
        print()
        
        # 3. 백테스트 (first_result 전달)
        backtest_result = self.backtest_analysis(first_result)
        print()
        
        # 4. Failed인 경우 피드백 실행 (둘 다 전달)
        feedback_result = None
        if backtest_result['Result'] == 'Failed':
            feedback_result = self.feedback_analysis(first_result, backtest_result)
            print()
        
        return {
            'first_result': first_result,
            'backtest_result': backtest_result,
            'feedback_result': feedback_result
        }



def first_llm_chain():
    analyzer = GdpSectorAnalyzer()
    return analyzer.first_analysis()


def backtest_llm_chain():
    analyzer = GdpSectorAnalyzer()
    return analyzer.backtest_analysis()


def feedback_llm_chain():
    analyzer = GdpSectorAnalyzer()
    return analyzer.feedback_analysis()


if __name__ == "__main__":
    analyzer = GdpSectorAnalyzer()
    result = analyzer.run_full_analysis()
    
    print("\n" + "="*50)
    print("📊 최종 분석 결과")
    print("="*50)
    print(f"\n첫 번째 추천:\n{result['first_result']}")
    print(f"\n백테스트:\n{result['backtest_result']}")
    if result['feedback_result']:
        print(f"\n피드백 후 수정:\n{result['feedback_result']}")
