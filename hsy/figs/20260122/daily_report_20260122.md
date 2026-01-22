# Daily Market Report (LLM-ready) — 2026-01-22

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
- Best performer: **GOLD** (2.153%)
- Worst performer: **US30YT** (-0.534%)
- Highest intraday range: **GOLD** (3.466%)
- Risk regime inference: **Risk-on (provisional)** (score=2.25)
  - Evidence:
    - Equity mean return: 0.093%
    - USD/KRW return: -0.151% (inverse tilt)
    - DXY return: -0.507% (inverse tilt)
    - Gold return: 2.153% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.235% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock    |   ret_pct |
|:---------|----------:|
| GOLD     |  2.15251  |
| DOWJONES |  0.370318 |
| US5YT    |  0.13015  |

### Bottom 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| US30YT           | -0.533553 |
| Dallor Index/USD | -0.507151 |
| US10YT           | -0.234791 |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| GOLD    |    3.46552  |
| BITCOIN |    1.75663  |
| US30YT  |    0.902938 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-22 | 23440.7   | 23503.2   | 23335.1   | 23436     |      7.8559e+09  | -0.020014 |    0.716743 |          0.9998   |           -1 |
| S&P500           | 2026-01-22 |  6914.44  |  6934.75  |  6893.62  |  6913.35  |      3.30914e+09 | -0.015762 |    0.59484  |          0.999842 |           -1 |
| DOWJONES         | 2026-01-22 | 49201.8   | 49607.3   | 49201.8   | 49384     |      4.55133e+08 |  0.370318 |    0.824117 |          1.0037   |            1 |
| RUSSELL2000      | 2026-01-22 |  2717.8   |  2735.1   |  2714.99  |  2718.77  |      0           |  0.03569  |    0.74005  |          1.00036  |            1 |
| USD/KRW          | 2026-01-22 |  1466.22  |  1470.92  |  1462.33  |  1464.01  |      0           | -0.150725 |    0.585866 |          0.998493 |           -1 |
| Dallor Index/USD | 2026-01-22 |    98.787 |    98.827 |    98.281 |    98.286 |      0           | -0.507151 |    0.55271  |          0.994928 |           -1 |
| GOLD             | 2026-01-22 |  4836.2   |  4940.3   |  4772.7   |  4940.3   | 258021           |  2.15251  |    3.46552  |          1.02153  |            1 |
| BITCOIN          | 2026-01-22 | 89372.4   | 90202.3   | 88632.4   | 89266.8   |      3.70831e+10 | -0.118229 |    1.75663  |          0.998818 |           -1 |
| US5YT            | 2026-01-22 |     3.842 |     3.863 |     3.84  |     3.847 |      0           |  0.13015  |    0.598647 |          1.0013   |            1 |
| US10YT           | 2026-01-22 |     4.259 |     4.277 |     4.243 |     4.249 |      0           | -0.234791 |    0.798308 |          0.997652 |           -1 |
| US30YT           | 2026-01-22 |     4.873 |     4.886 |     4.842 |     4.847 |      0           | -0.533553 |    0.902938 |          0.994664 |           -1 |
