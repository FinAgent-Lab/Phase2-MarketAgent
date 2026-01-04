# Daily Market Report (LLM-ready) — 2026-01-02

## How to use this file (for an LLM)
- Summarize today's market in 5–8 bullet points.
- Identify the biggest winners/losers and possible drivers.
- Comment on volatility (intraday range) and risk regime.
- Use the **Raw table** section for grounding and quoting numbers.

## Metric definitions
- **ret_pct**: (Close - Open) / Open * 100
- **range_pct**: (High - Low) / Open * 100
- **close_over_open**: Close / Open
- **candle_dir**: sign(Close - Open) → +1(up), 0(flat), -1(down)

## Executive summary (auto)
- Best performer: **BITCOIN** (1.266%)
- Worst performer: **NASDAQ** (-1.047%)
- Highest intraday range: **BITCOIN** (2.828%)
- Risk regime inference: **Risk-off (provisional)** (score=-1.25)
  - Evidence:
    - Equity mean return: -0.025%
    - USD/KRW return: -0.010% (inverse tilt)
    - DXY return: 0.180% (inverse tilt)
    - Gold return: -0.009% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.625% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| BITCOIN     |  1.26578  |
| RUSSELL2000 |  0.658316 |
| US5YT       |  0.646021 |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| NASDAQ  | -1.04705  |
| S&P500  | -0.285538 |
| USD/KRW | -0.009706 |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| BITCOIN |     2.82841 |
| GOLD    |     2.19123 |
| NASDAQ  |     1.98652 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-02 | 23481.5   | 23586     | 23119.5   | 23235.6   |      6.0672e+09  | -1.04705  |    1.98652  |          0.989529 |           -1 |
| S&P500           | 2026-01-02 |  6878.11  |  6894.87  |  6824.31  |  6858.47  |      2.62904e+09 | -0.285538 |    1.02586  |          0.997145 |           -1 |
| DOWJONES         | 2026-01-02 | 48106     | 48404.1   | 47853     | 48382.4   |      4.646e+08   |  0.574586 |    1.14543  |          1.00575  |            1 |
| RUSSELL2000      | 2026-01-02 |  2491.82  |  2509.72  |  2481.59  |  2508.22  |      0           |  0.658316 |    1.12886  |          1.00658  |            1 |
| USD/KRW          | 2026-01-02 |  1442.63  |  1447.53  |  1438.68  |  1442.49  |      0           | -0.009706 |    0.613461 |          0.999903 |           -1 |
| Dallor Index/USD | 2026-01-02 |    98.235 |    98.494 |    98.145 |    98.412 |      0           |  0.180182 |    0.355277 |          1.0018   |            1 |
| GOLD             | 2026-01-02 |  4340     |  4414.8   |  4319.7   |  4339.6   | 148868           | -0.009214 |    2.19123  |          0.999908 |           -1 |
| BITCOIN          | 2026-01-02 | 88725.5   | 90832.9   | 88323.3   | 89848.5   |      4.61933e+10 |  1.26578  |    2.82841  |          1.01266  |            1 |
| US5YT            | 2026-01-02 |     3.715 |     3.748 |     3.713 |     3.739 |      0           |  0.646021 |    0.942122 |          1.00646  |            1 |
| US10YT           | 2026-01-02 |     4.161 |     4.197 |     4.159 |     4.187 |      0           |  0.624839 |    0.913245 |          1.00625  |            1 |
| US30YT           | 2026-01-02 |     4.845 |     4.875 |     4.843 |     4.864 |      0           |  0.392148 |    0.660476 |          1.00392  |            1 |
