
```
# S&P 500 Sector Performance & Risk Analysis

A Python project to analyze and visualize risk and performance metrics for S&P 500 sector ETFs.  
This project automates data collection, risk metric calculation, visualization, and reporting—making it easy to monitor sector risk and performance over time.
```
```
```

---
## Features

- **Automated data download** for S&P 500 sector ETFs using yfinance.
- **Calculation of key risk metrics** for each sector:
  - Volatility (annualized)
  - Sharpe Ratio (annualized, risk-free rate = 0)
  - Max Drawdown
  - Beta (vs. S&P 500)
  - CAGR (Compound Annual Growth Rate)
  - Sortino Ratio
- **Bar chart visualizations** for all metrics.
- **Markdown report generation** with embedded tables and charts.
- **One-click automation**: Run the entire pipeline with `run_all.py`.

---

##  How to Run

1. **Clone the repo and set up a virtual environment:**
    ```bash
    git clone <your-repo-url>
    cd sp500-sector-risk
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. **Run the full pipeline:**
    ```bash
    python run_all.py
    ```

3. **View your results:**
    - Check the `reports/` folder for the latest markdown report and charts.


---
## Insights

- Sectors with higher volatility and max drawdown are riskier.
- Sharpe and Sortino ratios highlight sectors with better risk-adjusted returns.
- Beta shows which sectors are more/less sensitive to the overall market.

---

## Requirements

- Python 3.8+
- pandas, numpy, matplotlib, yfinance, seaborn

---

##  How to Present

- “This project automates the full risk analysis pipeline for S&P 500 sectors, from data collection to reporting.”
- “It provides clear, actionable insights for portfolio and risk management, and is easy to extend or automate.”

---
