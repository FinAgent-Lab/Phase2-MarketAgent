# Daily Market Report (LLM-ready) — 2026-01-12

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
- Best performer: **GOLD** (1.612%)
- Worst performer: **US30YT** (-0.391%)
- Highest intraday range: **GOLD** (2.643%)
- Risk regime inference: **Risk-on (provisional)** (score=1.25)
  - Evidence:
    - Equity mean return: 0.538%
    - USD/KRW return: 0.652% (inverse tilt)
    - DXY return: -0.286% (inverse tilt)
    - Gold return: 1.612% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.238% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| GOLD        |  1.6118   |
| RUSSELL2000 |  0.82635  |
| NASDAQ      |  0.666023 |

### Bottom 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| US30YT           | -0.391028 |
| Dallor Index/USD | -0.286396 |
| US10YT           | -0.238271 |

### Top 3 intraday ranges (range_pct)
| stock    |   range_pct |
|:---------|------------:|
| GOLD     |     2.64291 |
| BITCOIN  |     2.45162 |
| DOWJONES |     1.25666 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-12 | 23576.9   | 23804     | 23563     | 23733.9   |      7.76661e+09 |  0.666023 |    1.02251  |          1.00666  |            1 |
| S&P500           | 2026-01-12 |  6944.12  |  6986.33  |  6934.07  |  6977.27  |      3.03069e+09 |  0.477381 |    0.752583 |          1.00477  |            1 |
| DOWJONES         | 2026-01-12 | 49499.7   | 49633.4   | 49011.3   | 49590.2   |      5.16436e+08 |  0.182885 |    1.25666  |          1.00183  |            1 |
| RUSSELL2000      | 2026-01-12 |  2614.09  |  2636.72  |  2606.9   |  2635.69  |      0           |  0.82635  |    1.14094  |          1.00826  |            1 |
| USD/KRW          | 2026-01-12 |  1457.8   |  1470.03  |  1456.13  |  1467.3   |      0           |  0.651667 |    0.953493 |          1.00652  |            1 |
| Dallor Index/USD | 2026-01-12 |    99.165 |    99.246 |    98.672 |    98.881 |      0           | -0.286396 |    0.578838 |          0.997136 |           -1 |
| GOLD             | 2026-01-12 |  4529.1   |  4640.5   |  4520.8   |  4602.1   | 280525           |  1.6118   |    2.64291  |          1.01612  |            1 |
| BITCOIN          | 2026-01-12 | 90851.9   | 92340.9   | 90113.5   | 91186.1   |      4.20507e+10 |  0.367803 |    2.45162  |          1.00368  |            1 |
| US5YT            | 2026-01-12 |     3.769 |     3.773 |     3.748 |     3.767 |      0           | -0.053067 |    0.663308 |          0.999469 |           -1 |
| US10YT           | 2026-01-12 |     4.197 |     4.201 |     4.169 |     4.187 |      0           | -0.238271 |    0.762451 |          0.997617 |           -1 |
| US30YT           | 2026-01-12 |     4.859 |     4.861 |     4.819 |     4.84  |      0           | -0.391028 |    0.864381 |          0.99609  |           -1 |
