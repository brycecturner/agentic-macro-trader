import yfinance as yf
import numpy as np
import pandas as pd
import logging
import json

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_portfolio_prices_and_value(
    portfolio: dict,
    start: str = "2024-01-01",
    end: str = None
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Fetches daily prices for portfolio assets and computes:
        - Latest snapshot (ticker, name, weight, price, rationale)
        - Daily portfolio value, daily return, and cumulative return

    Args:
        portfolio (dict): Portfolio schema containing 'assets' and their weights.
        start (str): Start date for fetching price history (YYYY-MM-DD).
        end (str, optional): End date (defaults to today).

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]:
            latest_df: Latest snapshot with weights, price, and rationale
            portfolio_value_df: Daily portfolio value, daily return, cumulative return
    """
    assets = portfolio.get("schema", {}).get("properties", {}).get("assets", [])
    if not assets:
        raise ValueError("No assets found in portfolio schema.")

    tickers = [asset["ticker"] for asset in assets]
    weights = {asset["ticker"]: asset["weight"] for asset in assets}

    logger.info(f"Fetching daily prices for {len(tickers)} tickers: {tickers}")
    data = yf.download(tickers=tickers, start=start, end=end, interval="1d", progress=False)["Close"]

    # Handle single-ticker case
    if isinstance(data, pd.Series):
        data = data.to_frame(name=tickers[0])

    # Forward-fill missing values and enforce daily continuity
    data = data.ffill()
    full_range = pd.date_range(start=data.index.min(), end=data.index.max(), freq="D")
    data = data.reindex(full_range).ffill()
    data.index.name = "Date"

    # Normalize and compute weighted portfolio value
    normalized = data / data.iloc[0]
    weighted = normalized.mul(pd.Series(weights))
    portfolio_value = weighted.sum(axis=1) * 100  # Base 100

    # Compute returns
    daily_returns = portfolio_value.pct_change().fillna(0)
    cumulative_returns = (1 + daily_returns).cumprod() - 1

    portfolio_value_df = pd.DataFrame({
        "Date": portfolio_value.index,
        "Portfolio_Value": portfolio_value.values,
        "Daily_Return": daily_returns.values,
        "Cumulative_Return": cumulative_returns.values
    }).set_index("Date")

    # Latest snapshot
    latest_prices = data.iloc[-1]
    latest_df = pd.DataFrame([
        {
            "Ticker": asset["ticker"],
            "Name": asset.get("ticker_name", ""),
            "Weight": asset.get("weight", None),
            "Latest_Price": latest_prices.get(asset["ticker"]),
            "Rationale": asset.get("rationale", "")
        }
        for asset in assets
    ])

    logger.info("Fetched full daily price series and computed portfolio returns.")
    return latest_df, portfolio_value_df


def calculate_sharpe_ratio(
    portfolio_df: pd.DataFrame,
    risk_free_rate: float | None = None,
    start: str | None = None,
    end: str | None = None,
    sp500_ticker: str = "^GSPC"
) -> float:
    """
    Calculates the annualized Sharpe ratio for a portfolio.
    
    Args:
        portfolio_df (pd.DataFrame): Must contain a 'Daily_Return' column.
        risk_free_rate (float | None): Annual risk-free rate (e.g., 0.04 for 4%).
            If None, will fetch the S&P 500 and use its daily returns as the benchmark.
        start (str, optional): Start date for S&P 500 data if fetched.
        end (str, optional): End date for S&P 500 data if fetched.
        sp500_ticker (str): Ticker for S&P 500 index (^GSPC by default).

    Returns:
        float: The annualized Sharpe ratio.
    """
    if "Daily_Return" not in portfolio_df.columns:
        raise ValueError("portfolio_df must contain a 'Daily_Return' column.")

    daily_returns = portfolio_df["Daily_Return"].dropna()

    # Determine risk-free returns
    if risk_free_rate is not None:
        # Convert annual rate to daily equivalent (approximation)
        rf_daily = (1 + risk_free_rate) ** (1/252) - 1
        excess_returns = daily_returns - rf_daily
        logger.info(f"Using constant risk-free rate: {risk_free_rate*100:.2f}% annually.")
    else:
        # Fetch S&P 500 as proxy
        logger.info(f"Fetching S&P 500 returns ({sp500_ticker}) as risk-free proxy...")
        sp500 = yf.download(sp500_ticker, start=start, end=end, interval="1d", progress=False)["Close"]
        sp500_returns = sp500.pct_change().reindex(daily_returns.index).fillna(0)
        excess_returns = daily_returns - sp500_returns.mean()
        logger.info("Using S&P 500 mean daily return as risk-free proxy.")

    # Compute daily Sharpe ratio components
    mean_excess = np.mean(excess_returns)
    std_excess = np.std(excess_returns, ddof=1)

    if std_excess == 0:
        logger.warning("Standard deviation of returns is zero; Sharpe ratio undefined.")
        return np.nan

    sharpe_ratio = (mean_excess / std_excess) * np.sqrt(252)  # Annualized
    logger.info(f"Calculated Sharpe ratio: {sharpe_ratio:.3f}")

    return sharpe_ratio

def test():
    # Example portfolio
    with open("results/portfolio.json", "r") as f:
        portfolio = json.load(f)

    latest_df, portfolio_value_df = get_portfolio_prices_and_value(portfolio, start="2023-01-01")
    print("Latest Portfolio Snapshot:")
    print(latest_df)

    print("\nPortfolio Value Over Time:")
    print(portfolio_value_df)

    sharpe_ratio = calculate_sharpe_ratio(portfolio_value_df, risk_free_rate=0.03)
    print(f"\nPortfolio Sharpe Ratio: {sharpe_ratio:.3f}")

test()
