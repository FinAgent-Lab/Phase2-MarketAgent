import argparse
from datetime import datetime
from naver_news_daily_report import write_report

def main():
    parser = argparse.ArgumentParser(description="Naver News Daily Report")
    parser.add_argument("--date", type=str, help="Target date (YYYY-MM-DD)")
    args = parser.parse_args()

    if args.date is None:
        target_date = datetime.now().strftime("%Y-%m-%d")
    else:
        target_date = args.date

    write_report(
        date=target_date,
        show_stats=True,
    )

if __name__ == "__main__":
    main()
