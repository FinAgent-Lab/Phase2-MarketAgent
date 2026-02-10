# Daily Market Report (LLM-ready) — 2026-01-14

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
- Best performer: **BITCOIN** (2.256%)
- Worst performer: **USD/KRW** (-0.801%)
- Highest intraday range: **BITCOIN** (3.259%)
- Risk regime inference: **Risk-on (provisional)** (score=2.25)
  - Evidence:
    - Equity mean return: 0.090%
    - USD/KRW return: -0.801% (inverse tilt)
    - DXY return: -0.089% (inverse tilt)
    - Gold return: 0.703% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.481% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| BITCOIN     |  2.25623  |
| RUSSELL2000 |  0.782086 |
| GOLD        |  0.703051 |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| USD/KRW | -0.800535 |
| US30YT  | -0.559933 |
| US10YT  | -0.480757 |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| BITCOIN |     3.25883 |
| USD/KRW |     1.23743 |
| GOLD    |     1.22326 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-14 | 23563.9   | 23590.2   | 23306.7   | 23471.8   |      1.09063e+10 | -0.391132 |    1.20325  |          0.996089 |           -1 |
| S&P500           | 2026-01-14 |  6937.41  |  6941.3   |  6885.74  |  6926.6   |      3.36812e+09 | -0.155823 |    0.800869 |          0.998442 |           -1 |
| DOWJONES         | 2026-01-14 | 49088.2   | 49195.1   | 48852     | 49149.6   |      5.30675e+08 |  0.125038 |    0.698988 |          1.00125  |            1 |
| RUSSELL2000      | 2026-01-14 |  2631.06  |  2653.31  |  2624.29  |  2651.64  |      0           |  0.782086 |    1.10277  |          1.00782  |            1 |
| USD/KRW          | 2026-01-14 |  1474.02  |  1479.08  |  1460.84  |  1462.22  |      0           | -0.800535 |    1.23743  |          0.991995 |           -1 |
| Dallor Index/USD | 2026-01-14 |    99.186 |    99.248 |    98.933 |    99.098 |      0           | -0.08872  |    0.317588 |          0.999113 |           -1 |
| GOLD             | 2026-01-14 |  4594.3   |  4650.5   |  4594.3   |  4626.6   | 287828           |  0.703051 |    1.22326  |          1.00703  |            1 |
| BITCOIN          | 2026-01-14 | 95363.3   | 97735.1   | 94627.4   | 97514.9   |      6.67824e+10 |  2.25623  |    3.25883  |          1.02256  |            1 |
| US5YT            | 2026-01-14 |     3.734 |     3.743 |     3.707 |     3.717 |      0           | -0.455281 |    0.964114 |          0.995447 |           -1 |
| US10YT           | 2026-01-14 |     4.16  |     4.169 |     4.132 |     4.14  |      0           | -0.480757 |    0.889416 |          0.995192 |           -1 |
| US30YT           | 2026-01-14 |     4.822 |     4.833 |     4.79  |     4.795 |      0           | -0.559933 |    0.891751 |          0.994401 |           -1 |
