# Daily Market Report (LLM-ready) — 2026-02-04

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
- Best performer: **USD/KRW** (0.999%)
- Worst performer: **BITCOIN** (-4.526%)
- Highest intraday range: **BITCOIN** (6.172%)
- Risk regime inference: **Risk-off (provisional)** (score=-2.75)
  - Evidence:
    - Equity mean return: -0.707%
    - USD/KRW return: 0.999% (inverse tilt)
    - DXY return: 0.238% (inverse tilt)
    - Gold return: 0.379% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.164% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| USD/KRW |  0.998926 |
| US30YT  |  0.449619 |
| GOLD    |  0.378563 |

### Bottom 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| BITCOIN     |  -4.52624 |
| NASDAQ      |  -1.34573 |
| RUSSELL2000 |  -1.23803 |

### Top 3 intraday ranges (range_pct)
| stock       |   range_pct |
|:------------|------------:|
| BITCOIN     |     6.17195 |
| GOLD        |     4.95761 |
| RUSSELL2000 |     2.58004 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-02-04 | 23217     | 23270.1   | 22684.5   | 22904.6   |      9.08122e+09 | -1.34573  |    2.5221   |          0.986543 |           -1 |
| S&P500           | 2026-02-04 |  6924.5   |  6936.09  |  6838.8   |  6882.72  |      5.12478e+09 | -0.603362 |    1.40501  |          0.993966 |           -1 |
| DOWJONES         | 2026-02-04 | 49323.6   | 49649.9   | 49112.4   | 49501.3   |      7.42922e+08 |  0.360296 |    1.0896   |          1.0036   |            1 |
| RUSSELL2000      | 2026-02-04 |  2657.45  |  2660.44  |  2591.87  |  2624.55  |      0           | -1.23803  |    2.58004  |          0.98762  |           -1 |
| USD/KRW          | 2026-02-04 |  1447.55  |  1462.02  |  1447.55  |  1462.01  |      0           |  0.998926 |    0.999618 |          1.00999  |            1 |
| Dallor Index/USD | 2026-02-04 |    97.429 |    97.73  |    97.309 |    97.661 |      0           |  0.238124 |    0.432115 |          1.00238  |            1 |
| GOLD             | 2026-02-04 |  4966.1   |  5113.9   |  4867.7   |  4984.9   | 239067           |  0.378563 |    4.95761  |          1.00379  |            1 |
| BITCOIN          | 2026-02-04 | 75657.3   | 76745.6   | 72076     | 72232.8   |      6.44532e+10 | -4.52624  |    6.17195  |          0.954738 |           -1 |
| US5YT            | 2026-02-04 |     3.835 |     3.852 |     3.814 |     3.833 |      0           | -0.052141 |    0.990876 |          0.999479 |           -1 |
| US10YT           | 2026-02-04 |     4.268 |     4.29  |     4.261 |     4.275 |      0           |  0.164011 |    0.679471 |          1.00164  |            1 |
| US30YT           | 2026-02-04 |     4.893 |     4.922 |     4.891 |     4.915 |      0           |  0.449619 |    0.633561 |          1.0045   |            1 |
