# Daily Market Report (LLM-ready) — 2026-01-27

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
- Best performer: **GOLD** (3.464%)
- Worst performer: **Dallor Index/USD** (-1.276%)
- Highest intraday range: **GOLD** (3.650%)
- Risk regime inference: **Risk-on (provisional)** (score=2.25)
  - Evidence:
    - Equity mean return: 0.145%
    - USD/KRW return: -0.703% (inverse tilt)
    - DXY return: -1.276% (inverse tilt)
    - Gold return: 3.464% (weak inverse tilt)
    - US10Y change proxy (ret_pct): -0.283% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| GOLD    |  3.46419  |
| BITCOIN |  0.912094 |
| NASDAQ  |  0.34695  |

### Bottom 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| Dallor Index/USD | -1.27558  |
| USD/KRW          | -0.702516 |
| US5YT            | -0.469732 |

### Top 3 intraday ranges (range_pct)
| stock            |   range_pct |
|:-----------------|------------:|
| GOLD             |     3.64999 |
| BITCOIN          |     2.40333 |
| Dallor Index/USD |     1.78767 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-27 | 23734.8   | 23865.3   | 23694.4   | 23817.1   |      7.0425e+09  |  0.34695  |    0.719969 |          1.00347  |            1 |
| S&P500           | 2026-01-27 |  6965.96  |  6988.82  |  6958.83  |  6978.6   |      3.22777e+09 |  0.181456 |    0.430518 |          1.00181  |            1 |
| DOWJONES         | 2026-01-27 | 49103.6   | 49157.8   | 48862.5   | 49003.4   |      5.33786e+08 | -0.203993 |    0.601344 |          0.99796  |           -1 |
| RUSSELL2000      | 2026-01-27 |  2659.93  |  2668.56  |  2650.64  |  2666.7   |      0           |  0.254501 |    0.673957 |          1.00255  |            1 |
| USD/KRW          | 2026-01-27 |  1441.96  |  1452.1   |  1431.83  |  1431.83  |      0           | -0.702516 |    1.40573  |          0.992975 |           -1 |
| Dallor Index/USD | 2026-01-27 |    97.054 |    97.286 |    95.551 |    95.816 |      0           | -1.27558  |    1.78767  |          0.987244 |           -1 |
| GOLD             | 2026-01-27 |  5005.5   |  5187.2   |  5004.5   |  5178.9   | 315272           |  3.46419  |    3.64999  |          1.03464  |            1 |
| BITCOIN          | 2026-01-27 | 88261     | 89389.4   | 87268.2   | 89066.1   |      3.81897e+10 |  0.912094 |    2.40333  |          1.00912  |            1 |
| US5YT            | 2026-01-27 |     3.832 |     3.841 |     3.802 |     3.814 |      0           | -0.469732 |    1.01775  |          0.995303 |           -1 |
| US10YT           | 2026-01-27 |     4.235 |     4.239 |     4.207 |     4.223 |      0           | -0.283344 |    0.75561  |          0.997167 |           -1 |
| US30YT           | 2026-01-27 |     4.832 |     4.842 |     4.809 |     4.832 |      0           |  0        |    0.682947 |          1        |            0 |
