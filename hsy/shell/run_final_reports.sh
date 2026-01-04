#!/bin/bash

# start_date와 end_date를 입력받아서 stock_info.py를 실행하는 스크립트
# 사용법: ./run_stock_info.sh 2025-12-10 2025-12-20

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <start_date> <end_date>"
    echo "Example: $0 2025-12-10 2025-12-20"
    exit 1
fi

START_DATE=$1
END_DATE=$2

# 스크립트가 있는 디렉토리의 상위 디렉토리로 이동 (hsy 폴더로 이동 예상)
cd "$(dirname "$0")/.." || exit

current_date="$START_DATE"

# 날짜 비교 및 루프
while [[ "$current_date" < "$END_DATE" ]] || [[ "$current_date" == "$END_DATE" ]]; do
    echo "Processing date: $current_date"
    
    # uv run 실행
    uv run make_report_for_users.py --date "$current_date"
    
    # 날짜 하루 증가 (GNU date 기준)
    # Mac이나 BSD 계열에서는 다른 date 문법이 필요할 수 있음
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS (BSD date)
        current_date=$(date -j -v+1d -f "%Y-%m-%d" "$current_date" "+%Y-%m-%d")
    else
        # Linux / Windows Git Bash (GNU date)
        current_date=$(date -I -d "$current_date + 1 day")
    fi
    
    # 날짜 계산 실패 시 중단
    if [ $? -ne 0 ] || [ -z "$current_date" ]; then
        echo "Error: Failed to calculate next date."
        exit 1
    fi
done
