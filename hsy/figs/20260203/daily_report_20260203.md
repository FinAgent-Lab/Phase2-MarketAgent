# Daily Market Report (LLM-ready) — 2026-02-03

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
- Best performer: **GOLD** (5.711%)
- Worst performer: **BITCOIN** (-3.200%)
- Highest intraday range: **BITCOIN** (7.545%)
- Risk regime inference: **Risk-off (provisional)** (score=-0.75)
  - Evidence:
    - Equity mean return: -0.734%
    - USD/KRW return: -0.253% (inverse tilt)
    - DXY return: -0.157% (inverse tilt)
    - Gold return: 5.711% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.373% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| GOLD             |  5.71093  |
| RUSSELL2000      |  0.01382  |
| Dallor Index/USD | -0.156892 |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| BITCOIN |  -3.20019 |
| NASDAQ  |  -1.74188 |
| S&P500  |  -0.9683  |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| BITCOIN |     7.54532 |
| GOLD    |     6.98998 |
| NASDAQ  |     2.80718 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-02-03 | 23667.4   | 23691.6   | 23027.2   | 23255.2   |      8.67553e+09 | -1.74188  |    2.80718  |          0.982581 |           -1 |
| S&P500           | 2026-02-03 |  6985.45  |  6993.08  |  6862.05  |  6917.81  |      4.50915e+09 | -0.9683   |    1.87576  |          0.990317 |           -1 |
| DOWJONES         | 2026-02-03 | 49358.6   | 49653.1   | 48832.8   | 49241     |      7.41316e+08 | -0.23826  |    1.66202  |          0.997617 |           -1 |
| RUSSELL2000      | 2026-02-03 |  2648.13  |  2666.85  |  2605.88  |  2648.5   |      0           |  0.01382  |    2.30221  |          1.00014  |            1 |
| USD/KRW          | 2026-02-03 |  1453.53  |  1453.89  |  1438.88  |  1449.85  |      0           | -0.25318  |    1.03266  |          0.997468 |           -1 |
| Dallor Index/USD | 2026-02-03 |    97.519 |    97.692 |    97.298 |    97.366 |      0           | -0.156892 |    0.404029 |          0.998431 |           -1 |
| GOLD             | 2026-02-03 |  4691     |  5018.1   |  4690.2   |  4958.9   | 251103           |  5.71093  |    6.98998  |          1.05711  |            1 |
| BITCOIN          | 2026-02-03 | 78677.4   | 79008.9   | 73072.4   | 76159.6   |      6.71004e+10 | -3.20019  |    7.54532  |          0.967998 |           -1 |
| US5YT            | 2026-02-03 |     3.847 |     3.861 |     3.826 |     3.837 |      0           | -0.259949 |    0.909808 |          0.997401 |           -1 |
| US10YT           | 2026-02-03 |     4.29  |     4.3   |     4.266 |     4.274 |      0           | -0.372956 |    0.79255  |          0.99627  |           -1 |
| US30YT           | 2026-02-03 |     4.92  |     4.928 |     4.898 |     4.906 |      0           | -0.284552 |    0.60976  |          0.997154 |           -1 |
