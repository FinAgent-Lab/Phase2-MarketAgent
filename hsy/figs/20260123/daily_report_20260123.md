# Daily Market Report (LLM-ready) — 2026-01-23

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
- Best performer: **GOLD** (0.864%)
- Worst performer: **RUSSELL2000** (-1.605%)
- Highest intraday range: **BITCOIN** (2.520%)
- Risk regime inference: **Risk-off (provisional)** (score=-0.75)
  - Evidence:
    - Equity mean return: -0.393%
    - USD/KRW return: -1.256% (inverse tilt)
    - DXY return: -0.840% (inverse tilt)
    - Gold return: 0.864% (weak inverse tilt)
    - US10Y change proxy (ret_pct): 0.047% (context only)

## Leaderboards
### Top 3 daily returns (ret_pct)
| stock   |   ret_pct |
|:--------|----------:|
| GOLD    |  0.864376 |
| NASDAQ  |  0.257362 |
| US30YT  |  0.165811 |

### Bottom 3 daily returns (ret_pct)
| stock            |   ret_pct |
|:-----------------|----------:|
| RUSSELL2000      | -1.60484  |
| USD/KRW          | -1.25593  |
| Dallor Index/USD | -0.839999 |

### Top 3 intraday ranges (range_pct)
| stock   |   range_pct |
|:--------|------------:|
| BITCOIN |      2.5202 |
| GOLD    |      1.8259 |
| USD/KRW |      1.7859 |

## Notes / caveats
- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.
- Some assets may have missing/zero Volume; volume-based interpretation may be limited.
- FX/yield series may have different market conventions; interpret ret_pct carefully.

## Raw table (ground truth)
| stock            | date       |      Open |      High |       Low |     Close |           Volume |   ret_pct |   range_pct |   close_over_open |   candle_dir |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|-----------------:|----------:|------------:|------------------:|-------------:|
| NASDAQ           | 2026-01-23 | 23440.9   | 23610.7   | 23374.3   | 23501.2   |      7.10632e+09 |  0.257362 |    1.00884  |          1.00257  |            1 |
| S&P500           | 2026-01-23 |  6907.85  |  6932.96  |  6895.5   |  6915.61  |      3.22823e+09 |  0.112333 |    0.542281 |          1.00112  |            1 |
| DOWJONES         | 2026-01-23 | 49264.5   | 49265.5   | 48963.1   | 49098.7   |      4.61035e+08 | -0.336607 |    0.61385  |          0.996634 |           -1 |
| RUSSELL2000      | 2026-01-23 |  2712.7   |  2712.7   |  2664.55  |  2669.16  |      0           | -1.60484  |    1.77492  |          0.983952 |           -1 |
| USD/KRW          | 2026-01-23 |  1464.25  |  1469.64  |  1443.49  |  1445.86  |      0           | -1.25593  |    1.7859   |          0.987441 |           -1 |
| Dallor Index/USD | 2026-01-23 |    98.333 |    98.481 |    97.425 |    97.507 |      0           | -0.839999 |    1.0739   |          0.9916   |           -1 |
| GOLD             | 2026-01-23 |  4940     |  4991.4   |  4901.2   |  4982.7   | 271236           |  0.864376 |    1.8259   |          1.00864  |            1 |
| BITCOIN          | 2026-01-23 | 89460.2   | 90870.7   | 88616.1   | 89332.1   |      3.8236e+10  | -0.143229 |    2.5202   |          0.998568 |           -1 |
| US5YT            | 2026-01-23 |     3.842 |     3.863 |     3.835 |     3.839 |      0           | -0.078079 |    0.728796 |          0.999219 |           -1 |
| US10YT           | 2026-01-23 |     4.237 |     4.263 |     4.233 |     4.239 |      0           |  0.0472   |    0.708042 |          1.00047  |            1 |
| US30YT           | 2026-01-23 |     4.825 |     4.861 |     4.819 |     4.833 |      0           |  0.165811 |    0.870472 |          1.00166  |            1 |
