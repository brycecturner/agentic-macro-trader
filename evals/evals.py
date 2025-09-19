import yfinance as yf
import pandas as pd

def fetch_historical_data(ticker, period="5y", interval="1d"):
    """
    Fetch historical market data for a given ticker using yfinance.
    
    Args:
        ticker (str): The ticker symbol to fetch data for.
        period (str): The period of data to fetch (e.g., "1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max").
        interval (str): The data interval (e.g., "1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo").
    
    Returns:
        pd.DataFrame: A DataFrame containing the historical market data.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period, interval=interval)
        return hist
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return pd.DataFrame()
    
def calc_max_drawdown(prices):
    """
    Calculate the maximum drawdown of a price series.
    
    Args:
        prices (pd.Series): A pandas Series of prices.
    
    Returns:
        float: The maximum drawdown as a decimal (e.g., 0.2 for 20%).
    """
    roll_max = prices.cummax()
    drawdown = (prices - roll_max) / roll_max
    max_dd = drawdown.min()
    return max_dd
