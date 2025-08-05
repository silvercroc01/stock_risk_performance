import pandas as pd
import matplotlib.pyplot as plt

metrics = pd.read_csv('data/sector_metrics.csv', index_col=0)

sectors = metrics.drop('SPY')

# use plt.show() only when in gui or interactive interface like notebook

# plotting the Volatility
plt.figure(figsize=(10, 5))
sectors['Volatility'].plot(kind='bar', color='skyblue')
plt.title('Annualized Volatility by Sector')
plt.ylabel('Volatility')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/volatility_by_sector.png')
# plt.show()

# plotting the sharpe Ratio
plt.figure(figsize=(10, 5))
sectors['Sharpe'].plot(kind='bar', color='green')
plt.title('Sharpe Ratio by Sector')
plt.ylabel('Sharpe Ratio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/sharpe_by_sector.png')
# plt.show()

# max dropdown

plt.figure(figsize=(10, 5))
sectors['MaxDrawdown'].plot(kind='bar', color='red')
plt.title('Max Drawdown by Sector')
plt.ylabel('Max Drawdown')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/maxdrawdown_by_sector.png')
# plt.show()

# plotting beta

plt.figure(figsize=(10, 5))
sectors['Beta'].plot(kind='bar', color='orange')
plt.title('Beta vs S&P 500 by Sector')
plt.ylabel('Beta')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/beta_by_sector.png')
# plt.show()

# sector performance over time

prices = pd.read_csv('data/sector_prices.csv', index_col=0, parse_dates=True)
prices.plot(figsize=(12, 6), title="Sector ETF Prices Over Time")
plt.ylabel("Price")
plt.savefig('reports/performance_over_time.png')
# plt.show()
