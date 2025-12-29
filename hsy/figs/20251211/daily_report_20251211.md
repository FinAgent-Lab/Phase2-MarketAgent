# Daily Market Report (LLM-ready) — 2025-12-11

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
- Best performer: **GOLD** (1.456%)
- Worst performer: **Dallor Index/USD** (-0.213%)
- Highest intraday range: **BITCOIN** (4.585%)
- Risk regime inference: **Risk-on (provisional)** (score=1.25)
  - Evidence:
    - Equity mean return: 0.847%
    - USD/KRW return: 0.444% (inverse tilt)
    - DXY return: -0.213% (inverse tilt)
    - Gold return: 1.456% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.242% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock       |   ret_pct |
|:------------|----------:|
| GOLD        |   1.45597 |
| DOWJONES    |   1.29175 |
| RUSSELL2000 |   1.15698 |

### Bottom 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| Dallor Index/USD | -0.213067 |
| US5YT            |  0.134768 |
| US30YT           |  0.230177 |

### Top 3 intraday ranges (range_pct)
| stock    |   range_pct |
|:---------|------------:|
| BITCOIN  |     4.58527 |
| GOLD     |     1.71875 |
| DOWJONES |     1.40058 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |        Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|--------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2025-12-11 | 23509.2   | 23606.7   | 23308.9   | 23593.9   |   8.33777e+09 |  0.360023 |    1.26652  |          1.0036   |            1 |
| S&P500           | 2025-12-11 |  6861.3   |  6903.46  |  6833.45  |  6901     |   5.02106e+09 |  0.57861  |    1.02036  |          1.00579  |            1 |
| DOWJONES         | 2025-12-11 | 48082.9   | 48756.3   | 48082.9   | 48704     |   4.9395e+08  |  1.29175  |    1.40058  |          1.01292  |            1 |
| RUSSELL2000      | 2025-12-11 |  2560.98  |  2593.89  |  2558.46  |  2590.61  |   5.02106e+09 |  1.15698  |    1.38345  |          1.01157  |            1 |
| USD/KRW          | 2025-12-11 |  1462.55  |  1473.93  |  1462.55  |  1469.04  |   0           |  0.443745 |    0.778093 |          1.00444  |            1 |
| Dallor Index/USD | 2025-12-11 |    98.56  |    98.76  |    98.13  |    98.35  |   0           | -0.213067 |    0.63921  |          0.997869 |           -1 |
| GOLD             | 2025-12-11 |  4224     |  4286.9   |  4214.3   |  4285.5   | 528           |  1.45597  |    1.71875  |          1.01456  |            1 |
| BITCOIN          | 2025-12-11 | 92011.3   | 93554.3   | 89335.3   | 92511.3   |   6.45328e+10 |  0.543445 |    4.58527  |          1.00543  |            1 |
| US5YT            | 2025-12-11 |     3.71  |     3.72  |     3.679 |     3.715 |   0           |  0.134768 |    1.10512  |          1.00135  |            1 |
| US10YT           | 2025-12-11 |     4.131 |     4.143 |     4.102 |     4.141 |   0           |  0.242066 |    0.992493 |          1.00242  |            1 |
| US30YT           | 2025-12-11 |     4.779 |     4.794 |     4.749 |     4.79  |   0           |  0.230177 |    0.941621 |          1.0023   |            1 |
