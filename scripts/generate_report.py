import pandas as pd
from datetime import datetime

metrics = pd.read_csv('data/sector_metrics.csv', index_col=0)

with open('reports/sector_risk_report.md', 'w') as f:
    f.write(f"# S&P 500 Sector Risk Analysis Report\n")
    f.write(f"**Date generated:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
    f.write("## Key Risk Metrics by Sector\n\n")
    f.write(metrics.to_markdown())
    f.write("\n\n")
    f.write("## Visualizations\n")
    f.write("![Volatility](volatility_by_sector.png)\n")
    f.write("![Sharpe Ratio](sharpe_by_sector.png)\n")
    f.write("![Max Drawdown](maxdrawdown_by_sector.png)\n")
    f.write("![Beta](beta_by_sector.png)\n")
    f.write("\n")
    f.write("## Insights\n")
    f.write("- Sectors with the highest volatility are typically more sensitive to market swings.\n")
    f.write("- Sectors with higher Sharpe ratios offer better risk-adjusted returns.\n")
    f.write("- Max drawdown highlights the worst historical loss for each sector.\n")
    f.write("- Beta shows which sectors are more/less correlated with the overall market (SPY).\n")
    f.write("\n")
    f.write("*More Insights*\n")

print("Saved sector_risk_report.md in reports/")
