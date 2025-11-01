# scripts/data_cleaning.py

import pandas as pd

def load_and_clean_data(file_path):
    try:
        # ✅ Load dataset
        df = pd.read_csv(file_path)
        
        # ✅ Normalize column names (remove spaces, lowercase all)
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")
        print("\n🧾 Available columns in dataset:", list(df.columns))

        # ✅ Detect correct unemployment rate column automatically
        possible_cols = [c for c in df.columns if "unemployment" in c]
        if possible_cols:
            rate_col = possible_cols[0]
        else:
            raise ValueError("❌ No unemployment column found in dataset.")
        
        print(f"📊 Using column '{rate_col}' as unemployment rate.\n")

        # ✅ Clean up NaNs and parse dates
        df = df.dropna(subset=[rate_col])
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)
        else:
            print("⚠️ No date column found.")

        # ✅ Rename main columns for easier plotting
        df.rename(columns={rate_col: "unemployment_rate"}, inplace=True)

        print("✅ Data cleaned successfully — ready for analysis.\n")
        return df

    except Exception as e:
        print("❌ Error while loading/cleaning data:", e)
        return None
