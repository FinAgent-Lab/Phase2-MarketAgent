# Daily Market Report (LLM-ready) — 2026-01-21

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
- Best performer: **BITCOIN** (2.020%)
- Worst performer: **US30YT** (-0.996%)
- Highest intraday range: **BITCOIN** (3.545%)
- Risk regime inference: **Risk-on (provisional)** (score=1.25)
  - Evidence:
    - Equity mean return: 1.075%
    - USD/KRW return: -0.958% (inverse tilt)
    - DXY return: 0.160% (inverse tilt)
    - Gold return: 1.487% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.654% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| BITCOIN     |   2.02002 |
| GOLD        |   1.48715 |
| RUSSELL2000 |   1.35413 |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| US30YT  | -0.99594  |
| USD/KRW | -0.957579 |
| US10YT  | -0.654061 |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| BITCOIN |     3.54507 |
| GOLD    |     2.8107  |
| NASDAQ  |     1.97832 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-21 | 23017.7   | 23383.2   | 22927.9   | 23224.8   |      7.5762e+09  |  0.899945 |    1.97832  |          1.009    |            1 |
| S&P500           | 2026-01-21 |  6810.71  |  6910.39  |  6804.96  |  6875.62  |      3.81506e+09 |  0.95306  |    1.54801  |          1.00953  |            1 |
| DOWJONES         | 2026-01-21 | 48546     | 49295     | 48546     | 49077.2   |      6.00848e+08 |  1.09422  |    1.54287  |          1.01094  |            1 |
| RUSSELL2000      | 2026-01-21 |  2662.12  |  2703.75  |  2651.47  |  2698.17  |      0           |  1.35413  |    1.96374  |          1.01354  |            1 |
| USD/KRW          | 2026-01-21 |  1478.72  |  1481.46  |  1463.68  |  1464.56  |      0           | -0.957579 |    1.20239  |          0.990424 |           -1 |
| Dallor Index/USD | 2026-01-21 |    98.605 |    98.868 |    98.384 |    98.763 |      0           |  0.160232 |    0.490841 |          1.0016   |            1 |
| GOLD             | 2026-01-21 |  4767.5   |  4891.1   |  4757.1   |  4838.4   | 388570           |  1.48715  |    2.8107   |          1.01487  |            1 |
| BITCOIN          | 2026-01-21 | 88321.3   | 90371.6   | 87240.6   | 90105.4   |      6.07105e+10 |  2.02002  |    3.54507  |          1.0202   |            1 |
| US5YT            | 2026-01-21 |     3.835 |     3.856 |     3.826 |     3.831 |      0           | -0.104295 |    0.78228  |          0.998957 |           -1 |
| US10YT           | 2026-01-21 |     4.281 |     4.301 |     4.249 |     4.253 |      0           | -0.654061 |    1.21466  |          0.993459 |           -1 |
| US30YT           | 2026-01-21 |     4.92  |     4.938 |     4.861 |     4.871 |      0           | -0.99594  |    1.56504  |          0.990041 |           -1 |
