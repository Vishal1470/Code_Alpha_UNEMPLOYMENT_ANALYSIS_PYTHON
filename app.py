# app.py — Streamlit dashboard for Unemployment Analysis

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scripts.data_cleaning import load_and_clean_data

st.set_page_config(page_title="Unemployment Analysis", layout="wide")

st.title("📊 Unemployment Analysis Dashboard")

# ==========================================================
# Load and clean data
# ==========================================================
file_path = "dataset/unemployment_data.csv"
df = load_and_clean_data(file_path)

if df is None or df.empty:
    st.error("❌ Failed to load dataset.")
    st.stop()

# Normalize columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

st.write("### Data Preview")
st.dataframe(df.head())

# ==========================================================
# Filters
# ==========================================================
regions = ["All"] + sorted(df["region"].unique().tolist())
selected_region = st.selectbox("Select Region", regions)

if selected_region != "All":
    df = df[df["region"] == selected_region]

# ==========================================================
# Charts
# ==========================================================
col1, col2 = st.columns(2)

# Region-wise
with col1:
    st.subheader("🏙️ Top Regions by Average Unemployment Rate")
    region_avg = df.groupby("region")["unemployment_rate"].mean().sort_values(ascending=False).head(10)
    fig1, ax1 = plt.subplots()
    sns.barplot(y=region_avg.index, x=region_avg.values, hue=region_avg.index, palette="coolwarm", legend=False, ax=ax1)
    st.pyplot(fig1)

# Time-series
with col2:
    st.subheader("📅 Unemployment Trend Over Time")
    df_sorted = df.sort_values("date")
    fig2, ax2 = plt.subplots()
    sns.lineplot(x="date", y="unemployment_rate", data=df_sorted, ax=ax2, color="darkblue")
    st.pyplot(fig2)

# Area-wise
st.subheader("🏘️ Area-wise Employment Trend")
if "area" in df.columns:
    fig3, ax3 = plt.subplots()
    sns.boxplot(x="area", y="unemployment_rate", hue="area", data=df, palette="Set2", legend=False, ax=ax3)
    st.pyplot(fig3)
else:
    st.warning("⚠️ 'area' column not found in dataset.")
