#!/usr/bin/env python3
"""
간단한 시작 스크립트 - Windows용
"""
import os
import sys
import subprocess
from pathlib import Path


def main():
    """간단하게 시작"""
    print("🚀 FinAgent Market Agent 시작")
    print("🌐 FastAPI: http://localhost:8000")
    print("🌐 Streamlit: http://localhost:8501")
    print("-" * 50)

    # InterFace 디렉토리로 이동
    interface_dir = Path(__file__).parent / "InterFace"
    os.chdir(interface_dir)

    try:
        # FastAPI 시작 (백그라운드)
        print("🚀 FastAPI 백엔드 시작...")
        fastapi_process = subprocess.Popen([sys.executable, "FastAPI.py"])

        # 잠시 대기
        import time

        time.sleep(3)

        # Streamlit 시작
        print("🚀 Streamlit 프론트엔드 시작...")
        subprocess.run([sys.executable, "-m", "streamlit", "run", "Streamlit.py"])

    except KeyboardInterrupt:
        print("\n🛑 서버 중지 중...")
        try:
            fastapi_process.terminate()
        except:
            pass
        print("✅ 모든 서버가 중지되었습니다.")
    except Exception as e:
        print(f"❌ 오류: {e}")


if __name__ == "__main__":
    main()
