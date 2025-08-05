import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np

metrics = pd.read_csv('data/sector_metrics.csv', index_col=0)
prices = pd.read_csv('data/sector_prices.csv', index_col=0, parse_dates=True)
weights = pd.read_csv('data/optimal_weights.csv')

tickers = [
    'XLF', 'XLK', 'XLE', 'XLV', 'XLY', 'XLP', 'XLI', 'XLU', 'XLRE', 'XLB', 'SPY'
]


@st.cache_data(ttl=3600)  # Cache for 1 hour, so you don't hit Yahoo too often
def get_data():
    data = yf.download(tickers, start="2018-01-01")['Close']
    return data


st.title("S&P 500 Sector Risk Dashboard")

if st.button("Refresh Data (Live)"):
    st.cache_data.clear()  # Clear the cache to force a fresh download

data = get_data()
st.write("Latest data as of:", data.index[-1].date())
st.line_chart(data)

# calculate returns
returns = data.pct_change().dropna()

# calculate metrics
start = data.iloc[0]
end = data.iloc[-1]
years = (data.index[-1] - data.index[0]).days / 365.25
cagr = (end / start) ** (1 / years) - 1
vol = returns.std() * np.sqrt(252)
sharpe = returns.mean() / returns.std() * np.sqrt(252)
downside = returns.copy()
downside[downside > 0] = 0
sortino = returns.mean() / downside.std() * np.sqrt(252)


def max_drawdown(series):
    roll_max = series.cummax()
    drawdown = (series - roll_max) / roll_max
    return drawdown.min()


mdd = data.apply(max_drawdown)
spy_ret = returns['SPY']
beta = returns.apply(lambda x: x.cov(spy_ret) / spy_ret.var())

metrics = pd.DataFrame({
    'CAGR': cagr,
    'Volatility': vol,
    'Sharpe': sharpe,
    'Sortino': sortino,
    'MaxDrawdown': mdd,
    'Beta': beta
})

st.header("Risk Metrics Table")
st.dataframe(metrics)

# visualize metrics
for metric in ['CAGR', 'Volatility', 'Sharpe', 'Sortino', 'MaxDrawdown', 'Beta']:
    st.subheader(metric)
    fig, ax = plt.subplots()
    metrics.drop('SPY')[metric].plot(kind='bar', ax=ax)
    st.pyplot(fig)

st.header("Scenario Analysis")
drop = st.slider("Simulate a market drop (%)",
                 min_value=0, max_value=50, value=10)
sim_prices = prices * (1 - drop/100)
st.line_chart(sim_prices)

# optimal weights for minimum variance
st.header("Optimal Portfolio Weights (Minimum Variance)")
fig, ax = plt.subplots()
ax.bar(weights['Sector'], weights['Weight'], color='purple')
ax.set_ylabel("Weight")
ax.set_title("Optimal Sector Allocation")
plt.xticks(rotation=45)
st.pyplot(fig)

st.write("These weights show the recommended allocation to each sector to minimize overall portfolio risk based on historical data.")
