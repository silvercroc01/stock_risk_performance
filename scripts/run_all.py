import os

os.system("python scripts/fetch_data.py")
os.system("python scripts/compute_returns.py")
os.system("python scripts/compute_metrics.py")
os.system("python scripts/plot_metrics.py")
os.system("python scripts/generate_report.py")
os.system("python scripts/portfolio_optimization.py")
print("All steps completed! Check the reports/ folder.")
print("Running streamlit dashboard")
os.system("streamlit run scripts/dashboard.py")
