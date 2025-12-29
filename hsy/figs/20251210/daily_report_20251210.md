# Daily Market Report (LLM-ready) — 2025-12-10

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
- Best performer: **RUSSELL2000** (1.392%)
- Worst performer: **US5YT** (-1.236%)
- Highest intraday range: **BITCOIN** (3.061%)
- Risk regime inference: **Risk-on (provisional)** (score=2.25)
  - Evidence:
    - Equity mean return: 0.922%
    - USD/KRW return: 0.000% (inverse tilt)
    - DXY return: -0.433% (inverse tilt)
    - Gold return: -0.299% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.904% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| RUSSELL2000 |  1.39158  |
| DOWJONES    |  1.01692  |
| S&P500      |  0.778372 |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| US5YT   | -1.23554  |
| US10YT  | -0.904334 |
| BITCOIN | -0.727426 |

### Top 3 intraday ranges (range_pct)
| stock       |   range_pct |
|:------------|------------:|
| BITCOIN     |     3.06059 |
| RUSSELL2000 |     2.26344 |
| US5YT       |     1.78759 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |        Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|--------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2025-12-10 | 23536     | 23704.1   | 23435.2   | 23654.2   |   7.9879e+09  |  0.501999 |    1.14255  |          1.00502  |            1 |
| S&P500           | 2025-12-10 |  6833.49  |  6900.67  |  6824.69  |  6886.68  |   5.52657e+09 |  0.778372 |    1.11188  |          1.00778  |            1 |
| DOWJONES         | 2025-12-10 | 47574     | 48197.3   | 47462.9   | 48057.8   |   5.4561e+08  |  1.01692  |    1.54362  |          1.01017  |            1 |
| RUSSELL2000      | 2025-12-10 |  2524.48  |  2576.31  |  2519.17  |  2559.61  |   5.52657e+09 |  1.39158  |    2.26344  |          1.01392  |            1 |
| USD/KRW          | 2025-12-10 |  1467.93  |  1472.35  |  1467.51  |  1467.93  |   0           |  0        |    0.329714 |          1        |            0 |
| Dallor Index/USD | 2025-12-10 |    99.22  |    99.26  |    98.59  |    98.79  |   0           | -0.433381 |    0.675273 |          0.995666 |           -1 |
| GOLD             | 2025-12-10 |  4209     |  4234.5   |  4183.6   |  4196.4   | 692           | -0.299361 |    1.20931  |          0.997006 |           -1 |
| BITCOIN          | 2025-12-10 | 92695.2   | 94477.2   | 91640.1   | 92020.9   |   6.54207e+10 | -0.727426 |    3.06059  |          0.992726 |           -1 |
| US5YT            | 2025-12-10 |     3.804 |     3.806 |     3.738 |     3.757 |   0           | -1.23554  |    1.78759  |          0.987645 |           -1 |
| US10YT           | 2025-12-10 |     4.202 |     4.204 |     4.147 |     4.164 |   0           | -0.904334 |    1.3565   |          0.990957 |           -1 |
| US30YT           | 2025-12-10 |     4.82  |     4.822 |     4.771 |     4.797 |   0           | -0.477183 |    1.05809  |          0.995228 |           -1 |
