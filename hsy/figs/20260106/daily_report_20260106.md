# Daily Market Report (LLM-ready) — 2026-01-06

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
- Best performer: **RUSSELL2000** (2.626%)
- Worst performer: **BITCOIN** (-0.308%)
- Highest intraday range: **BITCOIN** (3.011%)
- Risk regime inference: **Mixed / unclear (provisional)** (score=0.25)
  - Evidence:
    - Equity mean return: 1.136%
    - USD/KRW return: 0.069% (inverse tilt)
    - DXY return: 0.206% (inverse tilt)
    - Gold return: 1.043% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.144% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| RUSSELL2000 |  2.62604  |
| GOLD        |  1.04265  |
| DOWJONES    |  0.969064 |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| BITCOIN | -0.307567 |
| US30YT  |  0.020553 |
| USD/KRW |  0.069133 |

### Top 3 intraday ranges (range_pct)
| stock       |   range_pct |
|:------------|------------:|
| BITCOIN     |     3.01125 |
| RUSSELL2000 |     1.6436  |
| GOLD        |     1.47541 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-06 | 23449.7   | 23559.2   | 23389.6   | 23547.2   |      7.80369e+09 |  0.415801 |    0.723175 |          1.00416  |            1 |
| S&P500           | 2026-01-06 |  6908.03  |  6948.69  |  6904.02  |  6944.82  |      3.29113e+09 |  0.532569 |    0.646638 |          1.00533  |            1 |
| DOWJONES         | 2026-01-06 | 48987.4   | 49509.9   | 48923.8   | 49462.1   |      5.41263e+08 |  0.969064 |    1.19642  |          1.00969  |            1 |
| RUSSELL2000      | 2026-01-06 |  2516.81  |  2582.99  |  2541.63  |  2582.9   |      0           |  2.62604  |    1.6436   |          1.02626  |            1 |
| USD/KRW          | 2026-01-06 |  1446.48  |  1449.38  |  1441.78  |  1447.48  |      0           |  0.069133 |    0.525412 |          1.00069  |            1 |
| Dallor Index/USD | 2026-01-06 |    98.411 |    98.626 |    98.161 |    98.614 |      0           |  0.206273 |    0.472504 |          1.00206  |            1 |
| GOLD             | 2026-01-06 |  4459.8   |  4503.7   |  4437.9   |  4506.3   | 166520           |  1.04265  |    1.47541  |          1.01043  |            1 |
| BITCOIN          | 2026-01-06 | 93861.7   | 94352.7   | 91526.3   | 93573     |      5.13076e+10 | -0.307567 |    3.01125  |          0.996924 |           -1 |
| US5YT            | 2026-01-06 |     3.715 |     3.724 |     3.708 |     3.72  |      0           |  0.134586 |    0.430687 |          1.00135  |            1 |
| US10YT           | 2026-01-06 |     4.173 |     4.181 |     4.165 |     4.179 |      0           |  0.143782 |    0.383424 |          1.00144  |            1 |
| US30YT           | 2026-01-06 |     4.865 |     4.884 |     4.854 |     4.866 |      0           |  0.020553 |    0.616644 |          1.00021  |            1 |
