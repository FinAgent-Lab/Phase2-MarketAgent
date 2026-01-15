# Daily Market Report (LLM-ready) — 2026-01-15

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
- Best performer: **US5YT** (0.966%)
- Worst performer: **BITCOIN** (-1.501%)
- Highest intraday range: **BITCOIN** (2.048%)
- Risk regime inference: **Risk-off (provisional)** (score=-2.25)
  - Evidence:
    - Equity mean return: -0.014%
    - USD/KRW return: 0.406% (inverse tilt)
    - DXY return: 0.223% (inverse tilt)
    - Gold return: -0.362% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.532% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| US5YT       |  0.966184 |
| US10YT      |  0.531654 |
| RUSSELL2000 |  0.505418 |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| BITCOIN | -1.501    |
| NASDAQ  | -0.691937 |
| GOLD    | -0.362411 |

### Top 3 intraday ranges (range_pct)
| stock       |   range_pct |
|:------------|------------:|
| BITCOIN     |     2.04764 |
| GOLD        |     1.14762 |
| RUSSELL2000 |     1.12695 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-15 | 23694     | 23721.1   | 23502.2   | 23530     |      8.52419e+09 | -0.691937 |    0.923997 |          0.993081 |           -1 |
| S&P500           | 2026-01-15 |  6969.46  |  6979.34  |  6937.93  |  6944.47  |      3.12748e+09 | -0.358561 |    0.594159 |          0.996414 |           -1 |
| DOWJONES         | 2026-01-15 | 49201.1   | 49581.2   | 49201.1   | 49442.4   |      5.41528e+08 |  0.490517 |    0.772499 |          1.0049   |            1 |
| RUSSELL2000      | 2026-01-15 |  2661.11  |  2689.28  |  2659.29  |  2674.56  |      0           |  0.505418 |    1.12695  |          1.00505  |            1 |
| USD/KRW          | 2026-01-15 |  1463.91  |  1474.17  |  1463.78  |  1469.86  |      0           |  0.406442 |    0.709744 |          1.00406  |            1 |
| Dallor Index/USD | 2026-01-15 |    99.129 |    99.492 |    99.086 |    99.35  |      0           |  0.222943 |    0.409566 |          1.00223  |            1 |
| GOLD             | 2026-01-15 |  4635.7   |  4637.2   |  4584     |  4618.9   | 222402           | -0.362411 |    1.14762  |          0.996376 |           -1 |
| BITCOIN          | 2026-01-15 | 96934.6   | 97097.1   | 95112.2   | 95479.6   |      5.50932e+10 | -1.501    |    2.04764  |          0.98499  |           -1 |
| US5YT            | 2026-01-15 |     3.726 |     3.764 |     3.724 |     3.762 |      0           |  0.966184 |    1.07353  |          1.00966  |            1 |
| US10YT           | 2026-01-15 |     4.138 |     4.164 |     4.136 |     4.16  |      0           |  0.531654 |    0.676652 |          1.00532  |            1 |
| US30YT           | 2026-01-15 |     4.781 |     4.8   |     4.772 |     4.787 |      0           |  0.125488 |    0.585649 |          1.00126  |            1 |
