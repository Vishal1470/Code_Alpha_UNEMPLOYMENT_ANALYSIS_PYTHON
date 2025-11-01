# main.py
import pandas as pd
from scripts.data_cleaning import load_and_clean_data
from scripts.data_visualization import visualize_trends, plot_seasonal_patterns
from scripts.covid_impact_analysis import covid_trend_analysis

def main():
    # Step 1: Load and Clean Data
    file_path = "dataset/unemployment_data.csv"
    df = load_and_clean_data(file_path)

    print("\n✅ Data loaded and cleaned successfully!")
    print(df.head())

    # Step 2: Visualize Unemployment Trends
    visualize_trends(df)

    # Step 3: Identify Seasonal Trends
    plot_seasonal_patterns(df)

    # Step 4: Analyze Covid-19 Impact
    covid_trend_analysis(df)

    print("\n📊 Analysis completed successfully! All plots saved in 'reports/figures/'")

if __name__ == "__main__":
    main()
