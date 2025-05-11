from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os

RAW_PATH = os.path.abspath("airflow/data/raw/raw_data.csv")
CLEANED_PATH = os.path.abspath("airflow/data/processed/cleaned_data.csv")

def ingest_data():
    # Download a sample CSV from URL
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
    df = pd.read_csv(url)
    os.makedirs(os.path.dirname(RAW_PATH), exist_ok=True)
    df.to_csv(RAW_PATH, index=False)
    print(f"Data ingested to {RAW_PATH}")

def clean_data():
    df = pd.read_csv(RAW_PATH)
    df.dropna(inplace=True)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    os.makedirs(os.path.dirname(CLEANED_PATH), exist_ok=True)
    df.to_csv(CLEANED_PATH, index=False)
    print(f"Cleaned data saved to {CLEANED_PATH}")

with DAG(
    dag_id="etl_pipeline",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["etl", "demo"]
) as dag:

    ingest = PythonOperator(
        task_id="ingest_data",
        python_callable=ingest_data
    )

    clean = PythonOperator(
        task_id="clean_data",
        python_callable=clean_data
    )

    ingest >> clean
