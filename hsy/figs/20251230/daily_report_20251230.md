# Daily Market Report (LLM-ready) — 2025-12-30

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
- Best performer: **BITCOIN** (1.487%)
- Worst performer: **RUSSELL2000** (-0.766%)
- Highest intraday range: **BITCOIN** (2.941%)
- Risk regime inference: **Risk-off (provisional)** (score=-2.75)
  - Evidence:
    - Equity mean return: -0.291%
    - USD/KRW return: 0.294% (inverse tilt)
    - DXY return: 0.235% (inverse tilt)
    - Gold return: 0.545% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.266% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| BITCOIN |  1.48711  |
| GOLD    |  0.545283 |
| USD/KRW |  0.293598 |

### Bottom 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| RUSSELL2000 | -0.766293 |
| US5YT       | -0.378793 |
| US30YT      | -0.269374 |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| BITCOIN |     2.94074 |
| GOLD    |     1.5093  |
| USD/KRW |     1.37574 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |         Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|---------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2025-12-30 | 23465.7   | 23521.1   | 23414.8   | 23419.1   |    6.7693e+09  | -0.198545 |    0.452664 |          0.998015 |           -1 |
| S&P500           | 2025-12-30 |  6900.44  |  6913.25  |  6893.47  |  6896.24  |    3.30993e+09 | -0.060861 |    0.286645 |          0.999391 |           -1 |
| DOWJONES         | 2025-12-30 | 48434.9   | 48471.7   | 48297.3   | 48367.1   |    2.8257e+08  | -0.140024 |    0.360149 |          0.9986   |           -1 |
| RUSSELL2000      | 2025-12-30 |  2519.9   |  2520.91  |  2500.49  |  2500.59  |    3.30993e+09 | -0.766293 |    0.810347 |          0.992337 |           -1 |
| USD/KRW          | 2025-12-30 |  1430.51  |  1448.63  |  1428.95  |  1434.71  |    0           |  0.293598 |    1.37574  |          1.00294  |            1 |
| Dallor Index/USD | 2025-12-30 |    98.01  |    98.27  |    97.94  |    98.24  |    0           |  0.234666 |    0.336694 |          1.00235  |            1 |
| GOLD             | 2025-12-30 |  4346.4   |  4403.6   |  4338     |  4370.1   | 1837           |  0.545283 |    1.5093   |          1.00545  |            1 |
| BITCOIN          | 2025-12-30 | 87134.4   | 89297.9   | 86735.5   | 88430.1   |    3.55864e+10 |  1.48711  |    2.94074  |          1.01487  |            1 |
| US5YT            | 2025-12-30 |     3.696 |     3.696 |     3.668 |     3.682 |    0           | -0.378793 |    0.757579 |          0.996212 |           -1 |
| US10YT           | 2025-12-30 |     4.141 |     4.141 |     4.116 |     4.13  |    0           | -0.265629 |    0.60371  |          0.997344 |           -1 |
| US30YT           | 2025-12-30 |     4.826 |     4.826 |     4.799 |     4.813 |    0           | -0.269374 |    0.559478 |          0.997306 |           -1 |
