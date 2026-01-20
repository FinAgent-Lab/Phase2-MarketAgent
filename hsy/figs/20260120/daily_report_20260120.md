# Daily Market Report (LLM-ready) — 2026-01-20

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
- Best performer: **GOLD** (2.793%)
- Worst performer: **BITCOIN** (-3.446%)
- Highest intraday range: **BITCOIN** (3.877%)
- Risk regime inference: **Risk-off (provisional)** (score=-1.75)
  - Evidence:
    - Equity mean return: -0.635%
    - USD/KRW return: 0.561% (inverse tilt)
    - DXY return: -0.571% (inverse tilt)
    - Gold return: 2.793% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.374% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| GOLD    |  2.79258  |
| USD/KRW |  0.56097  |
| US5YT   |  0.416463 |

### Bottom 3 daily returns (ret_pct)
| stock    |   ret_pct |
|:---------|----------:|
| BITCOIN  | -3.44587  |
| DOWJONES | -1.05381  |
| S&P500   | -0.996038 |

### Top 3 intraday ranges (range_pct)
| stock       |   range_pct |
|:------------|------------:|
| BITCOIN     |     3.8766  |
| GOLD        |     3.22204 |
| RUSSELL2000 |     1.43985 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-20 | 23142.7   | 23236.1   | 22916.8   | 22954.3   |      8.0271e+09  | -0.813921 |    1.37936  |          0.991861 |           -1 |
| S&P500           | 2026-01-20 |  6865.24  |  6871.17  |  6789.05  |  6796.86  |      3.89198e+09 | -0.996038 |    1.19617  |          0.99004  |           -1 |
| DOWJONES         | 2026-01-20 | 49005     | 49005     | 48428.1   | 48488.6   |      6.76039e+08 | -1.05381  |    1.17719  |          0.989462 |           -1 |
| RUSSELL2000      | 2026-01-20 |  2636.84  |  2670.32  |  2632.35  |  2645.36  |      0           |  0.323096 |    1.43985  |          1.00323  |            1 |
| USD/KRW          | 2026-01-20 |  1472.45  |  1481.02  |  1472.45  |  1480.71  |      0           |  0.56097  |    0.582028 |          1.00561  |            1 |
| Dallor Index/USD | 2026-01-20 |    99.138 |    99.139 |    98.246 |    98.572 |      0           | -0.570923 |    0.900762 |          0.994291 |           -1 |
| GOLD             | 2026-01-20 |  4633.7   |  4771.5   |  4622.2   |  4763.1   | 405542           |  2.79258  |    3.22204  |          1.02793  |            1 |
| BITCOIN          | 2026-01-20 | 92583.6   | 92797.2   | 89208.1   | 89393.3   |      5.07679e+10 | -3.44587  |    3.8766   |          0.965541 |           -1 |
| US5YT            | 2026-01-20 |     3.842 |     3.872 |     3.833 |     3.858 |      0           |  0.416463 |    1.0151   |          1.00416  |            1 |
| US10YT           | 2026-01-20 |     4.279 |     4.311 |     4.269 |     4.295 |      0           |  0.373914 |    0.981533 |          1.00374  |            1 |
| US30YT           | 2026-01-20 |     4.914 |     4.947 |     4.892 |     4.92  |      0           |  0.122101 |    1.11926  |          1.00122  |            1 |
