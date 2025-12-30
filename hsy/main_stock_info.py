import os
import argparse
import numpy as np
import pandas as pd
import FinanceDataReader as fdr
from typing import Dict, List, Optional
import matplotlib.pyplot as plt


# =============================================================================
# 1) Data Loading Layer
# =============================================================================
def load_stock_data(symbol: str, target_date: str) -> Optional[pd.Series]:
    """
    Fetches OHLCV data for a single `symbol` starting from `target_date`
    and returns the row corresponding to that date.

    Why we do this:
    - FinanceDataReader returns a time series DataFrame indexed by dates.
    - For a "daily report", we usually need the OHLCV values for a single day.
    - Some symbols may not have data on the target date (holiday, weekend,
      missing feed, delayed updates, etc.). In those cases we return None.

    Parameters
    ----------
    symbol : str
        FinanceDataReader symbol string (e.g., "IXIC", "US500", "BTC/USD").
    target_date : str
        Target date in "YYYY-MM-DD" format.

    Returns
    -------
    pd.Series or None
        If `target_date` exists in the returned DataFrame index, returns that
        day's row as a Series. Otherwise returns None.
    """
    try:
        df = fdr.DataReader(symbol, target_date)

        # FinanceDataReader index is often Timestamp. To avoid mismatch
        # between "YYYY-MM-DD" string and Timestamp, we compare as strings.
        idx_as_str = df.index.astype(str)

        if target_date in idx_as_str:
            # Extract the first matched row (should be unique for a daily index)
            row = df.loc[idx_as_str == target_date].iloc[0]
            return row
        else:
            print(f"[WARN] No data for target date / symbol={symbol} / date={target_date}")
            return None

    except KeyError as e:
        # Some symbols raise KeyError when the date is absent
        print(f"[WARN] KeyError (no data on that date) / symbol={symbol} / err={e}")
        return None

    except Exception as e:
        # Catch-all: networking issues, feed changes, transient errors, etc.
        print(f"[ERROR] Unexpected error / symbol={symbol} / err={e}")
        return None


def collect_indices(target_date: str, symbol_map: Dict[str, str]) -> pd.DataFrame:
    """
    Builds a unified daily OHLCV table across multiple assets.

    The output schema is intentionally "flat" and consistent across asset classes
    (equity indices, FX, commodities, crypto, yields), which makes downstream
    reporting logic simpler.

    Parameters
    ----------
    target_date : str
        Target date in "YYYY-MM-DD".
    symbol_map : Dict[str, str]
        Mapping from human-friendly asset name -> FinanceDataReader symbol.
        Example: {"NASDAQ": "IXIC", "BITCOIN": "BTC/USD"}

    Returns
    -------
    pd.DataFrame
        Columns: [stock, date, Open, High, Low, Close, Volume]
        One row per asset (when data exists).
    """
    results: List[dict] = []

    for name, symbol in symbol_map.items():
        data = load_stock_data(symbol, target_date)
        if data is None:
            # If missing, we just skip it and keep the pipeline robust.
            continue

        # Using .get() because some symbols may not provide every column
        # consistently, especially "Volume".
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
    Adds derived metrics commonly used in daily market reports.

    Added columns
    -------------
    ret_pct:
        Daily return (%) based on Open -> Close.
        ret_pct = (Close - Open) / Open * 100

    range_pct:
        Intraday range (%) normalized by Open.
        range_pct = (High - Low) / Open * 100

    close_over_open:
        Ratio (Close / Open). Useful for compact multiplicative comparisons.

    candle_dir:
        Direction of the candle:
        +1 if Close > Open
         0 if Close == Open
        -1 if Close < Open

    Notes
    -----
    - This function coerces OHLC columns into numeric, so upstream ingestion
      can be more permissive (strings, missing, etc.).
    - If Open is 0 or NaN (rare, but possible with faulty feeds),
      ret_pct / range_pct may become inf/NaN. That is preferable to silently
      hiding the issue.

    Returns
    -------
    pd.DataFrame
        Original columns plus the derived metrics.
    """
    out = df.copy()

    # Convert strings to numeric, invalid parsing -> NaN
    for col in ["Open", "High", "Low", "Close"]:
        out[col] = pd.to_numeric(out[col], errors="coerce")

    out["ret_pct"] = (out["Close"] - out["Open"]) / out["Open"] * 100.0
    out["range_pct"] = (out["High"] - out["Low"]) / out["Open"] * 100.0
    out["close_over_open"] = out["Close"] / out["Open"]
    out["candle_dir"] = np.sign(out["Close"] - out["Open"]).astype(int)

    return out


def save_metrics_markdown(df_metrics: pd.DataFrame, out_dir: str, target_date: str) -> str:
    """
    Saves the metrics dataframe into a Markdown report file so that an LLM
    (or any downstream text-based system) can ingest it easily.

    Design choices (LLM-friendly)
    -----------------------------
    - Includes a short header describing the table and metric definitions.
    - Writes a Markdown table using `DataFrame.to_markdown()` for readability.
    - Rounds numeric columns to a reasonable precision to reduce noise.

    Parameters
    ----------
    df_metrics : pd.DataFrame
        DataFrame produced by add_daily_metrics().
    out_dir : str
        Directory where figures are saved; the markdown file will be saved here too.
    target_date : str
        Target date string in "YYYY-MM-DD".

    Returns
    -------
    str
        Full path to the created markdown file.
    """
    os.makedirs(out_dir, exist_ok=True)

    # A copy for formatting only (avoid mutating the original df used for plots)
    d = df_metrics.copy()

    # Ensure consistent column order (if columns exist)
    preferred_cols = [
        "stock", "date", "Open", "High", "Low", "Close", "Volume",
        "ret_pct", "range_pct", "close_over_open", "candle_dir",
    ]
    cols = [c for c in preferred_cols if c in d.columns] + [c for c in d.columns if c not in preferred_cols]
    d = d[cols]

    # Round numeric columns for stable textual representation
    numeric_cols = d.select_dtypes(include=[np.number]).columns.tolist()
    d[numeric_cols] = d[numeric_cols].round(6)

    # Compose markdown text
    md_lines: List[str] = []
    md_lines.append(f"# Daily Market Metrics ({target_date})")
    md_lines.append("")
    md_lines.append("## What this file contains")
    md_lines.append("- This file is generated from the daily OHLCV table and derived metrics.")
    md_lines.append("- It is intended to be machine- and LLM-readable.")
    md_lines.append("")
    md_lines.append("## Metric definitions")
    md_lines.append("- **ret_pct**: (Close - Open) / Open * 100")
    md_lines.append("- **range_pct**: (High - Low) / Open * 100")
    md_lines.append("- **close_over_open**: Close / Open")
    md_lines.append("- **candle_dir**: sign(Close - Open) → +1(up), 0(flat), -1(down)")
    md_lines.append("")
    md_lines.append("## Table")
    md_lines.append(d.to_markdown(index=False))
    md_lines.append("")

    out_path = os.path.join(out_dir, f"metrics_{target_date.replace('-', '')}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    return out_path


# =============================================================================
# 3) Visualization Layer
# =============================================================================
def plot_daily_return_bar(dfm: pd.DataFrame, title: Optional[str] = None) -> plt.Figure:
    """
    Horizontal bar chart of daily returns.

    Interpretation:
    - Positive bars: assets closed above open (up day)
    - Negative bars: assets closed below open (down day)
    - Useful as the top-level "scoreboard" in a daily report.
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
    Horizontal bar chart of intraday range normalized by Open.

    Interpretation:
    - Higher values indicate larger intraday volatility / uncertainty.
    - This is direction-agnostic: both strong rallies and selloffs widen range.
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


def plot_candlestick_one_day(
    dfm: pd.DataFrame,
    stocks: List[str],
    title: Optional[str] = None,
) -> plt.Figure:
    """
    Draws a simple one-day candlestick chart for the requested `stocks`.

    Implementation notes:
    - We draw wicks via vlines (Low to High).
    - We draw bodies via bar rectangles (Open to Close).
    - Colors are set by condition:
        Open < Close -> blue (up candle)
        Open > Close -> red  (down candle)

    This is intentionally minimal (no external libs like mplfinance)
    to keep the deployment surface small.
    """
    d = dfm[dfm["stock"].isin(stocks)].copy()
    d["stock"] = pd.Categorical(d["stock"], categories=stocks, ordered=True)
    d = d.sort_values("stock")

    fig, ax = plt.subplots(figsize=(3, 5))
    x = np.arange(len(d))

    # wicks
    ax.vlines(x, d["Low"], d["High"], linewidth=1)

    # bodies
    body_bottom = np.minimum(d["Open"], d["Close"])
    body_top = np.maximum(d["Open"], d["Close"])

    colors = np.where(d["Open"] < d["Close"], "blue", "red")
    ax.bar(x, (body_top - body_bottom), bottom=body_bottom, width=0.6, color=colors)

    ax.set_xticks(x)
    ax.set_xticklabels(d["stock"], rotation=0)
    ax.set_ylabel("Price / Index Level")
    ax.set_title(title or f"1-day Candle ({d['date'].iloc[0]})")
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    return fig


def plot_volume_vs_return_scatter(dfm: pd.DataFrame, title: Optional[str] = None) -> plt.Figure:
    """
    Scatter plot: Volume (log scale) vs daily return (%).

    Purpose:
    - Helps assess whether a price move is accompanied by activity (volume).
    - For some indices / FX / yields, volume can be missing or meaningless;
      we filter to Volume > 0.

    Note:
    - Using log scale on volume since magnitudes vary heavily across assets.
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

    # Add labels for interpretability in small-N asset sets
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
# 4) CLI / Main Entrypoint
# =============================================================================
def parse_args() -> argparse.Namespace:
    """
    Parses CLI arguments.

    Required:
    - --date: the target date in YYYY-MM-DD format

    Optional:
    - --outdir: base directory for outputs (figures + markdown)
    """
    parser = argparse.ArgumentParser(description="Generate daily market report figures + metrics markdown.")
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

    Steps
    -----
    1) Read args (date, outdir)
    2) Collect OHLCV rows for the specified date across configured symbols
    3) Compute daily metrics (return, range, etc.)
    4) Save metrics as Markdown file (LLM-friendly)
    5) Generate figures and save to the same output folder
    """
    args = parse_args()
    target_date = args.date

    # Folder naming convention: YYYYMMDD for easy sorting and archiving
    folder_name = target_date.replace("-", "")
    out_dir = os.path.join(args.outdir, folder_name)
    os.makedirs(out_dir, exist_ok=True)

    # Map: report-friendly name -> FinanceDataReader symbol
    symbol_map: Dict[str, str] = {
        "NASDAQ": "IXIC",
        "S&P500": "US500",
        "DOWJONES": "DJI",
        "RUSSELL2000": "RUT",
        "USD/KRW": "USD/KRW",
        "Dallor Index/USD": "DX-Y.NYB",
        "GOLD": "GC=F",
        "BITCOIN": "BTC/USD",
        "VIX": "VIX",
        "US5YT": "US5YT",
        "US10YT": "US10YT",
        "US30YT": "US30YT",
    }

    # For candle and certain charts, we keep a smaller "focus list"
    stock_list: List[str] = ["NASDAQ", "S&P500", "DOWJONES", "RUSSELL2000", "BITCOIN"]

    # 1) Collect daily rows
    df_indices = collect_indices(target_date, symbol_map)
    if df_indices.empty:
        raise RuntimeError(f"No data collected for date={target_date}. Check symbols/date (weekend/holiday).")

    # 2) Compute metrics
    df = add_daily_metrics(df_indices)

    # 3) Save Markdown summary for LLM ingestion (same directory as figures)
    md_path = save_metrics_markdown(df, out_dir=out_dir, target_date=target_date)
    print(f"[OK] Saved metrics markdown: {md_path}")

    # 4) Candlestick figures (per asset)
    for stock in stock_list:
        fig = plot_candlestick_one_day(df, [stock])
        fig.savefig(os.path.join(out_dir, f"{stock}_OneDayCandles.png"), dpi=150)
        plt.close(fig)

    # 5) Daily return bar (exclude some series that can distort interpretation)
    #    - VIX: volatility index (not a "return asset" in same sense)
    #    - Dollar Index, USD/KRW: FX indices; include them if you want, but
    #      often daily report separates them from equity/commodity moves.
    exclude = {"VIX", "Dallor Index/USD", "USD/KRW"}
    df_return = df[~df["stock"].isin(exclude)].copy()
    fig = plot_daily_return_bar(df_return)
    fig.savefig(os.path.join(out_dir, "DailyReturn.png"), dpi=150)
    plt.close(fig)

    # 6) Intraday range bar (focus list only)
    df_range = df[df["stock"].isin(stock_list)].copy()
    fig = plot_intraday_range_bar(df_range)
    fig.savefig(os.path.join(out_dir, "IntradayRange.png"), dpi=150)
    plt.close(fig)

    # 7) Volume vs Return (only if volume exists and is meaningful)
    df_vol = df[df["stock"].isin(stock_list)].copy()
    if (pd.to_numeric(df_vol["Volume"], errors="coerce") > 0).any():
        fig = plot_volume_vs_return_scatter(df_vol)
        fig.savefig(os.path.join(out_dir, "volume_vs_return.png"), dpi=150)
        plt.close(fig)
    else:
        print("[INFO] No Volume>0 rows found; skipping volume_vs_return plot.")

    print(f"[DONE] All outputs saved to: {out_dir}")


if __name__ == "__main__":
    main()
