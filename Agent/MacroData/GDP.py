import pandas as pd


def get_gdp_data(fred):
    gdp_data = fred.get_series("GDP")

    annual_gdp = gdp_data.resample("YE").mean()
    gdp_growth = annual_gdp.pct_change() * 100

    result = pd.DataFrame(
        {"연평균GDP": annual_gdp.round(2), "전년 대비 성장률(%)": gdp_growth.round(2)}
    )
    return result


# if __name__ == "__main__":
#     gdp_data = get_gdp_data(fred)
#     print(gdp_data)
#     print(type(gdp_data))
