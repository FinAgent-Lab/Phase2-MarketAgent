from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Dict, TypeVar, Generic



#----------------------------------------------#
# 베이스 스키마 정의
#----------------------------------------------#

T = TypeVar('T', bound=BaseModel)

class BaseOutputSchema(BaseModel, Generic[T]):
    Content: List[T] = Field(description="결과 내용")

#----------------------------------------------#
# 첫 번째 분석 프롬프트
#----------------------------------------------#

class RecommendSectorsOutputSchema(BaseModel):
    Sectors: List[str]  = Field(description="추천하는 3개의 섹터명 (예: 'Technology', 'Healthcare', 'Financials')")
    Analysis: str = Field(description="섹터 선정 이유 및 분석 내용")

recommend_sectors_output_parser = JsonOutputParser(pydantic_object=BaseOutputSchema[RecommendSectorsOutputSchema])


RECOMMEND_SECTORS_PROMPT = PromptTemplate.from_template(
    """너는 최고의 미국 주식 시장 분석가입니다. 미국 주식 시장을 한국어로 분석해주세요.

    아래 제공된 미국 거시경제 데이터와 S&P 500 섹터별 가격 데이터를 종합적으로 분석하여,
    향후 가장 유망한 섹터 3개를 예측해주세요.

    ## 미국 거시경제 데이터
    {macro_data}

    ## S&P 500 섹터별 3개월 단위 종가 데이터
    {sector_data}

    분석 시 고려사항:
    1. 거시경제 데이터와 각 섹터의 역사적 상관관계
    2. 현재 거시경제 데이터 수준이 각 섹터에 미치는 영향
    3. 과거 흐름을 참고해서 향후 3개월 내 유망한 섹터 예측

    **중요**: 반드시 아래 JSON 형식을 정확히 따라주세요. 다른 형식으로 출력하지 마세요.

    출력 예시:
    {{
        "Content": [
            {{
                "Sectors": "Technology, Healthcare, Utilities",
                "Analysis": "현재 금리 환경과 경제 성장률을 고려할 때 기술 섹터는 혁신 주도 성장으로 유망합니다. 헬스케어는 인구 고령화로 안정적 수요가 예상되며, 유틸리티는 방어적 투자처로 적합합니다."
            }}
        ]
    }}

    {format_instructions}
    """
).partial(format_instructions=recommend_sectors_output_parser.get_format_instructions())


#----------------------------------------------#
# 요약 프롬프트
#----------------------------------------------#

class SummaryOutputSchema(BaseModel):
    MacroData: str = Field(description="거시경제 데이터(예시: 미국 기준금리, 미국 실업률, 미국 GDP 등)")
    DataAnalysis: str = Field(description="거시경제 데이터 분석 내용")
    RecommendSectors: str = Field(description="추천하는 3개의 섹터명 (예: 'Technology', 'Healthcare', 'Financials')")


summary_output_parser = JsonOutputParser(pydantic_object=BaseOutputSchema[SummaryOutputSchema])


SUMMARY_PROMPT = PromptTemplate.from_template(
    """아래 제공된 분석 내용들을 종합적으로 요약하고 분류해 주세요
    
    
    ## 거시경제 데이터 분석 내용
    {data_package}



    {format_instructions}
    """
).partial(format_instructions=summary_output_parser.get_format_instructions())
#----------------------------------------------#
# 백테스트 분석 프롬프트
#----------------------------------------------#


class BacktestOutputSchema(BaseModel):
    Result: str = Field(description="추천이 잘되었다면 Success 그렇지 않았다면 Failed")
    Feedback: str = Field(description="분석 내용")


backtest_output_parser = JsonOutputParser(pydantic_object=BaseOutputSchema[BacktestOutputSchema])


BACKTEST_PROMPT = PromptTemplate.from_template(
    """너는 최고의 미국 주식 시장 분석가입니다. 미국 주식 시장을 한국어로 분석해주세요.

    당신에게는 3개월전 데이터로 추천한 S&P500 섹터와 분석내용이 제공됩니다.
    해당 내용을 참고하고 현재 데이터와 비교하였을때 3개월전 추천이 잘됐는지 평가해주세요.
    추천이 잘되었다면 Success 그렇지 않았다면 Failed 데이터를 제공해주세요.


    ## 3개월전 데이터로 추천했던 섹터와 분석 내용
    {summary_data}

    ## 현재 거시경제 데이터
    {now_macro_data}

    ## 현재 S&P 500 섹터별 3개월 단위 종가 데이터
    {now_sector_data}

    분석 시 고려사항:
    1. 3개월전에 추천한 섹터가 현재 데이터와 비교하였을때 어떤 결과를 냈는지 분석해줘
    2. 추천한 섹터 3개중에 S&P500 시장 수익률과 비교했을때 수익률이 높은 섹터와 낮은 섹터를 분석해줘
    3. 추천한 섹터 3개중에 2개이상이 S&P500 시장 수익률 보다 좋으면 Success 그렇지 않았다면 Failed 출력해줘

    **중요**: 반드시 아래 JSON 형식을 정확히 따라주세요. 다른 형식으로 출력하지 마세요.

    출력 예시:
    {{
        "Content": [
            {{
                "Result": "Success",
                "Feedback": "추천한 Technology, Healthcare, Utilities 섹터 중 2개가 S&P500을 상회했습니다. Technology는 +15%, Healthcare는 +8%의 수익률을 기록했으나 Utilities는 -2%를 기록했습니다."
            }}
        ]
    }}

    {format_instructions}
    """
).partial(format_instructions=backtest_output_parser.get_format_instructions())





#----------------------------------------------#
# 피드백 분석 프롬프트
#----------------------------------------------#

class FeedbackOutputSchema(BaseModel):
    Sectors: str = Field(description="추천하는 3개의 섹터명 (예: 'Technology', 'Healthcare', 'Financials')")
    Analysis: str = Field(description="섹터 선정 이유 및 분석 내용")


feedback_output_parser = JsonOutputParser(pydantic_object=BaseOutputSchema[FeedbackOutputSchema])


FEEDBACK_PROMPT = PromptTemplate.from_template(
    """
    너는 최고의 미국 주식 시장 분석가입니다. 미국 주식 시장을 한국어로 분석해주세요.
    추천한 섹터가 부정확하여 피드백을 받았습니다
    해당 피드백을 참고하고 추천한 섹터를 수정하여 추천해주세요



    ## 3개월전 데이터로 추천했던 섹터와 분석 내용
    {summary_data}


    ## 피드백 내용
    {backtest_response}

    분석 시 고려사항:
    1. 피드백 내용을 참고하고 추천한 섹터를 수정하여 3개의 섹터를 추천해줘
    2. 과거 흐름을 참고해서 향후 3개월 내 유망한 섹터 예측

    최종 출력 스키마
    {format_instructions}
    """
).partial(format_instructions=feedback_output_parser.get_format_instructions())



final_summary_output_parser = StrOutputParser()

FINAL_SUMMARY_PROMPT = PromptTemplate.from_template(
    """
    당신은 최고의 미국 주식 시장 분석가입니다
    당신의 동료들이 추천한 섹터와 분석 내용을 참고하여 추천한 섹터와 분석 내용을 정리해서
    알기 쉽게 한국어로 설명해주세요
    
    
    분석결과
    {result}
    

    최종 출력 스키마
    {format_instructions}
    """
).partial(format_instructions=StrOutputParser())