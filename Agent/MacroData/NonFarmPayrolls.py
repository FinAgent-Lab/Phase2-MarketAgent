import pandas as pd

import os
from dotenv import load_dotenv
from fredapi import Fred

load_dotenv()

fred = Fred(api_key=os.getenv("FRED_API_KEY"))


def get_nonfarm_payrolls(fred):

    nonfarm_payrolls = fred.get_series("PAYEMS")

    annual_average = nonfarm_payrolls.resample("YE").mean()
    annual_end = nonfarm_payrolls.resample("YE").last()

    result = pd.DataFrame(
        {
            "연평균 비농업 고용": annual_average.round(2),
            "연말 비농업 고용": annual_end.astype(int),
        }
    )
    return result


if __name__ == "__main__":
    nonfarm_payrolls = get_nonfarm_payrolls(fred)
    print(nonfarm_payrolls)
    print(type(nonfarm_payrolls))
