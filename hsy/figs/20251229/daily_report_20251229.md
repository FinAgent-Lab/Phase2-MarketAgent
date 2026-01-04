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
- Best performer: **USD/KRW** (0.518%)
- Worst performer: **GOLD** (-1.061%)
- Highest intraday range: **BITCOIN** (4.077%)
- Risk regime inference: **Risk-off (provisional)** (score=-1.25)
  - Evidence:
    - Equity mean return: -0.068%
    - USD/KRW return: 0.518% (inverse tilt)
    - DXY return: -0.010% (inverse tilt)
    - Gold return: -1.061% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.000% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| USD/KRW |  0.518162 |
| NASDAQ  |  0.25484  |
| US30YT  |  0.125027 |

### Bottom 3 daily returns (ret_pct)
| stock    |   ret_pct |
|:---------|----------:|
| GOLD     | -1.06142  |
| BITCOIN  | -0.794264 |
| DOWJONES | -0.359193 |

### Top 3 intraday ranges (range_pct)
| stock       |   range_pct |
|:------------|------------:|
| BITCOIN     |    4.0772   |
| GOLD        |    1.23298  |
| RUSSELL2000 |    0.711727 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |         Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|---------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2025-12-29 | 23414.7   | 23531     | 23397.5   | 23474.3   |    6.52753e+09 |  0.25484  |    0.570155 |          1.00255  |            1 |
| S&P500           | 2025-12-29 |  6903.6   |  6920.21  |  6888.76  |  6905.74  |    3.54175e+09 |  0.031    |    0.455562 |          1.00031  |            1 |
| DOWJONES         | 2025-12-29 | 48636.6   | 48704.8   | 48390.9   | 48461.9   |    3.2185e+08  | -0.359193 |    0.645435 |          0.996408 |           -1 |
| RUSSELL2000      | 2025-12-29 |  2524.84  |  2533.65  |  2515.68  |  2519.8   |    3.54175e+09 | -0.199618 |    0.711727 |          0.998004 |           -1 |
| USD/KRW          | 2025-12-29 |  1433.9   |  1437.7   |  1429.64  |  1441.33  |    0           |  0.518162 |    0.562099 |          1.00518  |            1 |
| Dallor Index/USD | 2025-12-29 |    98.05  |    98.18  |    97.92  |    98.04  |    0           | -0.010201 |    0.265173 |          0.999898 |           -1 |
| GOLD             | 2025-12-29 |  4371.5   |  4379     |  4325.1   |  4325.1   | 2044           | -1.06142  |    1.23298  |          0.989386 |           -1 |
| BITCOIN          | 2025-12-29 | 87835.8   | 90299.2   | 86717.9   | 87138.1   |    4.84116e+10 | -0.794264 |    4.0772   |          0.992057 |           -1 |
| US5YT            | 2025-12-29 |     3.68  |     3.689 |     3.668 |     3.677 |    0           | -0.081522 |    0.57065  |          0.999185 |           -1 |
| US10YT           | 2025-12-29 |     4.116 |     4.13  |     4.108 |     4.116 |    0           |  0        |    0.534507 |          1        |            0 |
| US30YT           | 2025-12-29 |     4.799 |     4.815 |     4.794 |     4.805 |    0           |  0.125027 |    0.437589 |          1.00125  |            1 |
