"""
FinAgent Market Agent Streamlit 대시보드
FastAPI를 통한 매크로 경제 분석 및 섹터 추천 결과 표시
"""

import streamlit as st
import requests
import json

# API 기본 URL
API_BASE_URL = "http://localhost:8000"


def main():
    """메인 애플리케이션"""
    st.set_page_config(
        page_title="FinAgent Market Agent", page_icon="📊", layout="wide"
    )

    # 헤더
    st.title("📊 FinAgent Market Agent")
    st.markdown("AI 기반 S&P 500 섹터 분석 및 투자 추천")

    # API 연결 확인
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        if response.status_code != 200:
            st.error("❌ API 서버에 연결할 수 없습니다.")
            st.info("FastAPI 서버 실행: `cd InterFace && python FastAPI.py`")
            return
    except:
        st.error("❌ API 서버에 연결할 수 없습니다.")
        st.info("FastAPI 서버 실행: `cd InterFace && python FastAPI.py`")
        return

    # 분석 시작 버튼
    if st.button("🚀 분석 시작", type="primary", use_container_width=True):
        with st.spinner("분석 중... (약 3~5분 소요)"):
            try:
                # FastAPI로 분석 요청
                response = requests.post(f"{API_BASE_URL}/analyze")

                if response.status_code == 200:
                    result = response.json()

                    if result["status"] == "completed":
                        st.success("✅ 분석 완료!")

                        # 최종 요약
                        if result["data"]["final_summary"]:
                            st.markdown("## 📊 최종 분석 요약")
                            st.markdown(result["data"]["final_summary"])

                        # 각 지표별 섹터 추천
                        st.markdown("## 🔍 지표별 섹터 추천")

                        col1, col2 = st.columns(2)

                        with col1:
                            st.markdown("### 📈 기준금리 분석")
                            st.json(result["data"]["funds_rate_recommendation"])

                            st.markdown("### 📊 GDP 분석")
                            st.json(result["data"]["gdp_recommendation"])

                            st.markdown("### 👥 실업률 분석")
                            st.json(result["data"]["unemployment_recommendation"])

                        with col2:
                            st.markdown("### 💼 비농업 고용 분석")
                            st.json(result["data"]["nonfarm_payrolls_recommendation"])

                            st.markdown("### 💰 CPI 분석")
                            st.json(result["data"]["cpi_recommendation"])

                        # 성과 검증 결과
                        st.markdown("## 📊 추천 성과 검증")
                        st.json(result["data"]["evaluation_result"])

                        # 반복 횟수
                        st.info(
                            f"분석 반복 횟수: {result['data']['iteration_count']}회"
                        )

                    else:
                        st.error(f"❌ 분석 실패: {result['message']}")

                else:
                    st.error("❌ API 요청 실패")

            except Exception as e:
                st.error(f"❌ 오류 발생: {str(e)}")


if __name__ == "__main__":
    main()
