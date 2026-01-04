import os
import argparse
import numpy as np
import pandas as pd
import FinanceDataReader as fdr
from typing import Dict, List, Optional, Tuple
import matplotlib.pyplot as plt


# =============================================================================
# 1) Data Loading Layer
# =============================================================================
def load_stock_data(symbol: str, target_date: str) -> Optional[pd.Series]:
    """
    Fetch OHLCV data for `symbol` and return the row for `target_date`.

    Rationale
    ---------
    - FinanceDataReader returns a time-series DataFrame indexed by trading dates.
    - For a daily report, we need exactly one row per asset for the report date.
    - If the asset has no data for that date (holiday/weekend/data gap), we
      return None to keep the pipeline robust.

    Parameters
    ----------
    symbol : str
        FinanceDataReader symbol code (e.g., "IXIC", "US500", "BTC/USD").
    target_date : str
        Target date in "YYYY-MM-DD".

    Returns
    -------
    pd.Series or None
        Single-day OHLCV row if available; otherwise None.
    """
    try:
        df = fdr.DataReader(symbol, target_date)

        # Convert index to string to avoid mismatch between Timestamp vs string date
        idx_as_str = df.index.astype(str)

        if target_date in idx_as_str:
            # Daily index should yield a unique match; use iloc[0] defensively
            row = df.loc[idx_as_str == target_date].iloc[0]
            return row

        print(f"[WARN] No data for target date / symbol={symbol} / date={target_date}")
        return None

    except KeyError as e:
        print(f"[WARN] KeyError (no data on that date) / symbol={symbol} / err={e}")
        return None

    except Exception as e:
        print(f"[ERROR] Unexpected error / symbol={symbol} / err={e}")
        return None


def collect_indices(target_date: str, symbol_map: Dict[str, str]) -> pd.DataFrame:
    """
    Build a unified daily OHLCV table across many assets.

    Output schema
    -------------
    - stock: human-friendly asset label (e.g., "NASDAQ")
    - date : report date (string)
    - Open, High, Low, Close, Volume: standard OHLCV fields

    Notes
    -----
    - Some assets do not provide meaningful Volume; we still store it as-is.
    - Missing assets for a given date are skipped (not forced to NaN rows).

    Parameters
    ----------
    target_date : str
        Report date "YYYY-MM-DD".
    symbol_map : Dict[str, str]
        Mapping: asset label -> FDR symbol.

    Returns
    -------
    pd.DataFrame
        One row per asset (when data exists).
    """
    results: List[dict] = []

    for name, symbol in symbol_map.items():
        data = load_stock_data(symbol, target_date)
        if data is None:
            continue

        results.append(
            {
                "stock": name,
                "date": target_date,
                "Open": data.get("Open", np.nan),
                "High": data.get("High", np.nan),
                "Low": data.get("Low", np.nan),
                "Close": data.get("Close", np.nan),
                "Volume": data.get("Volume", np.nan),
            }
        )

    return pd.DataFrame(results)


# =============================================================================
# 2) Feature Engineering (Daily Metrics)
# =============================================================================
def add_daily_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add derived metrics for daily market reporting.

    Added columns
    -------------
    ret_pct:
        (Close - Open) / Open * 100
        - Primary "scoreboard" metric for daily performance.
    range_pct:
        (High - Low) / Open * 100
        - Direction-agnostic intraday volatility proxy.
    close_over_open:
        Close / Open
        - Multiplicative performance ratio (useful for logs/compounding).
    candle_dir:
        sign(Close - Open) in {-1, 0, +1}
        - Simple direction classifier for summarization.

    Returns
    -------
    pd.DataFrame
        Input columns + derived metrics.
    """
    out = df.copy()

    for col in ["Open", "High", "Low", "Close"]:
        out[col] = pd.to_numeric(out[col], errors="coerce")

    out["Volume"] = pd.to_numeric(out.get("Volume", np.nan), errors="coerce")

    out["ret_pct"] = (out["Close"] - out["Open"]) / out["Open"] * 100.0
    out["range_pct"] = (out["High"] - out["Low"]) / out["Open"] * 100.0
    out["close_over_open"] = out["Close"] / out["Open"]
    out["candle_dir"] = np.sign(out["Close"] - out["Open"]).astype(int)

    return out


# =============================================================================
# 3) LLM-Friendly Markdown Export
# =============================================================================
def _safe_top_bottom(df: pd.DataFrame, col: str, k: int = 3) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Utility to get top/bottom k rows by `col`, excluding NaN/inf.
    """
    d = df.replace([np.inf, -np.inf], np.nan).dropna(subset=[col]).copy()
    if d.empty:
        return d, d
    top = d.sort_values(col, ascending=False).head(k)
    bottom = d.sort_values(col, ascending=True).head(k)
    return top, bottom


def infer_risk_regime(df: pd.DataFrame) -> Dict[str, object]:
    """
    Infer a simple Risk-on / Risk-off signal using a heuristic.

    Heuristic components (configurable via your later refinement)
    ------------------------------------------------------------
    - Equity indices: NASDAQ, S&P500, DOWJONES, RUSSELL2000
      -> positive average return suggests risk-on
    - VIX: negative return suggests risk-on
    - USD/KRW and Dollar Index: risk-off often coincides with stronger USD
      -> positive return may tilt risk-off
    - GOLD: positive return can be risk-off (flight to safety) *or* inflation hedge
    - US10YT: higher yields can mean growth optimism (risk-on) or inflation fear;
      we treat direction as weak signal.

    Returns
    -------
    dict
        Includes label and the underlying evidence used for explanation.
    """
    equity = ["NASDAQ", "S&P500", "DOWJONES", "RUSSELL2000"]
    vix = "VIX"
    usdkrw = "USD/KRW"
    dxy = "Dallor Index/USD"
    gold = "GOLD"
    us10 = "US10YT"

    def get_ret(name: str) -> Optional[float]:
        r = df.loc[df["stock"] == name, "ret_pct"]
        if r.empty:
            return None
        val = r.iloc[0]
        if pd.isna(val) or np.isinf(val):
            return None
        return float(val)

    # Equity mean return (if available)
    eq_rets = [get_ret(x) for x in equity]
    eq_rets = [x for x in eq_rets if x is not None]
    eq_mean = float(np.mean(eq_rets)) if eq_rets else None

    vix_ret = get_ret(vix)
    usdkrw_ret = get_ret(usdkrw)
    dxy_ret = get_ret(dxy)
    gold_ret = get_ret(gold)
    us10_ret = get_ret(us10)

    # Scoring: positive => risk-on, negative => risk-off
    score = 0.0
    evidence = []

    if eq_mean is not None:
        score += np.sign(eq_mean) * 1.5
        evidence.append(f"Equity mean return: {eq_mean:.3f}%")

    if vix_ret is not None:
        score += (-np.sign(vix_ret)) * 1.0  # VIX up => risk-off
        evidence.append(f"VIX return: {vix_ret:.3f}% (inverse signal)")

    if usdkrw_ret is not None:
        score += (-np.sign(usdkrw_ret)) * 0.5  # USD/KRW up => KRW weaker => risk-off tilt
        evidence.append(f"USD/KRW return: {usdkrw_ret:.3f}% (inverse tilt)")

    if dxy_ret is not None:
        score += (-np.sign(dxy_ret)) * 0.5  # DXY up => risk-off tilt
        evidence.append(f"DXY return: {dxy_ret:.3f}% (inverse tilt)")

    if gold_ret is not None:
        score += (-np.sign(gold_ret)) * 0.25  # gold up slightly risk-off tilt
        evidence.append(f"Gold return: {gold_ret:.3f}% (weak inverse tilt)")

    if us10_ret is not None:
        evidence.append(f"US10Y change proxy (ret_pct): {us10_ret:.3f}% (context only)")

    if score > 0.5:
        label = "Risk-on (provisional)"
    elif score < -0.5:
        label = "Risk-off (provisional)"
    else:
        label = "Mixed / unclear (provisional)"

    return {
        "label": label,
        "score": float(score),
        "evidence": evidence,
        "eq_mean_ret": eq_mean,
        "vix_ret": vix_ret,
        "usdkrw_ret": usdkrw_ret,
        "dxy_ret": dxy_ret,
        "gold_ret": gold_ret,
        "us10_ret": us10_ret,
    }

def save_holiday_markdown(out_dir: str, target_date: str, reason: str = "휴장") -> str:
    """
    Write a minimal markdown file stating the market is closed for the date.
    This is used when we decide not to generate any charts/artifacts.
    """
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"daily_report_{target_date.replace('-', '')}.md")

    lines = [
        f"# Daily Market Report — {target_date}",
        "",
        "## Status",
        f"- {reason}",
        "",
        "## Notes",
        "- Data was not available for the target date; no figures were generated.",
        "",
    ]
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return out_path

def save_llm_markdown_report(
    df_metrics: pd.DataFrame,
    out_dir: str,
    target_date: str,
    k: int = 3,
) -> str:
    """
    Save an LLM-friendly Markdown report into the same folder as figures.

    What makes it LLM-friendly
    --------------------------
    - Clear sections with explicit tasks:
      * Summary bullets
      * Top/Bottom performers
      * Volatility leaders
      * Risk regime inference + evidence
      * Raw table (for grounding)
    - Minimal noise:
      * numeric rounding
      * stable column order
    - Self-contained:
      * includes metric definitions and assumptions

    Parameters
    ----------
    df_metrics : pd.DataFrame
        Output of add_daily_metrics().
    out_dir : str
        Output folder (same as figs).
    target_date : str
        Report date.
    k : int
        Top/bottom count for leaderboards.

    Returns
    -------
    str
        Full path to the created markdown file.
    """
    os.makedirs(out_dir, exist_ok=True)

    d = df_metrics.replace([np.inf, -np.inf], np.nan).copy()

    # Stable column order for downstream parsing
    preferred_cols = [
        "stock", "date", "Open", "High", "Low", "Close", "Volume",
        "ret_pct", "range_pct", "close_over_open", "candle_dir",
    ]
    cols = [c for c in preferred_cols if c in d.columns] + [c for c in d.columns if c not in preferred_cols]
    d = d[cols]

    # Round numeric fields to reduce textual noise
    num_cols = d.select_dtypes(include=[np.number]).columns
    d[num_cols] = d[num_cols].round(6)

    # Leaderboards
    top_ret, bot_ret = _safe_top_bottom(d, "ret_pct", k=k)
    top_rng, _ = _safe_top_bottom(d, "range_pct", k=k)

    # Risk regime heuristic
    regime = infer_risk_regime(d)

    # Build markdown
    lines: List[str] = []
    lines.append(f"# Daily Market Report (LLM-ready) — {target_date}")
    lines.append("")
    lines.append("## How to use this file (for an LLM)")
    lines.append("- Summarize today's market in 5–8 bullet points.")
    lines.append("- Identify the biggest winners/losers and possible drivers.")
    lines.append("- Comment on volatility (intraday range) and risk regime.")
    lines.append("- Use the **Raw table** section for grounding and quoting numbers.")
    lines.append("")
    lines.append("## Metric definitions")
    lines.append("- **ret_pct**: (Close - Open) / Open * 100")
    lines.append("- **range_pct**: (High - Low) / Open * 100")
    lines.append("- **close_over_open**: Close / Open")
    lines.append("- **candle_dir**: sign(Close - Open) → +1(up), 0(flat), -1(down)")
    lines.append("")
    lines.append("## Executive summary (auto)")
    if not top_ret.empty:
        best = top_ret.iloc[0]
        worst = bot_ret.iloc[0] if not bot_ret.empty else None
        lines.append(f"- Best performer: **{best['stock']}** ({best['ret_pct']:.3f}%)")
        if worst is not None:
            lines.append(f"- Worst performer: **{worst['stock']}** ({worst['ret_pct']:.3f}%)")
    if not top_rng.empty:
        vr = top_rng.iloc[0]
        lines.append(f"- Highest intraday range: **{vr['stock']}** ({vr['range_pct']:.3f}%)")
    lines.append(f"- Risk regime inference: **{regime['label']}** (score={regime['score']:.2f})")
    if regime["evidence"]:
        lines.append("  - Evidence:")
        for ev in regime["evidence"]:
            lines.append(f"    - {ev}")
    lines.append("")
    lines.append("## Leaderboards")
    lines.append(f"### Top {k} daily returns (ret_pct)")
    lines.append(top_ret[["stock", "ret_pct"]].to_markdown(index=False) if not top_ret.empty else "_No data_")
    lines.append("")
    lines.append(f"### Bottom {k} daily returns (ret_pct)")
    lines.append(bot_ret[["stock", "ret_pct"]].to_markdown(index=False) if not bot_ret.empty else "_No data_")
    lines.append("")
    lines.append(f"### Top {k} intraday ranges (range_pct)")
    lines.append(top_rng[["stock", "range_pct"]].to_markdown(index=False) if not top_rng.empty else "_No data_")
    lines.append("")
    lines.append("## Notes / caveats")
    lines.append("- Risk regime is a heuristic signal. Treat it as a starting point for narrative, not a definitive classifier.")
    lines.append("- Some assets may have missing/zero Volume; volume-based interpretation may be limited.")
    lines.append("- FX/yield series may have different market conventions; interpret ret_pct carefully.")
    lines.append("")
    lines.append("## Raw table (ground truth)")
    lines.append(d.to_markdown(index=False))
    lines.append("")

    out_path = os.path.join(out_dir, f"daily_report_{target_date.replace('-', '')}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    # Build markdown for d of raw data table
    lines: List[str] = []
    lines.append("# Market Overview")
    lines.append(d.to_markdown(index=False))
    lines.append("")
    
    out_path = os.path.join(out_dir, f"market_overview_{target_date.replace('-', '')}_for_users.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    return out_path


# =============================================================================
# 4) Visualization Layer
# =============================================================================
def plot_daily_return_bar(dfm: pd.DataFrame, title: Optional[str] = None) -> plt.Figure:
    """
    Horizontal bar chart of daily returns.

    Interpretation guide
    --------------------
    - Bars > 0: the asset closed above its open (positive day)
    - Bars < 0: the asset closed below its open (negative day)
    - Sorting makes it easy to see winners/losers at a glance.

    Typical placement in a report:
    - Page 1: top-left as the "performance scoreboard".
    """
    d = dfm.sort_values("ret_pct", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(d["stock"], d["ret_pct"])
    ax.axvline(0, linewidth=1)
    ax.set_xlabel("Daily return (%)")
    ax.set_ylabel("Asset")
    ax.set_title(title or f"Daily Return by Asset ({d['date'].iloc[0]})")
    ax.grid(axis="x", alpha=0.2)
    fig.tight_layout()
    return fig


def plot_intraday_range_bar(dfm: pd.DataFrame, title: Optional[str] = None) -> plt.Figure:
    """
    Horizontal bar chart of intraday range (High-Low) normalized by Open.

    Interpretation guide
    --------------------
    - Larger values imply larger intraday movement; often correlated with risk,
      uncertainty, macro events, or liquidity conditions.
    - This metric does not indicate direction; it measures amplitude.

    Typical placement:
    - Near volatility/risk section, alongside VIX or rates.
    """
    d = dfm.sort_values("range_pct", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(d["stock"], d["range_pct"])
    ax.set_xlabel("Intraday range (High-Low) / Open (%)")
    ax.set_ylabel("Asset")
    ax.set_title(title or f"Intraday Range by Asset ({d['date'].iloc[0]})")
    ax.grid(axis="x", alpha=0.2)
    fig.tight_layout()
    return fig

def plot_candlestick_subplots(
    dfm: pd.DataFrame,
    stocks: List[str],
    out_dir: str,
    filename: str = "AllStocks_Subplots.png",
):
    """
    Draw one-day candlesticks for multiple stocks,
    each in its own subplot, and save as a single PNG.

    Parameters
    ----------
    dfm : pd.DataFrame
        Must contain columns: ['date','stock','Open','Close','High','Low']
    stocks : List[str]
        List of stock tickers to plot
    out_dir : str
        Output directory
    filename : str
        Output filename (default: AllStocks_Subplots.png)
    """
    n = len(stocks)
    fig, axes = plt.subplots(1, n, figsize=(3*n, 5), sharey=False)

    # axes가 하나일 경우 리스트로 변환
    if n == 1:
        axes = [axes]

    for ax, stock in zip(axes, stocks):
        d = dfm[dfm["stock"] == stock].iloc[0]  # 하루치 데이터만 있다고 가정
        body_bottom = min(d["Open"], d["Close"])
        body_top = max(d["Open"], d["Close"])
        color = "blue" if d["Open"] > d["Close"] else "red"

        # Wick
        ax.vlines(0, d["Low"], d["High"], linewidth=1, color=color)
        # Body
        ax.bar(0, body_top - body_bottom, bottom=body_bottom, width=0.6, color=color)

        ax.set_xticks([0])
        ax.set_xticklabels([stock])
        ax.set_ylabel("Price")
        ax.set_title(f"{stock} ({d['date']})")
        ax.grid(axis="y", alpha=0.2)

    fig.tight_layout()
    os.makedirs(out_dir, exist_ok=True)
    fig.savefig(os.path.join(out_dir, filename), dpi=150)
    plt.close(fig)

def plot_volume_vs_return_scatter(dfm: pd.DataFrame, title: Optional[str] = None) -> plt.Figure:
    """
    Scatter plot: Volume vs daily return.

    Why it exists
    -------------
    - Helps judge whether price movement was accompanied by participation/activity.
    - High return with low volume may be less "confirmed" than high return with high volume.

    Implementation notes
    --------------------
    - We filter Volume > 0 because many macro series will have Volume==0 or NaN.
    - We use log scale on x-axis because volume spans many orders of magnitude.
    """
    d = dfm.copy()
    d["Volume"] = pd.to_numeric(d["Volume"], errors="coerce")
    d = d[(d["Volume"].notna()) & (d["Volume"] > 0)].copy()

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(d["Volume"], d["ret_pct"])
    ax.set_xscale("log")
    ax.axhline(0, linewidth=1)
    ax.set_xlabel("Volume (log scale)")
    ax.set_ylabel("Daily return (%)")
    ax.set_title(title or f"Volume vs Return ({dfm['date'].iloc[0]})")
    ax.grid(alpha=0.2)

    for _, r in d.iterrows():
        ax.annotate(
            str(r["stock"]),
            (r["Volume"], r["ret_pct"]),
            fontsize=9,
            xytext=(4, 4),
            textcoords="offset points",
        )

    fig.tight_layout()
    return fig

# =============================================================================
# 5) Holiday detection
# =============================================================================
def is_holiday_or_closed(df_indices: pd.DataFrame, focus_assets: List[str], min_focus_hits: int = 1) -> bool:
    """
    Decide whether to treat the date as "closed" and exit without charts.

    Logic (practical, robust):
    - If we cannot retrieve at least `min_focus_hits` assets among `focus_assets`,
      we consider it "closed" (or data unavailable) and do not generate charts.

    Why:
    - Weekends/holidays: most equity indices return no data.
    - Data outages: behaves similarly; user asked to stop and write "휴장".

    Tuning:
    - If you want stricter, set min_focus_hits=2 or 3.
    """
    if df_indices.empty:
        return True
    hits = df_indices[df_indices["stock"].isin(focus_assets)].shape[0]
    return hits < min_focus_hits

# =============================================================================
# 6) CLI / Main Entrypoint
# =============================================================================
def parse_args() -> argparse.Namespace:
    """
    CLI arguments for the daily report generator.

    Required
    --------
    --date:
        Report date as YYYY-MM-DD

    Optional
    --------
    --outdir:
        Base directory for output artifacts.
        Output artifacts include:
        - PNG figures
        - LLM-ready markdown report
    """
    parser = argparse.ArgumentParser(description="Generate daily market report figures + LLM-ready markdown.")
    parser.add_argument(
        "--date",
        required=True,
        help="Target date in YYYY-MM-DD (e.g., 2025-12-24)",
    )
    parser.add_argument(
        "--outdir",
        default="./figs",
        help="Base output directory (default: ./figs)",
    )
    return parser.parse_args()


def main() -> None:
    """
    End-to-end daily report pipeline.

    Pipeline overview
    -----------------
    1) Parse args and build output folder: {outdir}/{YYYYMMDD}/
    2) Collect OHLCV for configured assets from FinanceDataReader
    3) Compute daily metrics (return, range, etc.)
    4) Save an LLM-ready markdown report to the same folder
    5) Generate and save figures (PNG) to the same folder

    Failure modes and behavior
    --------------------------
    - If the date is a weekend/holiday for most assets, the output may be empty
      and we raise an error early to avoid writing misleading artifacts.
    - Missing symbols are skipped with warnings.
    """
    args = parse_args()
    target_date = args.date

    folder_name = target_date.replace("-", "")
    out_dir = os.path.join(args.outdir, folder_name)
    os.makedirs(out_dir, exist_ok=True)

    symbol_map: Dict[str, str] = {
        "NASDAQ": "IXIC",
        "S&P500": "US500",
        "DOWJONES": "DJI",
        "RUSSELL2000": "RUT",
        "USD/KRW": "USD/KRW",
        "Dallor Index/USD": "DX-Y.NYB",
        "GOLD": "GC=F",
        "BITCOIN": "BTC/USD",
        # "VIX": "VIX",
        "US5YT": "US5YT",
        "US10YT": "US10YT",
        "US30YT": "US30YT",
    }

    focus_list: List[str] = ["NASDAQ", "S&P500", "DOWJONES", "RUSSELL2000", "BITCOIN"]

    # 1) Collect OHLCV rows
    df_indices = collect_indices(target_date, symbol_map)
    if df_indices.empty:
        raise RuntimeError(f"No data collected for date={target_date}. (Weekend/holiday or symbol issues)")

    # 2) If holiday/closed -> write markdown and exit (no charts)
    if is_holiday_or_closed(df_indices, focus_assets=focus_list, min_focus_hits=3):
        md_path = save_holiday_markdown(out_dir=out_dir, target_date=target_date, reason="휴장")
        print(f"[CLOSED] {target_date} appears closed or data unavailable. Wrote: {md_path}")
        return

    # 3) Add derived metrics
    df = add_daily_metrics(df_indices)

    # 4) Save LLM-ready markdown (same folder as figures)
    md_path = save_llm_markdown_report(df, out_dir=out_dir, target_date=target_date, k=3)
    print(f"[OK] Saved LLM-ready markdown report: {md_path}")

    # 5) Candlesticks (one asset per file)
    plot_candlestick_subplots(df, focus_list, out_dir)

    # 6) Daily return bar
    exclude = {"VIX", "Dallor Index/USD", "USD/KRW"}
    df_return = df[~df["stock"].isin(exclude)].copy()
    fig = plot_daily_return_bar(df_return)
    fig.savefig(os.path.join(out_dir, "DailyReturn.png"), dpi=150)
    plt.close(fig)

    # 7) Intraday range bar (focus assets)
    df_range = df[df["stock"].isin(focus_list)].copy()
    fig = plot_intraday_range_bar(df_range)
    fig.savefig(os.path.join(out_dir, "IntradayRange.png"), dpi=150)
    plt.close(fig)

    # 8) Volume vs return (only if Volume exists)
    df_vol = df[df["stock"].isin(focus_list)].copy()
    if (pd.to_numeric(df_vol["Volume"], errors="coerce") > 0).any():
        fig = plot_volume_vs_return_scatter(df_vol)
        fig.savefig(os.path.join(out_dir, "volume_vs_return.png"), dpi=150)
        plt.close(fig)
    else:
        print("[INFO] No Volume>0 rows found; skipping volume_vs_return plot.")

    print(f"[DONE] All outputs saved to: {out_dir}")


if __name__ == "__main__":
    main()
