# scripts/covid_impact_analysis.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def covid_trend_analysis(df):
    """Compare unemployment before and after Covid-19."""
    os.makedirs("reports/figures", exist_ok=True)
    
    if "date" not in df.columns:
        print("❌ Date column missing; skipping Covid analysis.")
        return
    
    # Define Covid onset date properly as datetime
    covid_start = pd.Timestamp("2020-03-01")
    
    # Create a new column "period" for comparison
    df["period"] = df["date"].apply(lambda x: "Pre-Covid" if pd.notnull(x) and x < covid_start else "Post-Covid")
    
    # Plot unemployment before vs after Covid
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="period", y="unemployment_rate", data=df, palette="pastel")
    plt.title("Unemployment Rate Before vs After Covid-19")
    plt.xlabel("Period")
    plt.ylabel("Unemployment Rate (%)")
    plt.tight_layout()
    plt.savefig("reports/figures/covid_impact.png")
    plt.close()

    print("\n📊 Covid impact chart saved in 'reports/figures/covid_impact.png'")
