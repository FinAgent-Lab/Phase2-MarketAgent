# Daily Market Report (LLM-ready) — 2025-12-26

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
- Best performer: **US30YT** (0.626%)
- Worst performer: **RUSSELL2000** (-0.488%)
- Highest intraday range: **BITCOIN** (3.246%)
- Risk regime inference: **Risk-off (provisional)** (score=-1.75)
  - Evidence:
    - Equity mean return: -0.201%
    - USD/KRW return: -0.046% (inverse tilt)
    - DXY return: 0.102% (inverse tilt)
    - Gold return: 0.379% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.340% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| US30YT  |  0.626309 |
| GOLD    |  0.378992 |
| US10YT  |  0.339639 |

### Bottom 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| RUSSELL2000 | -0.488065 |
| NASDAQ      | -0.223339 |
| S&P500      | -0.087659 |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| BITCOIN |     3.24557 |
| USD/KRW |     1.5893  |
| GOLD    |     1.20345 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |        Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|--------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2025-12-26 | 23645.9   | 23665.2   | 23567.9   | 23593.1   |   5.1703e+09  | -0.223339 |    0.41145  |          0.997767 |           -1 |
| S&P500           | 2025-12-26 |  6936.02  |  6945.77  |  6921.6   |  6929.94  |   2.58655e+09 | -0.087659 |    0.34847  |          0.999123 |           -1 |
| DOWJONES         | 2025-12-26 | 48712.5   | 48782     | 48589.1   | 48711     |   2.8877e+08  | -0.003079 |    0.396058 |          0.999969 |           -1 |
| RUSSELL2000      | 2025-12-26 |  2546.78  |  2546.78  |  2527.36  |  2534.35  |   2.58655e+09 | -0.488065 |    0.762528 |          0.995119 |           -1 |
| USD/KRW          | 2025-12-26 |  1447.18  |  1452.9   |  1429.9   |  1446.52  |   0           | -0.045608 |    1.5893   |          0.999544 |           -1 |
| Dallor Index/USD | 2025-12-26 |    97.92  |    98.13  |    97.86  |    98.02  |   0           |  0.102123 |    0.275732 |          1.00102  |            1 |
| GOLD             | 2025-12-26 |  4512     |  4556.3   |  4502     |  4529.1   | 263           |  0.378992 |    1.20345  |          1.00379  |            1 |
| BITCOIN          | 2025-12-26 | 87235.5   | 89459.4   | 86628.1   | 87301.4   |   4.24557e+10 |  0.075568 |    3.24557  |          1.00076  |            1 |
| US5YT            | 2025-12-26 |     3.694 |     3.711 |     3.682 |     3.697 |   0           |  0.081213 |    0.785058 |          1.00081  |            1 |
| US10YT           | 2025-12-26 |     4.122 |     4.145 |     4.11  |     4.136 |   0           |  0.339639 |    0.849099 |          1.0034   |            1 |
| US30YT           | 2025-12-26 |     4.79  |     4.826 |     4.781 |     4.82  |   0           |  0.626309 |    0.939459 |          1.00626  |            1 |
