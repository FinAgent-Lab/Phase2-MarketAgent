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
- Best performer: **BITCOIN** (1.204%)
- Worst performer: **RUSSELL2000** (-0.766%)
- Highest intraday range: **BITCOIN** (2.710%)
- Risk regime inference: **Risk-off (provisional)** (score=-2.75)
  - Evidence:
    - Equity mean return: -0.291%
    - USD/KRW return: 0.151% (inverse tilt)
    - DXY return: 0.223% (inverse tilt)
    - Gold return: 0.262% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.266% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| BITCOIN          |  1.204    |
| GOLD             |  0.26206  |
| Dallor Index/USD |  0.223441 |

### Bottom 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| RUSSELL2000 | -0.766332 |
| US5YT       | -0.378786 |
| US30YT      | -0.269365 |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| BITCOIN |     2.70954 |
| GOLD    |     1.87804 |
| USD/KRW |     1.41535 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2025-12-30 | 23465.7   | 23521.1   | 23414.8   | 23419.1   |      6.03047e+09 | -0.198536 |    0.452656 |          0.998015 |           -1 |
| S&P500           | 2025-12-30 |  6900.44  |  6913.25  |  6893.47  |  6896.24  |      1.70596e+09 | -0.060861 |    0.286645 |          0.999391 |           -1 |
| DOWJONES         | 2025-12-30 | 48434.9   | 48471.7   | 48297.3   | 48367.1   |      2.82575e+08 | -0.140024 |    0.360149 |          0.9986   |           -1 |
| RUSSELL2000      | 2025-12-30 |  2519.9   |  2520.91  |  2500.49  |  2500.59  |      0           | -0.766332 |    0.810289 |          0.992337 |           -1 |
| USD/KRW          | 2025-12-30 |  1435.68  |  1450.1   |  1429.78  |  1437.85  |      0           |  0.151142 |    1.41535  |          1.00151  |            1 |
| Dallor Index/USD | 2025-12-30 |    98.01  |    98.269 |    97.939 |    98.229 |      0           |  0.223441 |    0.336694 |          1.00223  |            1 |
| GOLD             | 2025-12-30 |  4350.3   |  4420.5   |  4338.8   |  4361.7   | 182343           |  0.26206  |    1.87804  |          1.00262  |            1 |
| BITCOIN          | 2025-12-30 | 87132.9   | 89191.4   | 86830.5   | 88182     |      3.5521e+10  |  1.204    |    2.70954  |          1.01204  |            1 |
| US5YT            | 2025-12-30 |     3.696 |     3.696 |     3.668 |     3.682 |      0           | -0.378786 |    0.757572 |          0.996212 |           -1 |
| US10YT           | 2025-12-30 |     4.141 |     4.141 |     4.116 |     4.13  |      0           | -0.265629 |    0.60371  |          0.997344 |           -1 |
| US30YT           | 2025-12-30 |     4.826 |     4.826 |     4.799 |     4.813 |      0           | -0.269365 |    0.559459 |          0.997306 |           -1 |
