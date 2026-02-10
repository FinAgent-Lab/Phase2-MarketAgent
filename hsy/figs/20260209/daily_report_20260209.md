# Daily Market Report (LLM-ready) — 2026-02-09

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
- Best performer: **GOLD** (1.647%)
- Worst performer: **US5YT** (-0.979%)
- Highest intraday range: **BITCOIN** (4.046%)
- Risk regime inference: **Risk-on (provisional)** (score=2.25)
  - Evidence:
    - Equity mean return: 0.730%
    - USD/KRW return: -0.266% (inverse tilt)
    - DXY return: -0.867% (inverse tilt)
    - Gold return: 1.647% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.944% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| GOLD        |  1.64681  |
| NASDAQ      |  1.24793  |
| RUSSELL2000 |  0.810173 |

### Bottom 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| US5YT            | -0.979353 |
| US10YT           | -0.943841 |
| Dallor Index/USD | -0.86694  |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| BITCOIN |     4.04627 |
| GOLD    |     2.44824 |
| NASDAQ  |     1.90091 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-02-09 | 22952.2   | 23314.7   | 22878.4   | 23238.7   |      6.73867e+09 |  1.24793  |    1.90091  |          1.01248  |            1 |
| S&P500           | 2026-02-09 |  6917.26  |  6980.1   |  6905.87  |  6964.82  |      3.36394e+09 |  0.687556 |    1.07311  |          1.00688  |            1 |
| DOWJONES         | 2026-02-09 | 50047.8   | 50219.4   | 49837.4   | 50135.9   |      6.2364e+08  |  0.175996 |    0.763169 |          1.00176  |            1 |
| RUSSELL2000      | 2026-02-09 |  2667.44  |  2695.45  |  2659.96  |  2689.05  |      0           |  0.810173 |    1.33044  |          1.0081   |            1 |
| USD/KRW          | 2026-02-09 |  1463.33  |  1468.25  |  1452.95  |  1459.44  |      0           | -0.265833 |    1.04556  |          0.997342 |           -1 |
| Dallor Index/USD | 2026-02-09 |    97.7   |    97.761 |    96.793 |    96.853 |      0           | -0.86694  |    0.990791 |          0.991331 |           -1 |
| GOLD             | 2026-02-09 |  5003.6   |  5111.1   |  4988.6   |  5086     | 118452           |  1.64681  |    2.44824  |          1.01647  |            1 |
| BITCOIN          | 2026-02-09 | 70306.1   | 71291     | 68446.2   | 70348.8   |      5.39449e+10 |  0.060661 |    4.04627  |          1.00061  |            1 |
| US5YT            | 2026-02-09 |     3.778 |     3.778 |     3.739 |     3.741 |      0           | -0.979353 |    1.03229  |          0.990206 |           -1 |
| US10YT           | 2026-02-09 |     4.238 |     4.238 |     4.196 |     4.198 |      0           | -0.943841 |    0.991029 |          0.990562 |           -1 |
| US30YT           | 2026-02-09 |     4.889 |     4.89  |     4.846 |     4.848 |      0           | -0.838615 |    0.899992 |          0.991614 |           -1 |
