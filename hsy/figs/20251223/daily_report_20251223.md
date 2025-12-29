# Daily Market Report (LLM-ready) — 2025-12-23

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
- Best performer: **US5YT** (0.864%)
- Worst performer: **BITCOIN** (-1.216%)
- Highest intraday range: **BITCOIN** (2.589%)
- Risk regime inference: **Risk-on (provisional)** (score=2.25)
  - Evidence:
    - Equity mean return: 0.290%
    - USD/KRW return: 0.000% (inverse tilt)
    - DXY return: -0.265% (inverse tilt)
    - Gold return: -0.455% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.434% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| US5YT   |  0.864399 |
| NASDAQ  |  0.658504 |
| S&P500  |  0.543912 |

### Bottom 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| BITCOIN     | -1.21599  |
| GOLD        | -0.455222 |
| RUSSELL2000 | -0.295051 |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| BITCOIN |     2.58945 |
| US5YT   |     1.78282 |
| US10YT  |     1.22862 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |        Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|--------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2025-12-23 | 23407.7   | 23563.5   | 23377.5   | 23561.8   |   7.51819e+09 |  0.658504 |    0.794485 |          1.00659  |            1 |
| S&P500           | 2025-12-23 |  6872.41  |  6910.88  |  6868.81  |  6909.79  |   3.82056e+09 |  0.543912 |    0.612155 |          1.00544  |            1 |
| DOWJONES         | 2025-12-23 | 48320.6   | 48527.5   | 48254.3   | 48442.4   |   4.1892e+08  |  0.252108 |    0.565373 |          1.00252  |            1 |
| RUSSELL2000      | 2025-12-23 |  2548.64  |  2553.2   |  2537.94  |  2541.12  |   3.82056e+09 | -0.295051 |    0.598751 |          0.997049 |           -1 |
| USD/KRW          | 2025-12-23 |  1476.84  |  1484.43  |  1476.84  |  1476.84  |   0           |  0        |    0.513941 |          1        |            0 |
| Dallor Index/USD | 2025-12-23 |    98.2   |    98.2   |    97.85  |    97.94  |   0           | -0.26476  |    0.356414 |          0.997352 |           -1 |
| GOLD             | 2025-12-23 |  4503.3   |  4503.8   |  4450.4   |  4482.8   | 694           | -0.455222 |    1.18579  |          0.995448 |           -1 |
| BITCOIN          | 2025-12-23 | 88490     | 88898.4   | 86607     | 87414     |   4.3683e+10  | -1.21599  |    2.58945  |          0.98784  |           -1 |
| US5YT            | 2025-12-23 |     3.702 |     3.766 |     3.7   |     3.734 |   0           |  0.864399 |    1.78282  |          1.00864  |            1 |
| US10YT           | 2025-12-23 |     4.151 |     4.202 |     4.151 |     4.169 |   0           |  0.433633 |    1.22862  |          1.00434  |            1 |
| US30YT           | 2025-12-23 |     4.826 |     4.864 |     4.824 |     4.831 |   0           |  0.103598 |    0.828843 |          1.00104  |            1 |
