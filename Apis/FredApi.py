"""
FRED API를 사용하여 데이터를 가지고 오는코드
"""

import os
import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv

load_dotenv()

fred = Fred(api_key=os.getenv("FRED_API_KEY"))


def get_federal_funds_rate():
    """미국 기준금리 목표 범위 데이터 함수"""
    target_upper = fred.get_series("DFEDTARU")  # 상한선
    target_lower = fred.get_series("DFEDTARL")  # 하한선
    return target_upper, target_lower


def get_effective_federal_funds_rate():
    """미국 일별 시장금리(EFFR) 데이터 함수"""
    effr = fred.get_series("EFFR")
    return effr


def get_gdp_data():
    """GDP 함수 (분기, SAAR)"""
    gdp_data = fred.get_series("GDP")
    return gdp_data


def get_unemployment_rate():
    """실업률 (월별, UNRATE)"""
    return fred.get_series("UNRATE")


def get_nonfarm_payrolls():
    """비농업 고용자수 (월별, PAYEMS)"""
    return fred.get_series("PAYEMS")


def get_cpi_headline():
    """소비자물가지수 헤드라인 (월별, CPIAUCSL)"""
    return fred.get_series("CPIAUCSL")


def get_cpi_core():
    """근원 CPI (월별, CPILFESL)"""
    return fred.get_series("CPILFESL")


def get_pce():
    """개인소비지출 금액 (월별, PCE)"""
    return fred.get_series("PCE")


def get_core_pce_price_index():
    """근원 PCE 물가지수 (월별, PCEPILFE; 2012=100)"""
    return fred.get_series("PCEPILFE")


def get_industrial_production():
    """산업생산지수 (월별, INDPRO)"""
    return fred.get_series("INDPRO")


def get_michigan_sentiment():
    """미시간대 소비자심리지수 (월별, UMCSENT)"""
    return fred.get_series("UMCSENT")


def get_chicago_fed_nfci():
    """시카고 연은 NFCI (주간, NFCI)"""
    return fred.get_series("NFCI")


def get_fhfa_hpi():
    """FHFA 주택가격지수 (월별, USSTHPI)"""
    return fred.get_series("USSTHPI")


def get_case_shiller_20():
    """S&P/Case-Shiller 20대 도시 주택가격지수 (월별, SPCS20RSA)"""
    return fred.get_series("SPCS20RSA")


def get_existing_home_sales():
    """기존주택판매 (월별, SAAR, EXHOSLUSM495S)"""
    return fred.get_series("EXHOSLUSM495S")


def get_initial_jobless_claims():
    """주간 신규 실업수당 청구 (주간, ICSA)"""
    return fred.get_series("ICSA")


def get_treasury_yield(maturity: str = "10Y"):
    """
    미 국체 수익률 (일별)
    지원: 3MO, 2Y, 5Y, 10Y, 30Y
    """
    code_map = {
        "3MO": "DGS3MO",
        "2Y": "DGS2",
        "5Y": "DGS5",
        "10Y": "DGS10",
        "30Y": "DGS30",
    }
    code = code_map.get(maturity.upper())
    if not code:
        raise ValueError("지원 만기: 3MO, 2Y, 5Y, 10Y, 30Y")
    return fred.get_series(code)


def get_vix():
    """VIX 지수 (일별, VIXCLS)"""
    return fred.get_series("VIXCLS")


def get_cleveland_median_cpi():
    """클리블랜드 연은 Median CPI (월별, MEDCPIM158SFRBCLE)"""
    return fred.get_series("MEDCPIM158SFRBCLE")


def get_dallas_trimmed_mean_pce_yoy():
    """달라스 연은 Trimmed Mean PCE (12개월 상승률, 월별, PCETRIM12M159SFRBDAL)"""
    return fred.get_series("PCETRIM12M159SFRBDAL")


def get_gscpi():
    """뉴욕 연은 글로벌 공급망 압력지수 (월별, GSCPI)"""
    return fred.get_series("GSCPI")
