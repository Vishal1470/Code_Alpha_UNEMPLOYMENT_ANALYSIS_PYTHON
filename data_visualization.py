# scripts/data_visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
import os

def visualize_trends(df):
    """Plot overall unemployment trends over time."""
    os.makedirs("reports/figures", exist_ok=True)
    plt.figure(figsize=(10, 5))
    sns.lineplot(x="date", y="unemployment_rate", data=df)
    plt.title("Unemployment Rate Over Time")
    plt.xlabel("Date")
    plt.ylabel("Unemployment Rate (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("reports/figures/unemployment_trend.png")
    plt.close()

def plot_seasonal_patterns(df):
    """Analyze seasonal patterns by month or quarter."""
    os.makedirs("reports/figures", exist_ok=True)
    if "date" in df.columns:
        df["month"] = df["date"].dt.month
        monthly_avg = df.groupby("month")["unemployment_rate"].mean()

        plt.figure(figsize=(8, 5))
        monthly_avg.plot(kind="bar", color="skyblue")
        plt.title("Average Unemployment Rate by Month")
        plt.xlabel("Month")
        plt.ylabel("Average Unemployment Rate (%)")
        plt.tight_layout()
        plt.savefig("reports/figures/seasonal_patterns.png")
        plt.close()
