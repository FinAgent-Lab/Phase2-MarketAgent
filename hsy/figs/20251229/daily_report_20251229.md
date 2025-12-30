# Daily Market Report (LLM-ready) — 2025-12-29

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
- Best performer: **NASDAQ** (0.255%)
- Worst performer: **GOLD** (-4.777%)
- Highest intraday range: **GOLD** (5.808%)
- Risk regime inference: **Mixed / unclear (provisional)** (score=-0.25)
  - Evidence:
    - Equity mean return: -0.068%
    - USD/KRW return: -0.449% (inverse tilt)
    - DXY return: -0.047% (inverse tilt)
    - Gold return: -4.777% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.000% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| NASDAQ  |  0.25484  |
| US30YT  |  0.125017 |
| S&P500  |  0.031    |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| GOLD    | -4.77671  |
| BITCOIN | -0.709129 |
| USD/KRW | -0.449387 |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| GOLD    |    5.80779  |
| BITCOIN |    3.83576  |
| USD/KRW |    0.981296 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2025-12-29 | 23414.7   | 23531     | 23397.5   | 23474.3   |      5.75262e+09 |  0.25484  |    0.570163 |          1.00255  |            1 |
| S&P500           | 2025-12-29 |  6903.6   |  6920.21  |  6888.76  |  6905.74  |      1.92287e+09 |  0.031    |    0.455562 |          1.00031  |            1 |
| DOWJONES         | 2025-12-29 | 48636.6   | 48704.8   | 48390.9   | 48461.9   |      3.21913e+08 | -0.359193 |    0.645435 |          0.996408 |           -1 |
| RUSSELL2000      | 2025-12-29 |  2524.84  |  2533.65  |  2515.67  |  2519.8   |      0           | -0.199686 |    0.712085 |          0.998003 |           -1 |
| USD/KRW          | 2025-12-29 |  1441.96  |  1442.83  |  1428.68  |  1435.48  |      0           | -0.449387 |    0.981296 |          0.995506 |           -1 |
| Dallor Index/USD | 2025-12-29 |    98.049 |    98.177 |    97.915 |    98.003 |      0           | -0.046921 |    0.267214 |          0.999531 |           -1 |
| GOLD             | 2025-12-29 |  4568     |  4581.3   |  4316     |  4349.8   | 306734           | -4.77671  |    5.80779  |          0.952233 |           -1 |
| BITCOIN          | 2025-12-29 | 87858.6   | 90228.7   | 86858.6   | 87235.6   |      4.88594e+10 | -0.709129 |    3.83576  |          0.992909 |           -1 |
| US5YT            | 2025-12-29 |     3.68  |     3.689 |     3.668 |     3.677 |      0           | -0.081516 |    0.57065  |          0.999185 |           -1 |
| US10YT           | 2025-12-29 |     4.116 |     4.13  |     4.108 |     4.116 |      0           |  0        |    0.534496 |          1        |            0 |
| US30YT           | 2025-12-29 |     4.799 |     4.815 |     4.794 |     4.805 |      0           |  0.125017 |    0.437599 |          1.00125  |            1 |
