import yfinance as yf
import pandas as pd
import warnings

# FutureWarning 무시
warnings.filterwarnings("ignore", category=FutureWarning)

# S&P 500 섹터별 ETF 티커
SP500_SECTOR_ETFS = {
    "Technology": "XLK",  # Technology Select Sector SPDR Fund
    "Healthcare": "XLV",  # Health Care Select Sector SPDR Fund
    "Financials": "XLF",  # Financial Select Sector SPDR Fund
    "Consumer Discretionary": "XLY",  # Consumer Discretionary Select Sector SPDR Fund
    "Communication Services": "XLC",  # Communication Services Select Sector SPDR Fund
    "Industrials": "XLI",  # Industrial Select Sector SPDR Fund
    "Consumer Staples": "XLP",  # Consumer Staples Select Sector SPDR Fund
    "Energy": "XLE",  # Energy Select Sector SPDR Fund
    "Utilities": "XLU",  # Utilities Select Sector SPDR Fund
    "Real Estate": "XLRE",  # Real Estate Select Sector SPDR Fund
    "Materials": "XLB",  # Materials Select Sector SPDR Fund
}


def get_sp500_sectors_data(period="1y", interval="1d", include_market=True):
    """
    S&P 500 11개 섹터 및 S&P 500 지수의 데이터를 가져오는 함수

    Parameters:
    -----------
    period : str
        데이터 기간 (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
    interval : str
        데이터 간격 (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
    include_market : bool
        S&P 500 지수 데이터 포함 여부 (기본값: True)

    Returns:
    --------
    dict : 섹터명/지수명을 키로 하는 데이터프레임 딕셔너리
    """
    sector_data = {}

    # S&P 500 지수 데이터 먼저 로드
    if include_market:
        try:
            sp500_data = yf.download(
                "^GSPC", period=period, interval=interval, progress=False
            )
            sector_data["S&P 500"] = sp500_data
            print(f"✓ S&P 500 지수 (^GSPC) 데이터 로드 완료")
        except Exception as e:
            print(f"✗ S&P 500 지수 (^GSPC) 데이터 로드 실패: {e}")

    # 섹터별 ETF 데이터 로드
    for sector_name, ticker in SP500_SECTOR_ETFS.items():
        try:
            data = yf.download(ticker, period=period, interval=interval, progress=False)
            sector_data[sector_name] = data
            # print(f"✓ {sector_name} ({ticker}) 데이터 로드 완료")
        except Exception as e:
            print(f"✗ {sector_name} ({ticker}) 데이터 로드 실패: {e}")

    return sector_data


def get_sp500_sectors_latest_price():
    """
    S&P 500 11개 섹터의 최신 가격 정보를 가져오는 함수

    Returns:
    --------
    DataFrame : 섹터별 최신 가격 정보
    """
    tickers = list(SP500_SECTOR_ETFS.values())
    tickers_str = " ".join(tickers)

    data = yf.download(tickers_str, period="5d", progress=False)
    latest_prices = data["Close"].iloc[-1]

    result = pd.DataFrame(
        {
            "섹터": list(SP500_SECTOR_ETFS.keys()),
            "티커": list(SP500_SECTOR_ETFS.values()),
            "현재가": [latest_prices[ticker] for ticker in SP500_SECTOR_ETFS.values()],
        }
    )

    return result


def get_sp500_sector_performance(period="1mo"):
    """
    S&P 500 11개 섹터의 수익률을 계산하는 함수

    Parameters:
    -----------
    period : str
        수익률 계산 기간 (1d, 5d, 1mo, 3mo, 6mo, 1y, ytd, max)

    Returns:
    --------
    DataFrame : 섹터별 수익률 정보 (수익률 내림차순 정렬)
    """
    tickers = list(SP500_SECTOR_ETFS.values())
    tickers_str = " ".join(tickers)

    data = yf.download(tickers_str, period=period, progress=False)

    # 수익률 계산
    returns = (
        (data["Close"].iloc[-1] - data["Close"].iloc[0]) / data["Close"].iloc[0] * 100
    )

    result = (
        pd.DataFrame(
            {
                "섹터": list(SP500_SECTOR_ETFS.keys()),
                "티커": list(SP500_SECTOR_ETFS.values()),
                "수익률(%)": [returns[ticker] for ticker in SP500_SECTOR_ETFS.values()],
            }
        )
        .sort_values("수익률(%)", ascending=False)
        .reset_index(drop=True)
    )

    return result


def get_sp500_sector_info(ticker):
    """
    특정 섹터 ETF의 상세 정보를 가져오는 함수

    Parameters:
    -----------
    ticker : str
        섹터 ETF 티커 (예: 'XLK', 'XLV')

    Returns:
    --------
    dict : 섹터 ETF 상세 정보
    """
    etf = yf.Ticker(ticker)
    info = etf.info

    return {
        "이름": info.get("longName", "N/A"),
        "현재가": info.get("regularMarketPrice", "N/A"),
        "52주 최고": info.get("fiftyTwoWeekHigh", "N/A"),
        "52주 최저": info.get("fiftyTwoWeekLow", "N/A"),
        "거래량": info.get("volume", "N/A"),
        "평균 거래량": info.get("averageVolume", "N/A"),
        "시가총액": info.get("totalAssets", "N/A"),
    }


if __name__ == "__main__":
    sectors_data = get_sp500_sectors_data(period="max", interval="1mo")

    # 모든 섹터의 종가를 하나의 DataFrame으로 합치기
    all_sectors_close = pd.DataFrame()

    for sector_name, data in sectors_data.items():
        # 2008년 이후 데이터만 필터링
        if len(data) > 0 and data.index[0].year <= 2008:
            monthly_2008 = data.loc["2008":]
        else:
            monthly_2008 = data

        # Close 컬럼 추출 (컬럼명에 'Close'가 포함된 경우 처리)
        close_col = [col for col in monthly_2008.columns if "Close" in str(col)]
        if close_col:
            all_sectors_close[sector_name] = monthly_2008[close_col[0]]

    print("S&P 500 섹터별 월별 종가 (2008~현재)")
    print(all_sectors_close)
