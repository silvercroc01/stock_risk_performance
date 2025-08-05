import pandas as pd
import numpy as np

returns = pd.read_csv('data/sector_returns.csv', index_col=0, parse_dates=True)
prices = pd.read_csv('data/sector_prices.csv', index_col=0, parse_dates=True)

vol = returns.std() * np.sqrt(252)

sharpe = returns.mean() / returns.std() * np.sqrt(252)


def max_drawdown(series):
    roll_max = series.cummax()
    drawdown = (series - roll_max) / roll_max
    return drawdown.min()


mdd = prices.apply(max_drawdown)

spy_ret = returns['SPY']
beta = returns.apply(lambda x: x.cov(spy_ret) / spy_ret.var())

metrics = pd.DataFrame({
    'Volatility': vol,
    'Sharpe': sharpe,
    'MaxDrawdown': mdd,
    'Beta': beta
})

# CAGR calculation
start = prices.iloc[0]
end = prices.iloc[-1]
years = (prices.index[-1] - prices.index[0]).days / 365.25
cagr = (end / start) ** (1 / years) - 1

# sortino ratio
downside = returns.copy()
downside[downside > 0] = 0
sortino = returns.mean() / downside.std() * np.sqrt(252)

# add to metrics DataFrame
metrics = pd.DataFrame({
    'CAGR': cagr,
    'Volatility': vol,
    'Sharpe': sharpe,
    'Sortino': sortino,
    'MaxDrawdown': mdd,
    'Beta': beta
})
metrics.to_csv('data/sector_metrics.csv')
print("Saved sector_metrics.csv in data/")
