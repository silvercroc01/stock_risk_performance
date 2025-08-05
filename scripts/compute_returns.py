import pandas as pd

# Load the price data
data = pd.read_csv('data/sector_prices.csv', index_col=0, parse_dates=True)

# Calculate daily returns (percentage change)
returns = data.pct_change().dropna()

# Save to CSV for later use
returns.to_csv('data/sector_returns.csv')
print("Saved sector_returns.csv in data/")
