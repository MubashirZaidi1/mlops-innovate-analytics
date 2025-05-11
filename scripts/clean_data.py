import pandas as pd
import os

RAW_PATH = "airflow/data/raw/raw_data.csv"
CLEANED_PATH = "airflow/data/processed/cleaned_data.csv"

def main():
    df = pd.read_csv(RAW_PATH)
    df.dropna(inplace=True)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    os.makedirs(os.path.dirname(CLEANED_PATH), exist_ok=True)
    df.to_csv(CLEANED_PATH, index=False)
    print(f"[DVC] Cleaned data saved to {CLEANED_PATH}")

if __name__ == "__main__":
    main()
