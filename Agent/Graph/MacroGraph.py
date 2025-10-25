import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import pandas as pd


from fredapi import Fred
from dotenv import load_dotenv

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from datetime import datetime
from dateutil.relativedelta import relativedelta


from Agent.Util.Yfinace3moData import yfinance_get_sectors_data
from Agent.Util.LLM import create_llm


from Agent.MacroData.FundsRate import get_funds_rate_data
from Agent.MacroData.GDP import get_gdp_data
from Agent.MacroData.UmEmployMent import get_unemployment_rate
from Agent.MacroData.NonFarmPayrolls import get_nonfarm_payrolls
from Agent.MacroData.CPI import get_cpi_data


from Agent.Prompt.Prompts import *
from Agent.Chain.Chains import *

load_dotenv()

model = create_llm(model="openai/gpt-4o")
three_months_ago = (datetime.now() - relativedelta(months=3)).strftime("%Y-%m")
fred = Fred(api_key=os.getenv('FRED_API_KEY'))

# GraphState 상태를 저장하는 용도로 사용합니다.
class GraphState(TypedDict):
    # S&P500 섹터데이터
    SectorData: dict
    SectorData3monthsAgo: dict
    
    # 매크로 경제 데이터 (한 번만 호출하여 재사용)
    FundsRateData: pd.DataFrame
    GDPData: pd.DataFrame
    UnemploymentData: pd.DataFrame
    NonfarmPayrollsData: pd.DataFrame
    CPIData: pd.DataFrame
    
    # 거시경제 기준 섹터 추천 결과
    FundsRateRecommendSectors: dict
    GDPRecommendSectors: dict
    UnemploymentRecommendSector: dict
    NonfarmPayrollsRecommendSector: dict
    CPIRecommendSector: dict
    # 요약 결과
    SummaryResult: dict
    
    # 백테스트 결과
    EvaluationResult: dict
    
    # 피드백 결과
    FeedbackResult: dict
    
    # 최종 요약
    FinalSummary: str

    # 반복 제어
    IterationCount: int  # 현재 반복 횟수


def initialize_data(state: GraphState) -> dict:
    """섹터 데이터와 매크로 데이터를 한 번에 불러와 초기화"""
    # 시작 날짜 설정 (기본값: 2008-01)
    start_date = "2008-01"
    iteration_count = 0
    
    # 섹터 데이터 로드
    sector_result = yfinance_get_sectors_data(start_year=int(start_date.split('-')[0]))
    
    # 매크로 데이터 한 번에 로드
    funds_rate_data = get_funds_rate_data(fred)
    gdp_data = get_gdp_data(fred)
    unemployment_data = get_unemployment_rate(fred)
    nonfarm_payrolls_data = get_nonfarm_payrolls(fred)
    cpi_data = get_cpi_data(fred)
    
    
    return {
        "IterationCount": iteration_count,
        "SectorData": sector_result,
        "SectorData3monthsAgo": sector_result.loc[:three_months_ago],
        "FundsRateData": funds_rate_data,
        "GDPData": gdp_data,
        "UnemploymentData": unemployment_data,
        "NonfarmPayrollsData": nonfarm_payrolls_data,
        "CPIData": cpi_data,
        
    }


def recommend_sectors(state: GraphState):
    """모든 매크로 지표 기반 섹터 추천을 한 번에 처리"""
    sector_data = state["SectorData3monthsAgo"]
    

    macro_data_mapping = {
        "FundsRateData": "FundsRateRecommendSectors",
        "GDPData": "GDPRecommendSectors",
        "UnemploymentData": "UnemploymentRecommendSector",
        "NonfarmPayrollsData": "NonfarmPayrollsRecommendSector",
        "CPIData": "CPIRecommendSector",
    }
    
    results = {}
    
    # 각 매크로 데이터에 대해 섹터 추천 수행
    for data_key, result_key in macro_data_mapping.items():
        macro_data = state[data_key]
        macro_data_3months_ago = macro_data.loc[:three_months_ago]
        
        results[result_key] = recommend_sectors_chain(
            llm=model,
            macro_data=macro_data_3months_ago,
            sector_data=sector_data,
            prompt=RECOMMEND_SECTORS_PROMPT
        )
    
    return results



def summarize_recommend_data(state: GraphState):
    
    data_merge = pd.DataFrame({
        "FundsRateRecommendSectors": state["FundsRateRecommendSectors"],
        "GDPRecommendSectors": state["GDPRecommendSectors"],
        "UnemploymentRecommendSector": state["UnemploymentRecommendSector"],
        "NonfarmPayrollsRecommendSector": state["NonfarmPayrollsRecommendSector"],
        "CPIRecommendSector": state["CPIRecommendSector"],
    })
    
    result = summarize_data_chain(
        llm=model,
        data_package=data_merge,
        prompt=SUMMARY_PROMPT
    )
    return {
        "SummaryResult": result
    }



def run_evaluation(state: GraphState):
    summary_data = state["SummaryResult"]

    now_macro_data_merge = pd.concat(
        [
            state["FundsRateData"],
            state["GDPData"],
            state["UnemploymentData"],
            state["NonfarmPayrollsData"],
            state["CPIData"],
        ],
        axis=1
    )

    result = evaluation_chain(
        llm=model,
        summary_data=summary_data,
        now_macro_data=now_macro_data_merge,
        now_sector_data=state["SectorData"],
        prompt=EVALUATION_PROMPT
    )

    return {
        "EvaluationResult": result
    }
    
    
def feedback_analysis(state: GraphState):
    summary_data = state["SummaryResult"]
    evaluation_response = state["EvaluationResult"]
    iteration_count = state.get("IterationCount", 0)
    
    result = feedback_analysis_chain(
        llm=model,
        summary_data=summary_data,
        evaluation_response=evaluation_response,
        prompt=FEEDBACK_PROMPT
    )
    
    return {
        "FeedbackResult": result,
        "IterationCount": iteration_count + 1  # 반복 횟수 증가
    }


def should_feedback(state: GraphState) -> str:
    """조건부 라우팅: Failed일 때만 feedback 노드로 (최대 5번)"""
    iteration_count = state.get("IterationCount", 0)
    
    # 5번 이상 반복했으면 종료
    if iteration_count >= 5:
        return "end"
    
    # BacktestResult에서 Result 확인
    try:
        result = state["EvaluationResult"]["Content"][0]["Result"]
        
        if result == "Success":
            return "end"
        elif result == "Failed":
            return "feedback"
        else:
            return "end"
            
    except (KeyError, IndexError, TypeError):
        return "end"


def final_summary(state: GraphState):
    """최종 결과를 요약해서 출력"""
    # state의 모든 결과를 종합
    result_package = {
        "summary": state.get("SummaryResult", {}),
        "backtest": state.get("EvaluationResult", {}),
    }

    model = create_llm(model="openai/gpt-5")
    final_result = final_summary_chain(
        llm=model,
        result=result_package,
        prompt=FINAL_SUMMARY_PROMPT
    )

    return {
        "FinalSummary": final_result
    }


workflow = StateGraph(GraphState)
workflow.add_node("initialize_data", initialize_data)
workflow.add_node("recommend_sectors", recommend_sectors)
workflow.add_node("summarize_recommend_data", summarize_recommend_data)
workflow.add_node("run_evaluation", run_evaluation)
workflow.add_node("feedback_analysis", feedback_analysis)
workflow.add_node("final_summary", final_summary)

workflow.add_edge(START, "initialize_data")
workflow.add_edge("initialize_data", "recommend_sectors")
workflow.add_edge("recommend_sectors", "summarize_recommend_data")
workflow.add_edge("summarize_recommend_data", "run_evaluation")
workflow.add_conditional_edges(
    "run_evaluation",
    should_feedback,
    {
        "feedback": "feedback_analysis",
        "end": "final_summary"
    }
)

workflow.add_edge("feedback_analysis", "run_evaluation")
workflow.add_edge("final_summary", END)


MacroGraph = workflow.compile()



if __name__ == "__main__":
    print("🚀매크로 경제 분석 시작\n")
    
    # 그래프 실행
    result = MacroGraph.invoke({})
    
    # 디버깅: 각 매크로 지표별 추천 결과
    print("\n" + "="*60)
    print("🔍 각 매크로 지표별 추천 결과")
    print("="*60)
    print("\n📈 FundsRate 추천:", result.get("FundsRateRecommendSectors"))
    print("\n📈 GDP 추천:", result.get("GDPRecommendSectors"))
    print("\n📈 Unemployment 추천:", result.get("UnemploymentRecommendSector"))
    print("\n📈 NonFarmPayrolls 추천:", result.get("NonfarmPayrollsRecommendSector"))
    print("\n📈 CPI 추천:", result.get("CPIRecommendSector"))
    
    # 디버깅: 요약 결과
    print("\n" + "="*60)
    print("🔍 [DEBUG] 요약 결과")
    print("="*60)
    print(result.get("SummaryResult"))
    
    # 디버깅: 백테스트 결과
    print("\n" + "="*60)
    print("🔍 [DEBUG] 평가 결과")
    print("="*60)
    print(result.get("EvaluationResult"))
    
    # 최종 결과 출력
    print("\n" + "="*60)
    print("📊 최종 요약")
    print("="*60)
    
    if "FinalSummary" in result:
        print(result["FinalSummary"])
    else:
        print("❌ FinalSummary를 찾을 수 없습니다.")
        print(f"사용 가능한 키: {list(result.keys())}")
    
    print("\n" + "="*60)
