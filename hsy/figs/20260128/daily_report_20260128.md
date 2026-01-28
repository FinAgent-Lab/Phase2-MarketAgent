# Daily Market Report (LLM-ready) — 2026-01-28

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
- Best performer: **GOLD** (4.582%)
- Worst performer: **RUSSELL2000** (-1.024%)
- Highest intraday range: **GOLD** (4.559%)
- Risk regime inference: **Risk-off (provisional)** (score=-1.75)
  - Evidence:
    - Equity mean return: -0.459%
    - USD/KRW return: -0.261% (inverse tilt)
    - DXY return: 0.422% (inverse tilt)
    - Gold return: 4.582% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.378% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| GOLD             |  4.58196  |
| US5YT            |  0.549592 |
| Dallor Index/USD |  0.422036 |

### Bottom 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| RUSSELL2000 | -1.02432  |
| NASDAQ      | -0.449237 |
| S&P500      | -0.342334 |

### Top 3 intraday ranges (range_pct)
| stock       |   range_pct |
|:------------|------------:|
| GOLD        |     4.5588  |
| BITCOIN     |     1.79139 |
| RUSSELL2000 |     1.42588 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-28 | 23965.1   | 23988.3   | 23775.5   | 23857.4   |      7.06415e+09 | -0.449237 |    0.887863 |          0.995508 |           -1 |
| S&P500           | 2026-01-28 |  7002     |  7002.28  |  6963.46  |  6978.03  |      3.33782e+09 | -0.342334 |    0.554411 |          0.996577 |           -1 |
| DOWJONES         | 2026-01-28 | 49024.7   | 49150.3   | 48901.5   | 49015.6   |      4.70999e+08 | -0.018517 |    0.507605 |          0.999815 |           -1 |
| RUSSELL2000      | 2026-01-28 |  2681.01  |  2685.86  |  2647.63  |  2653.55  |      0           | -1.02432  |    1.42588  |          0.989757 |           -1 |
| USD/KRW          | 2026-01-28 |  1434.04  |  1437.6   |  1419.78  |  1430.29  |      0           | -0.261499 |    1.24264  |          0.997385 |           -1 |
| Dallor Index/USD | 2026-01-28 |    95.965 |    96.787 |    95.859 |    96.37  |      0           |  0.422036 |    0.967021 |          1.00422  |            1 |
| GOLD             | 2026-01-28 |  5179     |  5429.7   |  5193.6   |  5416.3   | 401556           |  4.58196  |    4.5588   |          1.04582  |            1 |
| BITCOIN          | 2026-01-28 | 89129.9   | 90340     | 88743.3   | 89265.6   |      4.11662e+10 |  0.152271 |    1.79139  |          1.00152  |            1 |
| US5YT            | 2026-01-28 |     3.821 |     3.873 |     3.821 |     3.842 |      0           |  0.549592 |    1.3609   |          1.0055   |            1 |
| US10YT           | 2026-01-28 |     4.235 |     4.271 |     4.235 |     4.251 |      0           |  0.37781  |    0.850065 |          1.00378  |            1 |
| US30YT           | 2026-01-28 |     4.855 |     4.894 |     4.85  |     4.86  |      0           |  0.102979 |    0.906285 |          1.00103  |            1 |
