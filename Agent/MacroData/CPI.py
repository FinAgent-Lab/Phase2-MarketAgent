import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


def get_cpi_data(fred):

    RECENT_YEARS = 5

    cpi_data = fred.get_series("CPIAUCSL")

    end_date = datetime.now()

    start_date = end_date - relativedelta(years=RECENT_YEARS)

    result = cpi_data[start_date:]

    increase_rate = result.pct_change(periods=1) * 100

    return pd.DataFrame(
        {
            f"최근{RECENT_YEARS}년간 미국 소비자물가지수": result,
            "전월대비 증가율(%)": increase_rate.round(2),
        }
    )


# if __name__ == "__main__":
#     cpi_data = get_cpi_data(fred)
#     print(cpi_data)
#     print(type(cpi_data))
