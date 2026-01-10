# Daily Market Report (LLM-ready) — 2026-01-07

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
- Best performer: **US5YT** (0.271%)
- Worst performer: **BITCOIN** (-2.861%)
- Highest intraday range: **BITCOIN** (3.194%)
- Risk regime inference: **Risk-off (provisional)** (score=-2.25)
  - Evidence:
    - Equity mean return: -0.405%
    - USD/KRW return: 0.239% (inverse tilt)
    - DXY return: 0.168% (inverse tilt)
    - Gold return: -0.934% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.145% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| US5YT            |  0.271437 |
| USD/KRW          |  0.239291 |
| Dallor Index/USD |  0.168393 |

### Bottom 3 daily returns (ret_pct)
| stock    |   ret_pct |
|:---------|----------:|
| BITCOIN  | -2.86078  |
| DOWJONES | -1.04345  |
| GOLD     | -0.934436 |

### Top 3 intraday ranges (range_pct)
| stock    |   range_pct |
|:---------|------------:|
| BITCOIN  |     3.19415 |
| GOLD     |     1.76455 |
| DOWJONES |     1.35206 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-07 | 23544.9   | 23723.4   | 23504.2   | 23584.3   |      7.3353e+09  |  0.167259 |    0.930777 |          1.00167  |            1 |
| S&P500           | 2026-01-07 |  6945.07  |  6965.69  |  6919.19  |  6920.93  |      3.21229e+09 | -0.34758  |    0.66954  |          0.996524 |           -1 |
| DOWJONES         | 2026-01-07 | 49512.7   | 49621.4   | 48952     | 48996.1   |      5.06187e+08 | -1.04345  |    1.35206  |          0.989565 |           -1 |
| RUSSELL2000      | 2026-01-07 |  2585.62  |  2585.62  |  2563.4   |  2575.42  |      0           | -0.394261 |    0.85949  |          0.996057 |           -1 |
| USD/KRW          | 2026-01-07 |  1445.97  |  1450.41  |  1445.41  |  1449.43  |      0           |  0.239291 |    0.345789 |          1.00239  |            1 |
| Dallor Index/USD | 2026-01-07 |    98.579 |    98.747 |    98.497 |    98.745 |      0           |  0.168393 |    0.253604 |          1.00168  |            1 |
| GOLD             | 2026-01-07 |  4505.4   |  4512.4   |  4432.9   |  4463.3   | 196608           | -0.934436 |    1.76455  |          0.990656 |           -1 |
| BITCOIN          | 2026-01-07 | 93707.1   | 93707.1   | 90714     | 91026.4   |      4.44679e+10 | -2.86078  |    3.19415  |          0.971392 |           -1 |
| US5YT            | 2026-01-07 |     3.684 |     3.713 |     3.675 |     3.694 |      0           |  0.271437 |    1.03149  |          1.00271  |            1 |
| US10YT           | 2026-01-07 |     4.132 |     4.161 |     4.124 |     4.138 |      0           |  0.145209 |    0.895454 |          1.00145  |            1 |
| US30YT           | 2026-01-07 |     4.817 |     4.844 |     4.807 |     4.815 |      0           | -0.041517 |    0.768107 |          0.999585 |           -1 |
