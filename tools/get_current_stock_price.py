import yfinance as yf
from crewai.tools import tool

@tool("getTickerPrice")
def getTickerPrice(ticker: str) -> str:
    """Query yahoo finance api to get current or recent close price for a single stock ticker"""
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if not data.empty:
        price = data['Close'][0]
        return price
    else:
        raise ValueError(f"No price data found for ticker {ticker}")