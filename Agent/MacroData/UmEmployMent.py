import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


def get_unemployment_rate(fred) -> pd.DataFrame:
    
    RECENT_YEARS = 5

    unemployment_data = fred.get_series('UNRATE')

    end_date = datetime.now()
    start_date = end_date - relativedelta(years=RECENT_YEARS)
    
    result = unemployment_data[start_date:]
    
    return pd.DataFrame({
        f'최근{RECENT_YEARS}년간 미국실업률': result
    })



# if __name__ == "__main__":
#     unemployment_rate = get_unemployment_rate(fred)
#     print(unemployment_rate)
#     print(type(unemployment_rate))