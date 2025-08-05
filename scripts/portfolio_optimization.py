import pandas as pd
import numpy as np
from scipy.optimize import minimize

returns = pd.read_csv('data/sector_returns.csv', index_col=0)
mean_returns = returns.mean()
cov_matrix = returns.cov()
num_assets = len(mean_returns)


def portfolio_volatility(weights):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))


constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
bounds = tuple((0, 1) for _ in range(num_assets))
init_guess = num_assets * [1. / num_assets,]

result = minimize(portfolio_volatility, init_guess,
                  bounds=bounds, constraints=constraints)
optimal_weights = result.x

sectors = mean_returns.index.tolist()
weights_df = pd.DataFrame({'Sector': sectors, 'Weight': optimal_weights})
weights_df.to_csv('data/optimal_weights.csv', index=False)
print("Saved optimal_weights.csv in data/")
