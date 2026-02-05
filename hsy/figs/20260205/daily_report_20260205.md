# Daily Market Report (LLM-ready) — 2026-02-05

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
- Best performer: **USD/KRW** (0.719%)
- Worst performer: **BITCOIN** (-13.415%)
- Highest intraday range: **BITCOIN** (14.549%)
- Risk regime inference: **Risk-off (provisional)** (score=-2.25)
  - Evidence:
    - Equity mean return: -0.696%
    - USD/KRW return: 0.719% (inverse tilt)
    - DXY return: 0.310% (inverse tilt)
    - Gold return: -3.959% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.988% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| USD/KRW          |  0.719322 |
| Dallor Index/USD |  0.31022  |
| NASDAQ           | -0.280612 |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| BITCOIN | -13.415   |
| GOLD    |  -3.95861 |
| US5YT   |  -1.23782 |

### Top 3 intraday ranges (range_pct)
| stock       |   range_pct |
|:------------|------------:|
| BITCOIN     |    14.5488  |
| GOLD        |     5.30422 |
| RUSSELL2000 |     2.32483 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |    ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|-----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-02-05 | 22604     | 22841.3   | 22461.1   | 22540.6   |      8.13107e+09 |  -0.280612 |    1.68174  |          0.997194 |           -1 |
| S&P500           | 2026-02-05 |  6837.39  |  6857.85  |  6780.13  |  6798.4   |      4.33055e+09 |  -0.57025  |    1.13669  |          0.994297 |           -1 |
| DOWJONES         | 2026-02-05 | 49313     | 49340.9   | 48829.1   | 48908.7   |      7.1027e+08  |  -0.819905 |    1.03785  |          0.991801 |           -1 |
| RUSSELL2000      | 2026-02-05 |  2606.71  |  2629.83  |  2569.23  |  2577.65  |      0           |  -1.11486  |    2.32483  |          0.988851 |           -1 |
| USD/KRW          | 2026-02-05 |  1461.1   |  1471.81  |  1458.98  |  1471.61  |      0           |   0.719322 |    0.878111 |          1.00719  |            1 |
| Dallor Index/USD | 2026-02-05 |    97.673 |    97.986 |    97.607 |    97.976 |      0           |   0.31022  |    0.388027 |          1.0031   |            1 |
| GOLD             | 2026-02-05 |  4986.6   |  5045     |  4780.5   |  4789.2   | 227712           |  -3.95861  |    5.30422  |          0.960414 |           -1 |
| BITCOIN          | 2026-02-05 | 73019     | 73096.6   | 62473.2   | 63223.6   |      1.22319e+11 | -13.415    |   14.5488   |          0.86585  |           -1 |
| US5YT            | 2026-02-05 |     3.797 |     3.799 |     3.745 |     3.75  |      0           |  -1.23782  |    1.42218  |          0.987622 |           -1 |
| US10YT           | 2026-02-05 |     4.252 |     4.256 |     4.204 |     4.21  |      0           |  -0.987766 |    1.22296  |          0.990122 |           -1 |
| US30YT           | 2026-02-05 |     4.904 |     4.908 |     4.857 |     4.862 |      0           |  -0.85645  |    1.03997  |          0.991436 |           -1 |
