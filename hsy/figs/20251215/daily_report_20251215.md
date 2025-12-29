# Daily Market Report (LLM-ready) — 2025-12-15

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
- Best performer: **US30YT** (0.331%)
- Worst performer: **BITCOIN** (-1.986%)
- Highest intraday range: **BITCOIN** (5.308%)
- Risk regime inference: **Risk-off (provisional)** (score=-0.75)
  - Evidence:
    - Equity mean return: -0.853%
    - USD/KRW return: 0.000% (inverse tilt)
    - DXY return: -0.254% (inverse tilt)
    - Gold return: -0.037% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.288% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| US30YT  |  0.330916 |
| US10YT  |  0.287772 |
| US5YT   |  0.187868 |

### Bottom 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| BITCOIN     |  -1.98625 |
| RUSSELL2000 |  -1.24215 |
| NASDAQ      |  -1.16857 |

### Top 3 intraday ranges (range_pct)
| stock       |   range_pct |
|:------------|------------:|
| BITCOIN     |     5.30769 |
| RUSSELL2000 |     1.48643 |
| NASDAQ      |     1.42975 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |        Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|--------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2025-12-15 | 23330     | 23345.6   | 23012     | 23057.4   |   8.64924e+09 | -1.16857  |    1.42975  |          0.988314 |           -1 |
| S&P500           | 2025-12-15 |  6860.19  |  6861.59  |  6801.49  |  6816.51  |   4.9756e+09  | -0.63672  |    0.876063 |          0.993633 |           -1 |
| DOWJONES         | 2025-12-15 | 48594.4   | 48679.1   | 48283.3   | 48416.6   |   5.1663e+08  | -0.365888 |    0.814644 |          0.996341 |           -1 |
| RUSSELL2000      | 2025-12-15 |  2562.5   |  2567.46  |  2529.37  |  2530.67  |   4.9756e+09  | -1.24215  |    1.48643  |          0.987579 |           -1 |
| USD/KRW          | 2025-12-15 |  1472.91  |  1477.75  |  1462.42  |  1472.91  |   0           |  0        |    1.04079  |          1        |            0 |
| Dallor Index/USD | 2025-12-15 |    98.4   |    98.48  |    98.14  |    98.15  |   0           | -0.254065 |    0.345532 |          0.997459 |           -1 |
| GOLD             | 2025-12-15 |  4308.3   |  4349.2   |  4292.9   |  4306.7   | 854           | -0.037129 |    1.30679  |          0.999629 |           -1 |
| BITCOIN          | 2025-12-15 | 88171.1   | 89983.9   | 85304.1   | 86419.8   |   4.55595e+10 | -1.98625  |    5.30769  |          0.980138 |           -1 |
| US5YT            | 2025-12-15 |     3.726 |     3.738 |     3.701 |     3.733 |   0           |  0.187868 |    0.99302  |          1.00188  |            1 |
| US10YT           | 2025-12-15 |     4.17  |     4.186 |     4.151 |     4.182 |   0           |  0.287772 |    0.839325 |          1.00288  |            1 |
| US30YT           | 2025-12-15 |     4.835 |     4.853 |     4.818 |     4.851 |   0           |  0.330916 |    0.723895 |          1.00331  |            1 |
