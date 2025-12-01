import argparse
from datetime import datetime
from naver_news_daily_report import write_report

def main():
    parser = argparse.ArgumentParser(description="Naver News Daily Report")
    parser.add_argument("--date", type=str, help="Target date (YYYY-MM-DD)")
    parser.add_argument("--categorize-revision", type=str, default="REV00", help="Revision for categorize news")
    parser.add_argument("--build-revision", type=str, default="REV00", help="Revision for build report")
    args = parser.parse_args()

    if args.date is None:
        target_date = datetime.now().strftime("%Y-%m-%d")
    else:
        target_date = args.date

    write_report(
        date=target_date,
        show_stats=True,
        categorize_revision=args.categorize_revision,
        build_revision=args.build_revision,
    )

if __name__ == "__main__":
    main()
