import yfinance as yf
import pandas as pd

tickers = [
    'XLF', 'XLK', 'XLE', 'XLV', 'XLY', 'XLP', 'XLI', 'XLU', 'XLRE', 'XLB', 'SPY'
]

data = yf.download(tickers, start="2018-01-01")
print(data.head())
print(data.columns)
print("Is empty:", data.empty)

if data.empty:
    print("No data was downloaded. Check your internet connection or ticker symbols.")
    exit(1)

if isinstance(data.columns, pd.MultiIndex):
    if 'Adj Close' in data.columns.levels[0]:
        adj_close = data['Adj Close']
    elif 'Close' in data.columns.levels[0]:
        print("Warning: 'Adj Close' not found, using 'Close' instead.")
        adj_close = data['Close']
    else:
        print("Neither 'Adj Close' nor 'Close' found. Available:",
              data.columns.levels[0])
        exit(1)
else:
    if 'Adj Close' in data.columns:
        adj_close = data['Adj Close'].to_frame()
    elif 'Close' in data.columns:
        print("Warning: 'Adj Close' not found, using 'Close' instead.")
        adj_close = data['Close'].to_frame()
    else:
        print("Neither 'Adj Close' nor 'Close' found. Available:", data.columns)
        exit(1)

adj_close.to_csv('data/sector_prices.csv')
print("Saved sector_prices.csv in data/")
