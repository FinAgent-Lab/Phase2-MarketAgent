# Daily Market Report (LLM-ready) — 2025-12-16

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
- Best performer: **BITCOIN** (1.643%)
- Worst performer: **US5YT** (-0.806%)
- Highest intraday range: **BITCOIN** (3.226%)
- Risk regime inference: **Risk-off (provisional)** (score=-1.25)
  - Evidence:
    - Equity mean return: -0.067%
    - USD/KRW return: 0.000% (inverse tilt)
    - DXY return: -0.122% (inverse tilt)
    - Gold return: 0.796% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.504% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| BITCOIN |  1.64257  |
| GOLD    |  0.79616  |
| NASDAQ  |  0.564101 |

### Bottom 3 daily returns (ret_pct)
| stock    |   ret_pct |
|:---------|----------:|
| US5YT    | -0.805801 |
| DOWJONES | -0.549626 |
| US10YT   | -0.503595 |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| BITCOIN |     3.22641 |
| US5YT   |     1.53102 |
| US10YT  |     1.27098 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |         Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|---------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2025-12-16 | 22981.8   | 23162.6   | 22920.7   | 23111.5   |    7.75996e+09 |  0.564101 |    1.05274  |          1.00564  |            1 |
| S&P500           | 2025-12-16 |  6800.12  |  6819.27  |  6759.74  |  6800.26  |    4.98318e+09 |  0.002054 |    0.875423 |          1.00002  |            1 |
| DOWJONES         | 2025-12-16 | 48380.2   | 48452.2   | 47946.2   | 48114.3   |    4.574e+08   | -0.549626 |    1.04572  |          0.994504 |           -1 |
| RUSSELL2000      | 2025-12-16 |  2526.5   |  2536.62  |  2506.55  |  2519.3   |    4.98318e+09 | -0.284977 |    1.19019  |          0.99715  |           -1 |
| USD/KRW          | 2025-12-16 |  1467.48  |  1477.04  |  1467.25  |  1467.48  |    0           |  0        |    0.667133 |          1        |            0 |
| Dallor Index/USD | 2025-12-16 |    98.27  |    98.32  |    97.87  |    98.15  |    0           | -0.122108 |    0.457919 |          0.998779 |           -1 |
| GOLD             | 2025-12-16 |  4270.5   |  4321.4   |  4270.5   |  4304.5   | 1796           |  0.79616  |    1.1919   |          1.00796  |            1 |
| BITCOIN          | 2025-12-16 | 86424.4   | 88170.1   | 85381.7   | 87844     |    4.12622e+10 |  1.64257  |    3.22641  |          1.01643  |            1 |
| US5YT            | 2025-12-16 |     3.723 |     3.738 |     3.681 |     3.693 |    0           | -0.805801 |    1.53102  |          0.991942 |           -1 |
| US10YT           | 2025-12-16 |     4.17  |     4.196 |     4.143 |     4.149 |    0           | -0.503595 |    1.27098  |          0.994964 |           -1 |
| US30YT           | 2025-12-16 |     4.836 |     4.871 |     4.821 |     4.824 |    0           | -0.248141 |    1.03391  |          0.997519 |           -1 |
