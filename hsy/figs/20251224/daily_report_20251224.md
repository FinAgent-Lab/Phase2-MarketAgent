# Daily Market Report (LLM-ready) — 2025-12-24

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
- Best performer: **DOWJONES** (0.633%)
- Worst performer: **US10YT** (-0.744%)
- Highest intraday range: **USD/KRW** (3.312%)
- Risk regime inference: **Risk-on (provisional)** (score=1.25)
  - Evidence:
    - Equity mean return: 0.403%
    - USD/KRW return: 0.000% (inverse tilt)
    - DXY return: 0.092% (inverse tilt)
    - Gold return: -0.447% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.744% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| DOWJONES    |  0.632836 |
| S&P500      |  0.393049 |
| RUSSELL2000 |  0.344579 |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| US10YT  | -0.743932 |
| US5YT   | -0.694631 |
| US30YT  | -0.62138  |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| USD/KRW |    3.31244  |
| BITCOIN |    1.76774  |
| US10YT  |    0.839929 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |        Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|--------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2025-12-24 | 23555.9   | 23621.7   | 23528     | 23613.3   |   3.88519e+09 |  0.243511 |    0.397989 |          1.00243  |            1 |
| S&P500           | 2025-12-24 |  6904.91  |  6937.32  |  6904.91  |  6932.05  |   1.79827e+09 |  0.393049 |    0.469371 |          1.00393  |            1 |
| DOWJONES         | 2025-12-24 | 48424.7   | 48771.3   | 48386.6   | 48731.2   |   2.0674e+08  |  0.632836 |    0.794492 |          1.00633  |            1 |
| RUSSELL2000      | 2025-12-24 |  2539.33  |  2549.96  |  2535.13  |  2548.08  |   1.79827e+09 |  0.344579 |    0.584015 |          1.00345  |            1 |
| USD/KRW          | 2025-12-24 |  1478.67  |  1478.67  |  1429.69  |  1478.67  |   0           |  0        |    3.31244  |          1        |            0 |
| Dallor Index/USD | 2025-12-24 |    97.89  |    98.01  |    97.75  |    97.98  |   0           |  0.091944 |    0.265606 |          1.00092  |            1 |
| GOLD             | 2025-12-24 |  4500.7   |  4503.4   |  4468.4   |  4480.6   | 500           | -0.446599 |    0.777657 |          0.995534 |           -1 |
| BITCOIN          | 2025-12-24 | 87404.3   | 87956.9   | 86411.8   | 87612     |   2.55503e+10 |  0.237563 |    1.76774  |          1.00238  |            1 |
| US5YT            | 2025-12-24 |     3.743 |     3.743 |     3.713 |     3.717 |   0           | -0.694631 |    0.801495 |          0.993054 |           -1 |
| US10YT           | 2025-12-24 |     4.167 |     4.167 |     4.132 |     4.136 |   0           | -0.743932 |    0.839929 |          0.992561 |           -1 |
| US30YT           | 2025-12-24 |     4.828 |     4.829 |     4.791 |     4.798 |   0           | -0.62138  |    0.787078 |          0.993786 |           -1 |
