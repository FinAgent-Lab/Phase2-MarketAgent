# Daily Market Report (LLM-ready) — 2025-12-31

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
- Best performer: **US5YT** (1.224%)
- Worst performer: **BITCOIN** (-1.041%)
- Highest intraday range: **BITCOIN** (2.205%)
- Risk regime inference: **Risk-off (provisional)** (score=-1.25)
  - Evidence:
    - Equity mean return: -0.728%
    - USD/KRW return: -0.114% (inverse tilt)
    - DXY return: 0.031% (inverse tilt)
    - Gold return: -0.182% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.897% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| US5YT   |  1.22382  |
| US10YT  |  0.896757 |
| US30YT  |  0.56098  |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| BITCOIN | -1.04123  |
| S&P500  | -0.772883 |
| NASDAQ  | -0.763676 |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| BITCOIN |     2.20484 |
| GOLD    |     1.81839 |
| US5YT   |     1.49579 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |        Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|--------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2025-12-31 | 23420.8   | 23445.3   | 23237.8   | 23242     |   5.89513e+09 | -0.763676 |    0.885879 |          0.992363 |           -1 |
| S&P500           | 2025-12-31 |  6898.82  |  6901.42  |  6844.55  |  6845.5   |   3.26183e+09 | -0.772883 |    0.824346 |          0.992271 |           -1 |
| DOWJONES         | 2025-12-31 | 48371.5   | 48394.5   | 48050.9   | 48063.3   |   3.3606e+08  | -0.637215 |    0.710403 |          0.993628 |           -1 |
| RUSSELL2000      | 2025-12-31 |  2500.37  |  2501.77  |  2480.68  |  2481.91  |   3.26183e+09 | -0.738299 |    0.843479 |          0.992617 |           -1 |
| USD/KRW          | 2025-12-31 |  1439.55  |  1449.2   |  1437.37  |  1437.91  |   0           | -0.113926 |    0.821782 |          0.998861 |           -1 |
| Dallor Index/USD | 2025-12-31 |    98.25  |    98.5   |    98.18  |    98.28  |   0           |  0.030533 |    0.325699 |          1.0003   |            1 |
| GOLD             | 2025-12-31 |  4333.5   |  4363.8   |  4285     |  4325.6   | 785           | -0.182298 |    1.81839  |          0.998177 |           -1 |
| BITCOIN          | 2025-12-31 | 88429.6   | 89080.3   | 87130.6   | 87508.8   |   3.38302e+10 | -1.04123  |    2.20484  |          0.989588 |           -1 |
| US5YT            | 2025-12-31 |     3.677 |     3.73  |     3.675 |     3.722 |   0           |  1.22382  |    1.49579  |          1.01224  |            1 |
| US10YT           | 2025-12-31 |     4.126 |     4.173 |     4.126 |     4.163 |   0           |  0.896757 |    1.13912  |          1.00897  |            1 |
| US30YT           | 2025-12-31 |     4.813 |     4.851 |     4.81  |     4.84  |   0           |  0.56098  |    0.851857 |          1.00561  |            1 |
