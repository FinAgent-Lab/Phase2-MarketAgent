from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field



#----------------------------------------------#
# 첫 번째 분석 프롬프트
#----------------------------------------------#

class FirstOutputSchema(BaseModel):
    Sectors: str = Field(description="추천하는 3개의 섹터명 (예: 'Technology', 'Healthcare', 'Financials')")
    Analysis: str = Field(description="섹터 선정 이유 및 분석 내용")


first_output_parser = JsonOutputParser(pydantic_object=FirstOutputSchema)


ANALYSIS_PROMPT = PromptTemplate.from_template(
    """너는 최고의 미국 주식 시장 분석가입니다. 미국 주식 시장을 한국어로 분석해주세요.
    
    아래 제공된 미국 GDP 데이터와 S&P 500 섹터별 가격 데이터를 종합적으로 분석하여,
    향후 가장 유망한 섹터 3개를 예측해주세요.

    ## 미국 GDP 데이터 (연간 성장률)
    {before_gdp_data}

    ## S&P 500 섹터별 3개월 단위 종가 데이터
    {before_sector_data}

    분석 시 고려사항:
    1. GDP 성장률 변화와 각 섹터의 역사적 상관관계
    2. 현재 GDP 성장 추세가 각 섹터에 미치는 영향
    3. 과거 흐름을 참고해서 향후 3개월 내 유망한 섹터 예측

    {format_instructions}
    """
).partial(format_instructions=first_output_parser.get_format_instructions())





#----------------------------------------------#
# 백테스트 분석 프롬프트
#----------------------------------------------#


class BacktestOutputSchema(BaseModel):
    Result: str = Field(description="추천이 잘되었다면 Success 그렇지 않았다면 Failed")
    Feedback: str = Field(description="왜 그렇게 평가 했는지에 분석 내용")


backtest_output_parser = JsonOutputParser(pydantic_object=BacktestOutputSchema)


BACKTEST_PROMPT = PromptTemplate.from_template(
    """너는 최고의 미국 주식 시장 분석가입니다. 미국 주식 시장을 한국어로 분석해주세요.
    
    당신에게는 3개월전 데이터로 추천한 S&P500 섹터와 분석내용이 제공됩니다
    해당 내용을 참고하고 현재 데이터와 비교하였을때 3개월전 추천이 잘됐는지 평가해주세요.
    추천이 잘되었다면 Success 그렇지 않았다면 Failed 데이터를 제공해주세요


    ## 기존 추천했던 섹터
    {recommend_sectors}

    ## 추천했던 섹터 분석내용
    {analysis_data}

    ## 현재 GDP 데이터
    {now_gdp_data}

    ## 현재 섹터 데이터
    {now_sector_data}

    분석 시 고려사항:
    1. 3개월전에 추천한 섹터가 3개월 후에 어떤 결과를 냈는지 분석해줘
    2. 추천한 섹터 3개중에 S&P500 시장 수익률과 비교했을때 수익률이 높은 섹터와 낮은 섹터를 분석해줘
    3. 추천한 섹터 3개중에 2개이상이 시장 수익률 보다 좋으면 Success 그렇지 않았다면 Failed 출력해줘

    최종 출력예시
    예시: "Success"
    분석내용: "추천한 섹터가 모두 긍정적인 성과를 보였습니다."



    {format_instructions}
    """
).partial(format_instructions=backtest_output_parser.get_format_instructions())





#----------------------------------------------#
# 피드백 분석 프롬프트
#----------------------------------------------#

class FeedbackOutputSchema(BaseModel):
    Sectors: str = Field(description="추천하는 3개의 섹터명 (예: 'Technology', 'Healthcare', 'Financials')")
    Analysis: str = Field(description="섹터 선정 이유 및 분석 내용")


feedback_output_parser = JsonOutputParser(pydantic_object=FeedbackOutputSchema)


FEEDBACK_PROMPT = PromptTemplate.from_template(
    """
    너는 최고의 미국 주식 시장 분석가입니다. 미국 주식 시장을 한국어로 분석해주세요.
    추천한 섹터가 부정확하여 피드백을 받았습니다
    해당 피드백을 참고하고 추천한 섹터를 수정하여 추천해주세요



    ## 기존 추천 섹터 및 분석내용
    {first_response}

    ## 미국 GDP 데이터
    {now_gdp_data}

    ## S&P 500 섹터별 3개월 단위 종가 데이터
    {now_sector_data}

    ## 피드백 내용
    {backtest_response}

    분석 시 고려사항:
    1. GDP 성장률 변화와 각 섹터의 역사적 상관관계
    2. 현재 GDP 성장 추세가 각 섹터에 미치는 영향
    3. 과거 흐름을 참고해서 향후 3개월 내 유망한 섹터 예측

    {format_instructions}
    """
).partial(format_instructions=feedback_output_parser.get_format_instructions())

