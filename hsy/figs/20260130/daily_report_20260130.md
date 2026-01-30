# Daily Market Report (LLM-ready) — 2026-01-30

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
- Best performer: **USD/KRW** (1.434%)
- Worst performer: **GOLD** (-9.787%)
- Highest intraday range: **GOLD** (14.414%)
- Risk regime inference: **Risk-off (provisional)** (score=-2.25)
  - Evidence:
    - Equity mean return: -0.395%
    - USD/KRW return: 1.434% (inverse tilt)
    - DXY return: 1.011% (inverse tilt)
    - Gold return: -9.787% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.141% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| USD/KRW          |  1.43384  |
| Dallor Index/USD |  1.01076  |
| S&P500           | -0.118611 |

### Bottom 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| GOLD        | -9.78743  |
| RUSSELL2000 | -0.761271 |
| BITCOIN     | -0.512988 |

### Top 3 intraday ranges (range_pct)
| stock       |   range_pct |
|:------------|------------:|
| GOLD        |    14.4141  |
| BITCOIN     |     3.88082 |
| RUSSELL2000 |     1.84886 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-30 | 23579     | 23662.2   | 23351.5   | 23461.8   |      7.83584e+09 | -0.496802 |    1.3177   |          0.995032 |           -1 |
| S&P500           | 2026-01-30 |  6947.27  |  6964.09  |  6893.48  |  6939.03  |      4.26159e+09 | -0.118611 |    1.01637  |          0.998814 |           -1 |
| DOWJONES         | 2026-01-30 | 48991.6   | 49047.7   | 48459.9   | 48892.5   |      7.61992e+08 | -0.202386 |    1.1998   |          0.997976 |           -1 |
| RUSSELL2000      | 2026-01-30 |  2633.79  |  2648.27  |  2599.57  |  2613.74  |      0           | -0.761271 |    1.84886  |          0.992387 |           -1 |
| USD/KRW          | 2026-01-30 |  1429.73  |  1451.35  |  1429.73  |  1450.23  |      0           |  1.43384  |    1.51217  |          1.01434  |            1 |
| Dallor Index/USD | 2026-01-30 |    96.165 |    97.149 |    96.32  |    97.137 |      0           |  1.01076  |    0.862062 |          1.01011  |            1 |
| GOLD             | 2026-01-30 |  5410     |  5480.2   |  4700.4   |  4880.5   | 491832           | -9.78743  |   14.4141   |          0.902126 |           -1 |
| BITCOIN          | 2026-01-30 | 84553.7   | 84592.6   | 81311.2   | 84119.9   |      7.32814e+10 | -0.512988 |    3.88082  |          0.99487  |           -1 |
| US5YT            | 2026-01-30 |     3.811 |     3.828 |     3.793 |     3.797 |      0           | -0.367356 |    0.91839  |          0.996326 |           -1 |
| US10YT           | 2026-01-30 |     4.247 |     4.261 |     4.236 |     4.241 |      0           | -0.141277 |    0.588653 |          0.998587 |           -1 |
| US30YT           | 2026-01-30 |     4.881 |     4.893 |     4.864 |     4.872 |      0           | -0.184385 |    0.594146 |          0.998156 |           -1 |
