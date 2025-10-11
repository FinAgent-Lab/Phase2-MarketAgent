import os
import pandas as pd
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from Apis.YFinace import get_sp500_sectors_data

load_dotenv()
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_MODEL="openai/gpt-4o"


def create_llm(model: str = DEFAULT_MODEL):
    
    llm = ChatOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
    model_name=model,
    temperature=0,
    )
    return llm


def yfinance_get_sectors_data(start_year: int) -> pd.DataFrame:
    """S&P 500 지수 및 섹터별 종가 데이터 추출
    
    Args:
        start_year : int
        데이터 시작 연도
    Returns:
        S&P 500 지수 및 섹터별 종가 데이터프레임
        (컬럼: 'S&P 500', 'Technology', 'Healthcare', 'Financials', ...)
    """

    period = 'max'
    interval = '3mo'

    sectors_data = get_sp500_sectors_data(period=period, interval=interval)
    all_sectors_close = pd.DataFrame()
    
    for sector_name, data in sectors_data.items():
        if len(data) == 0:
            continue
            
        # 지정된 연도 이후 데이터만 필터링
        if data.index[0].year <= start_year:
            filtered_data = data.loc[f'{start_year}':]
        else:
            filtered_data = data
        
        # Close 컬럼 추출
        close_columns = [col for col in filtered_data.columns if 'Close' in str(col)]
        if close_columns:
            all_sectors_close[sector_name] = filtered_data[close_columns[0]]
    
    return all_sectors_close 


# if __name__ == "__main__":
#     data = yfinance_get_sectors_data(start_year=2008)
#     print(data)
