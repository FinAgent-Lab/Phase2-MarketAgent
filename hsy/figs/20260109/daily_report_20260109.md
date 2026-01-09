# Daily Market Report (LLM-ready) — 2026-01-09

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
- Best performer: **NASDAQ** (0.745%)
- Worst performer: **BITCOIN** (-0.754%)
- Highest intraday range: **BITCOIN** (2.402%)
- Risk regime inference: **Mixed / unclear (provisional)** (score=0.25)
  - Evidence:
    - Equity mean return: 0.553%
    - USD/KRW return: 0.425% (inverse tilt)
    - DXY return: 0.246% (inverse tilt)
    - Gold return: 0.588% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.382% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| NASDAQ  |  0.745375 |
| GOLD    |  0.588074 |
| S&P500  |  0.555004 |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| BITCOIN | -0.754139 |
| US30YT  | -0.618689 |
| US10YT  | -0.38213  |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| BITCOIN |     2.40186 |
| US5YT   |     1.54585 |
| GOLD    |     1.45235 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-09 | 23496.2   | 23721.2   | 23426.5   | 23671.3   |      7.00567e+09 |  0.745375 |    1.25414  |          1.00745  |            1 |
| S&P500           | 2026-01-09 |  6927.83  |  6978.36  |  6917.64  |  6966.28  |      2.9561e+09  |  0.555004 |    0.876461 |          1.00555  |            1 |
| DOWJONES         | 2026-01-09 | 49234.8   | 49571.4   | 49197.1   | 49504.1   |      4.42717e+08 |  0.546893 |    0.760339 |          1.00547  |            1 |
| RUSSELL2000      | 2026-01-09 |  2614.73  |  2635.8   |  2606.66  |  2624.22  |      0           |  0.363093 |    1.11435  |          1.00363  |            1 |
| USD/KRW          | 2026-01-09 |  1453.77  |  1461.46  |  1451.06  |  1459.95  |      0           |  0.425097 |    0.715375 |          1.00425  |            1 |
| Dallor Index/USD | 2026-01-09 |    98.912 |    99.264 |    98.896 |    99.155 |      0           |  0.245669 |    0.372044 |          1.00246  |            1 |
| GOLD             | 2026-01-09 |  4489.3   |  4527     |  4461.8   |  4515.7   | 196949           |  0.588074 |    1.45235  |          1.00588  |            1 |
| BITCOIN          | 2026-01-09 | 91019.6   | 91814.7   | 89628.6   | 90333.2   |      3.90386e+10 | -0.754139 |    2.40186  |          0.992459 |           -1 |
| US5YT            | 2026-01-09 |     3.752 |     3.783 |     3.725 |     3.757 |      0           |  0.133259 |    1.54585  |          1.00133  |            1 |
| US10YT           | 2026-01-09 |     4.187 |     4.211 |     4.159 |     4.171 |      0           | -0.38213  |    1.24194  |          0.996179 |           -1 |
| US30YT           | 2026-01-09 |     4.849 |     4.874 |     4.812 |     4.819 |      0           | -0.618689 |    1.27862  |          0.993813 |           -1 |
