import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import pandas as pd
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from Agent.Chain.FredChain import FredRateSectorAnalyzer


# GraphState 상태를 저장하는 용도로 사용합니다.
class GraphState(TypedDict):
    # 분석 결과
    first_result: dict
    backtest_result: dict
    feedback_result: dict


analyzer = FredRateSectorAnalyzer()


def first_llm_chain(state: GraphState):
    """노드 1: 첫 번째 분석"""
    state["first_result"] = analyzer.first_analysis()
    return state


def backtest_llm_chain(state: GraphState):
    """노드 2: 백테스트 - State에서 first_result 전달"""
    first_result = state["first_result"]
    state["backtest_result"] = analyzer.backtest_analysis(first_result)
    return state


def feedback_llm_chain(state: GraphState):
    """노드 3: 피드백 - State에서 first_result와 backtest_result 전달"""
    first_result = state["first_result"]
    backtest_result = state["backtest_result"]
    state["feedback_result"] = analyzer.feedback_analysis(first_result, backtest_result)
    return state


def should_feedback(state: GraphState) -> str:
    """조건부 라우팅: Failed일 때만 feedback 노드로"""
    if state["backtest_result"]["Result"] == "Failed":
        return "feedback"
    return "end"


# LangGraph 구성
workflow = StateGraph(GraphState)

workflow.add_node("first_analysis", first_llm_chain)
workflow.add_node("backtest", backtest_llm_chain)
workflow.add_node("feedback", feedback_llm_chain)

workflow.add_edge(START, "first_analysis")
workflow.add_edge("first_analysis", "backtest")

# 조건부 엣지
workflow.add_conditional_edges(
    "backtest",
    should_feedback,
    {
        "feedback": "feedback",
        "end": END
    }
)
workflow.add_edge("feedback", END)

# 컴파일
FredGraph = workflow.compile()


if __name__ == "__main__":
    print("🚀섹터 분석 시작\n")
    
    # 그래프 실행
    result = FredGraph.invoke({})
    
    # 결과 출력
    print("\n" + "="*60)
    print("📊 최종 결과")
    print("="*60)
    
    print(f"\n[1단계] 첫 번째 추천 섹터:")
    print(f"  섹터: {result['first_result']['Sectors']}")
    print(f"  분석: {result['first_result']['Analysis']}\n")
    
    print(f"[2단계] 백테스트 결과:")
    print(f"  결과: {result['backtest_result']['Result']}")
    print(f"  피드백: {result['backtest_result']['Feedback']}\n")
    
    if result['backtest_result']['Result'] == "Failed":
        print(f"[3단계] 피드백 후 수정된 추천:")
        print(f"  섹터: {result['feedback_result']['Sectors']}")
        print(f"  분석: {result['feedback_result']['Analysis']}")
    else:
        print(f"[3단계] 백테스트 성공으로 피드백 생략")
    
    print("\n" + "="*60 + "\n")
