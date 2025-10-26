import pandas as pd
from datetime import datetime


def funds_rate_target(fred) -> pd.DataFrame:
    """기준금리 목표 범위의 변화 시점만 추출"""
    target_upper = fred.get_series("DFEDTARU")  # 상한선
    target_lower = fred.get_series("DFEDTARL")  # 하한선

    # 변화가 있는 시점만 필터링
    changes_mask = (target_upper.diff() != 0) | (target_lower.diff() != 0)

    return pd.DataFrame(
        {"하한선": target_lower[changes_mask], "상한선": target_upper[changes_mask]}
    )


def get_funds_rate_data(fred) -> pd.DataFrame:
    """특정 기간의 기준금리 데이터 조회"""
    start_date = "2008-01"
    end_date = datetime.now().strftime("%Y-%m")
    funds_rate_data = funds_rate_target(fred)
    return funds_rate_data.loc[start_date:end_date]


if __name__ == "__main__":
    funds_rate_data = get_funds_rate_data()
    print(funds_rate_data)
    print(type(funds_rate_data))
