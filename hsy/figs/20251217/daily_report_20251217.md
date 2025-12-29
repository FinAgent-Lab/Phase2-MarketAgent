# Daily Market Report (LLM-ready) — 2025-12-17

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
- Best performer: **GOLD** (0.905%)
- Worst performer: **BITCOIN** (-1.940%)
- Highest intraday range: **BITCOIN** (5.633%)
- Risk regime inference: **Risk-off (provisional)** (score=-2.75)
  - Evidence:
    - Equity mean return: -1.198%
    - USD/KRW return: 0.001% (inverse tilt)
    - DXY return: 0.163% (inverse tilt)
    - Gold return: 0.905% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.288% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| GOLD             |  0.905187 |
| Dallor Index/USD |  0.16292  |
| USD/KRW          |  0.00068  |

### Bottom 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| BITCOIN |  -1.93956 |
| NASDAQ  |  -1.91172 |
| S&P500  |  -1.19728 |

### Top 3 intraday ranges (range_pct)
| stock       |   range_pct |
|:------------|------------:|
| BITCOIN     |     5.63283 |
| RUSSELL2000 |     2.07247 |
| NASDAQ      |     2.01939 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |         Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|---------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2025-12-17 | 23135.6   | 23159.2   | 22692     | 22693.3   |    8.61614e+09 | -1.91172  |    2.01939  |          0.980883 |           -1 |
| S&P500           | 2025-12-17 |  6802.88  |  6812.26  |  6720.43  |  6721.43  |    5.12212e+09 | -1.19728  |    1.34986  |          0.988027 |           -1 |
| DOWJONES         | 2025-12-17 | 48128.1   | 48387.3   | 47856.8   | 47886     |    5.3426e+08  | -0.502996 |    1.10235  |          0.99497  |           -1 |
| RUSSELL2000      | 2025-12-17 |  2522.11  |  2540.25  |  2487.98  |  2492.3   |    5.12212e+09 | -1.18195  |    2.07247  |          0.988181 |           -1 |
| USD/KRW          | 2025-12-17 |  1471.73  |  1481.79  |  1470.41  |  1471.74  |    0           |  0.00068  |    0.77324  |          1.00001  |            1 |
| Dallor Index/USD | 2025-12-17 |    98.21  |    98.64  |    98.18  |    98.37  |    0           |  0.16292  |    0.468383 |          1.00163  |            1 |
| GOLD             | 2025-12-17 |  4308.5   |  4351.4   |  4308.5   |  4347.5   | 2169           |  0.905187 |    0.995704 |          1.00905  |            1 |
| BITCOIN          | 2025-12-17 | 87847.6   | 90264.6   | 85316.3   | 86143.8   |    4.42434e+10 | -1.93956  |    5.63283  |          0.980604 |           -1 |
| US5YT            | 2025-12-17 |     3.709 |     3.716 |     3.693 |     3.695 |    0           | -0.377465 |    0.620113 |          0.996225 |           -1 |
| US10YT           | 2025-12-17 |     4.163 |     4.17  |     4.143 |     4.151 |    0           | -0.288256 |    0.64857  |          0.997117 |           -1 |
| US30YT           | 2025-12-17 |     4.835 |     4.843 |     4.813 |     4.828 |    0           | -0.144777 |    0.62047  |          0.998552 |           -1 |
