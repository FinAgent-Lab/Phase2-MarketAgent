# Daily Market Report (LLM-ready) — 2026-01-08

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
- Best performer: **RUSSELL2000** (1.414%)
- Worst performer: **NASDAQ** (-0.292%)
- Highest intraday range: **BITCOIN** (2.296%)
- Risk regime inference: **Mixed / unclear (provisional)** (score=0.25)
  - Evidence:
    - Equity mean return: 0.520%
    - USD/KRW return: 0.371% (inverse tilt)
    - DXY return: 0.140% (inverse tilt)
    - Gold return: 0.358% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.384% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| RUSSELL2000 |  1.41355  |
| DOWJONES    |  0.851456 |
| US5YT       |  0.565273 |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| NASDAQ  | -0.292452 |
| BITCOIN | -0.094942 |
| S&P500  |  0.106306 |

### Top 3 intraday ranges (range_pct)
| stock       |   range_pct |
|:------------|------------:|
| BITCOIN     |     2.29578 |
| GOLD        |     1.66327 |
| RUSSELL2000 |     1.63244 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-08 | 23548.9   | 23558.2   | 23353.5   | 23480     |      6.62455e+09 | -0.292452 |    0.869285 |          0.997075 |           -1 |
| S&P500           | 2026-01-08 |  6914.11  |  6931.28  |  6899.33  |  6921.46  |      3.18487e+09 |  0.106306 |    0.462094 |          1.00106  |            1 |
| DOWJONES         | 2026-01-08 | 48850.2   | 49357.7   | 48792.3   | 49266.1   |      5.15076e+08 |  0.851456 |    1.15741  |          1.00852  |            1 |
| RUSSELL2000      | 2026-01-08 |  2567.61  |  2608.57  |  2566.66  |  2603.91  |      0           |  1.41355  |    1.63244  |          1.01414  |            1 |
| USD/KRW          | 2026-01-08 |  1447.15  |  1454.3   |  1447     |  1452.52  |      0           |  0.371074 |    0.504443 |          1.00371  |            1 |
| Dallor Index/USD | 2026-01-08 |    98.736 |    98.984 |    98.679 |    98.874 |      0           |  0.139767 |    0.308905 |          1.0014   |            1 |
| GOLD             | 2026-01-08 |  4467.1   |  4489.3   |  4415     |  4483.1   | 190823           |  0.358174 |    1.66327  |          1.00358  |            1 |
| BITCOIN          | 2026-01-08 | 91280.7   | 91440.6   | 89345     | 91194     |      4.36304e+10 | -0.094942 |    2.29578  |          0.999051 |           -1 |
| US5YT            | 2026-01-08 |     3.715 |     3.741 |     3.711 |     3.736 |      0           |  0.565273 |    0.807536 |          1.00565  |            1 |
| US10YT           | 2026-01-08 |     4.167 |     4.187 |     4.161 |     4.183 |      0           |  0.383976 |    0.623939 |          1.00384  |            1 |
| US30YT           | 2026-01-08 |     4.85  |     4.862 |     4.842 |     4.858 |      0           |  0.164956 |    0.412371 |          1.00165  |            1 |
