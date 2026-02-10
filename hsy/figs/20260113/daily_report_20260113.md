# Daily Market Report (LLM-ready) — 2026-01-13

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
- Best performer: **BITCOIN** (3.233%)
- Worst performer: **DOWJONES** (-0.856%)
- Highest intraday range: **BITCOIN** (3.818%)
- Risk regime inference: **Risk-off (provisional)** (score=-2.25)
  - Evidence:
    - Equity mean return: -0.143%
    - USD/KRW return: 0.787% (inverse tilt)
    - DXY return: 0.268% (inverse tilt)
    - Gold return: -0.299% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.525% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| BITCOIN |  3.23281  |
| NASDAQ  |  0.909347 |
| USD/KRW |  0.786523 |

### Bottom 3 daily returns (ret_pct)
| stock    |   ret_pct |
|:---------|----------:|
| DOWJONES | -0.856483 |
| US5YT    | -0.742505 |
| US10YT   | -0.52468  |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| BITCOIN |     3.81813 |
| US5YT   |     1.67064 |
| GOLD    |     1.45987 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-13 | 23496.2   | 23813.3   | 23607.6   | 23709.9   |      8.27739e+09 |  0.909347 |    0.87549  |          1.00909  |            1 |
| S&P500           | 2026-01-13 |  6977.41  |  6985.83  |  6938.77  |  6963.74  |      3.22414e+09 | -0.195917 |    0.674463 |          0.998041 |           -1 |
| DOWJONES         | 2026-01-13 | 49616.9   | 49616.9   | 49056.3   | 49192     |      5.4996e+08  | -0.856483 |    1.12994  |          0.991435 |           -1 |
| RUSSELL2000      | 2026-01-13 |  2644.49  |  2647.04  |  2627.4   |  2633.1   |      0           | -0.430435 |    0.742507 |          0.995696 |           -1 |
| USD/KRW          | 2026-01-13 |  1465.95  |  1477.59  |  1465.95  |  1477.48  |      0           |  0.786523 |    0.794025 |          1.00787  |            1 |
| Dallor Index/USD | 2026-01-13 |    98.898 |    99.227 |    98.853 |    99.163 |      0           |  0.267952 |    0.378168 |          1.00268  |            1 |
| GOLD             | 2026-01-13 |  4610     |  4644     |  4576.7   |  4596.2   | 248288           | -0.299345 |    1.45987  |          0.997007 |           -1 |
| BITCOIN          | 2026-01-13 | 91195.6   | 94468.9   | 90986.9   | 94143.8   |      4.75928e+10 |  3.23281  |    3.81813  |          1.03233  |            1 |
| US5YT            | 2026-01-13 |     3.771 |     3.785 |     3.722 |     3.743 |      0           | -0.742505 |    1.67064  |          0.992575 |           -1 |
| US10YT           | 2026-01-13 |     4.193 |     4.195 |     4.156 |     4.171 |      0           | -0.52468  |    0.930122 |          0.994753 |           -1 |
| US30YT           | 2026-01-13 |     4.844 |     4.848 |     4.821 |     4.828 |      0           | -0.330301 |    0.55739  |          0.996697 |           -1 |
