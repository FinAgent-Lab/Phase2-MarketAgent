"""
간단한 FastAPI - FinAgent Market Agent
MacroGraph만 실행하고 결과 반환
"""

import os
import sys
from datetime import datetime

# 프로젝트 루트 경로 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Agent.Graph.MacroGraph import MacroGraph
import uvicorn

# FastAPI 앱 생성
app = FastAPI(title="FinAgent API", version="1.0.0")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """서버 상태 확인"""
    return {"message": "FinAgent API", "status": "running"}


@app.get("/health")
async def health():
    """헬스 체크"""
    return {"status": "healthy"}


@app.post("/analyze")
async def analyze():
    """매크로 경제 분석 실행"""
    try:
        print("🚀 분석 시작...")
        result = MacroGraph.invoke({})
        print("✅ 분석 완료!")

        return {
            "status": "completed",
            "message": "분석이 완료되었습니다.",
            "data": {
                "final_summary": result.get("FinalSummary"),
                "funds_rate_recommendation": result.get("FundsRateRecommendSectors"),
                "gdp_recommendation": result.get("GDPRecommendSectors"),
                "unemployment_recommendation": result.get(
                    "UnemploymentRecommendSector"
                ),
                "nonfarm_payrolls_recommendation": result.get(
                    "NonfarmPayrollsRecommendSector"
                ),
                "cpi_recommendation": result.get("CPIRecommendSector"),
                "summary_result": result.get("SummaryResult"),
                "evaluation_result": result.get("EvaluationResult"),
                "iteration_count": result.get("IterationCount", 0),
            },
            "timestamp": datetime.now().isoformat(),
        }
    except Exception as e:
        print(f"❌ 분석 실패: {str(e)}")
        return {
            "status": "failed",
            "message": f"분석 실패: {str(e)}",
            "timestamp": datetime.now().isoformat(),
        }


if __name__ == "__main__":
    print("🚀 FinAgent API 서버 시작")
    uvicorn.run(app, host="0.0.0.0", port=8000)
