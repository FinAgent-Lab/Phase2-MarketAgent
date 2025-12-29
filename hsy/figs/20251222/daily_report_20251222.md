# Daily Market Report (LLM-ready) — 2025-12-22

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
- Best performer: **GOLD** (1.681%)
- Worst performer: **Dallor Index/USD** (-0.385%)
- Highest intraday range: **BITCOIN** (2.927%)
- Risk regime inference: **Risk-on (provisional)** (score=1.75)
  - Evidence:
    - Equity mean return: 0.300%
    - USD/KRW return: 0.000% (inverse tilt)
    - DXY return: -0.385% (inverse tilt)
    - Gold return: 1.681% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.048% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| GOLD        |  1.6815   |
| RUSSELL2000 |  0.786985 |
| DOWJONES    |  0.312788 |

### Bottom 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| Dallor Index/USD | -0.385119 |
| BITCOIN          | -0.148252 |
| NASDAQ           | -0.092532 |

### Top 3 intraday ranges (range_pct)
| stock       |   range_pct |
|:------------|------------:|
| BITCOIN     |     2.9269  |
| GOLD        |     1.75013 |
| RUSSELL2000 |     1.34315 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |        Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|--------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2025-12-22 | 23450.5   | 23476.5   | 23362.9   | 23428.8   |   7.24491e+09 | -0.092532 |    0.484297 |          0.999075 |           -1 |
| S&P500           | 2025-12-22 |  6865.21  |  6882.03  |  6855.74  |  6878.49  |   4.46503e+09 |  0.193443 |    0.382939 |          1.00193  |            1 |
| DOWJONES         | 2025-12-22 | 48211.9   | 48457.5   | 48199.1   | 48362.7   |   4.2705e+08  |  0.312788 |    0.535843 |          1.00313  |            1 |
| RUSSELL2000      | 2025-12-22 |  2538.8   |  2572.9   |  2538.8   |  2558.78  |   4.46503e+09 |  0.786985 |    1.34315  |          1.00787  |            1 |
| USD/KRW          | 2025-12-22 |  1473.72  |  1481.67  |  1473.72  |  1473.72  |   0           |  0        |    0.539456 |          1        |            0 |
| Dallor Index/USD | 2025-12-22 |    98.67  |    98.73  |    98.2   |    98.29  |   0           | -0.385119 |    0.537151 |          0.996149 |           -1 |
| GOLD             | 2025-12-22 |  4371.1   |  4447.6   |  4371.1   |  4444.6   | 449           |  1.6815   |    1.75013  |          1.01682  |            1 |
| BITCOIN          | 2025-12-22 | 88621.4   | 90501.9   | 87908.1   | 88490     |   3.80475e+10 | -0.148252 |    2.9269   |          0.998517 |           -1 |
| US5YT            | 2025-12-22 |     3.711 |     3.723 |     3.702 |     3.718 |   0           |  0.188628 |    0.565889 |          1.00189  |            1 |
| US10YT           | 2025-12-22 |     4.167 |     4.175 |     4.155 |     4.169 |   0           |  0.048004 |    0.479961 |          1.00048  |            1 |
| US30YT           | 2025-12-22 |     4.843 |     4.846 |     4.829 |     4.842 |   0           | -0.020647 |    0.351026 |          0.999794 |           -1 |
