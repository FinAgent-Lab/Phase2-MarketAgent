import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Generate final report for users.")
    parser.add_argument('--date', type=str, required=True, help='Date in YYYY-MM-DD format')
    args = parser.parse_args()

    date_str = args.date  # e.g., 2026-01-01
    date_compact = date_str.replace('-', '')  # e.g., 20260101

    base_dir = os.path.dirname(os.path.abspath(__file__))
    figs_dir = os.path.join(base_dir, 'figs', date_compact)
    output_dir = os.path.join(base_dir, 'final_reports')
    
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Path to the daily report inside figs (for status check)
    figs_daily_report_path = os.path.join(figs_dir, f'daily_report_{date_compact}.md')
    
    is_closed = False
    
    # Check if market is closed
    if os.path.exists(figs_daily_report_path):
        with open(figs_daily_report_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            content = "".join(lines)
            
            # Logic: Status has "휴장" AND lines <= 20
            if len(lines) <= 20 and "Status" in content and "휴장" in content:
                is_closed = True
    
    final_content = ""

    if is_closed:
        final_content += "# Market overview\n\n휴장으로 지표가 없습니다.\n\n"
    else:
        market_overview_path = os.path.join(figs_dir, f'market_overview_{date_compact}_for_users.md')
        if os.path.exists(market_overview_path):
            with open(market_overview_path, 'r', encoding='utf-8') as f:
                final_content += f.read() + "\n\n"
        
        # Append images
        images_to_append = [
            "AllStocks_Subplots.png",
            "DailyReturn.png",
            "IntradayRange.png",
            "volume_vs_return.png"
        ]
        
        for img_name in images_to_append:
            img_path = os.path.join(figs_dir, img_name)
            rel_path = f"../figs/{date_compact}/{img_name}"
            final_content += f"![{img_name}]({rel_path})\n\n"

    # Lastly, append summary_news/summary_news_{date_str}.md
    summary_news_dir = os.path.join(base_dir, 'summary_news')
    summary_news_path = os.path.join(summary_news_dir, f'summary_news_{date_str}.md')
    
    if os.path.exists(summary_news_path):
        with open(summary_news_path, 'r', encoding='utf-8') as f:
            final_content += f.read() + "\n"
    
    # Save to final_reports
    final_output_path = os.path.join(output_dir, f'final_report_{date_str}.md')
    
    with open(final_output_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"Successfully generated report at: {final_output_path}")

if __name__ == "__main__":
    main()
