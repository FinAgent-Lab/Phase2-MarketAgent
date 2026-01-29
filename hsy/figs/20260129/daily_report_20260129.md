# Daily Market Report (LLM-ready) — 2026-01-29

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
- Best performer: **DOWJONES** (0.272%)
- Worst performer: **BITCOIN** (-5.300%)
- Highest intraday range: **GOLD** (9.189%)
- Risk regime inference: **Risk-off (provisional)** (score=-2.25)
  - Evidence:
    - Equity mean return: -0.171%
    - USD/KRW return: 0.092% (inverse tilt)
    - DXY return: 0.003% (inverse tilt)
    - Gold return: -0.677% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.471% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| DOWJONES         |  0.272362 |
| USD/KRW          |  0.092286 |
| Dallor Index/USD |  0.003118 |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| BITCOIN | -5.29958  |
| GOLD    | -0.677075 |
| NASDAQ  | -0.611805 |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| GOLD    |     9.18916 |
| BITCOIN |     6.53731 |
| NASDAQ  |     2.55035 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-29 | 23830.9   | 23840.5   | 23232.8   | 23685.1   |      7.17853e+09 | -0.611805 |    2.55035  |          0.993882 |           -1 |
| S&P500           | 2026-01-29 |  6977.74  |  6992.84  |  6870.8   |  6969.01  |      4.11606e+09 | -0.125119 |    1.74899  |          0.998749 |           -1 |
| DOWJONES         | 2026-01-29 | 48938.3   | 49292.8   | 48597.2   | 49071.6   |      6.93044e+08 |  0.272362 |    1.42136  |          1.00272  |            1 |
| RUSSELL2000      | 2026-01-29 |  2660.61  |  2665.06  |  2616.14  |  2654.78  |      0           | -0.219172 |    1.83859  |          0.997808 |           -1 |
| USD/KRW          | 2026-01-29 |  1430.28  |  1438.57  |  1423.48  |  1431.6   |      0           |  0.092286 |    1.05504  |          1.00092  |            1 |
| Dallor Index/USD | 2026-01-29 |    96.16  |    96.656 |    96.016 |    96.163 |      0           |  0.003118 |    0.665557 |          1.00003  |            1 |
| GOLD             | 2026-01-29 |  5449.9   |  5626.8   |  5126     |  5413     | 555429           | -0.677075 |    9.18916  |          0.993229 |           -1 |
| BITCOIN          | 2026-01-29 | 89163.5   | 89163.5   | 83334.6   | 84438.2   |      6.28637e+10 | -5.29958  |    6.53731  |          0.947004 |           -1 |
| US5YT            | 2026-01-29 |     3.826 |     3.844 |     3.798 |     3.805 |      0           | -0.548874 |    1.2023   |          0.994511 |           -1 |
| US10YT           | 2026-01-29 |     4.247 |     4.271 |     4.223 |     4.227 |      0           | -0.47092  |    1.13021  |          0.995291 |           -1 |
| US30YT           | 2026-01-29 |     4.872 |     4.895 |     4.848 |     4.854 |      0           | -0.369461 |    0.964695 |          0.996305 |           -1 |
