# Daily Market Report (LLM-ready) — 2026-01-16

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
- Best performer: **US5YT** (1.083%)
- Worst performer: **NASDAQ** (-0.526%)
- Highest intraday range: **GOLD** (1.869%)
- Risk regime inference: **Risk-off (provisional)** (score=-2.25)
  - Evidence:
    - Equity mean return: -0.251%
    - USD/KRW return: 0.248% (inverse tilt)
    - DXY return: 0.006% (inverse tilt)
    - Gold return: -0.502% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.858% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| US5YT   |  1.08265  |
| US10YT  |  0.858159 |
| US30YT  |  0.290104 |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| NASDAQ  | -0.525814 |
| GOLD    | -0.501995 |
| S&P500  | -0.294952 |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| GOLD    |     1.86948 |
| BITCOIN |     1.52654 |
| US5YT   |     1.34672 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-16 | 23639.7   | 23664.3   | 23446.8   | 23515.4   |      8.40886e+09 | -0.525814 |    0.919832 |          0.994742 |           -1 |
| S&P500           | 2026-01-16 |  6960.54  |  6967.3   |  6925.09  |  6940.01  |      3.99093e+09 | -0.294952 |    0.606418 |          0.99705  |           -1 |
| DOWJONES         | 2026-01-16 | 49466.7   | 49616.7   | 49246.2   | 49359.3   |      9.92978e+08 | -0.217057 |    0.74891  |          0.997829 |           -1 |
| RUSSELL2000      | 2026-01-16 |  2676.81  |  2692.23  |  2668.56  |  2677.74  |      0           |  0.034649 |    0.883948 |          1.00035  |            1 |
| USD/KRW          | 2026-01-16 |  1469.85  |  1475.53  |  1468.63  |  1473.5   |      0           |  0.248326 |    0.469437 |          1.00248  |            1 |
| Dallor Index/USD | 2026-01-16 |    99.369 |    99.483 |    99.163 |    99.375 |      0           |  0.006035 |    0.322032 |          1.00006  |            1 |
| GOLD             | 2026-01-16 |  4621.6   |  4625.5   |  4539.1   |  4598.4   | 242360           | -0.501995 |    1.86948  |          0.99498  |           -1 |
| BITCOIN          | 2026-01-16 | 95562.8   | 95773.6   | 94314.8   | 95495.3   |      3.38029e+10 | -0.070651 |    1.52654  |          0.999293 |           -1 |
| US5YT            | 2026-01-16 |     3.787 |     3.829 |     3.778 |     3.828 |      0           |  1.08265  |    1.34672  |          1.01083  |            1 |
| US10YT           | 2026-01-16 |     4.195 |     4.233 |     4.181 |     4.231 |      0           |  0.858159 |    1.23957  |          1.00858  |            1 |
| US30YT           | 2026-01-16 |     4.826 |     4.843 |     4.8   |     4.84  |      0           |  0.290104 |    0.891002 |          1.0029   |            1 |
