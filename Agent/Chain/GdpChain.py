"""
FRED GDP 데이터와 S&P 500 섹터 데이터를 분석하여 
향후 유망한 섹터를 예측하는 LangChain 기반 분석 체인
"""

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser

from Apis.FredApi import get_gdp_data
from Apis.YFinace import get_sp500_sectors_data

load_dotenv()


class GDPAnalyzer:
    """FRED API를 사용한 기준금리 데이터 분석 클래스""" 
    def __init__(self):
        self.fred = Fred(api_key=os.getenv('FRED_API_KEY'))

    def get_gdp_data(self):
        return self.fred.get_series('GDP')

    def annual_gdp(self):
        gdp_data = self.get_gdp_data()
        annual_gdp = gdp_data.resample('YE').mean()
        gdp_growth = annual_gdp.pct_change() * 100
        
        result = pd.DataFrame({
            'GDP': annual_gdp,
            '전년 대비 성장률(%)': gdp_growth
        })
        return result




















if __name__ == "__main__":
