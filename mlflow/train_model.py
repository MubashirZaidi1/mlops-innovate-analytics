import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import joblib
import os

# Load and clean dataset
df = pd.read_csv("airflow/data/processed/cleaned_data.csv")

# Rename columns for easier access
df.columns = ["index", "height_in", "weight_lb"]

# Drop index column
df = df.drop(columns=["index"])

# Create a binary target based on height
df["target"] = df["height_in"].apply(lambda x: 1 if x > 66 else 0)

# Define features and target
X = df[["height_in", "weight_lb"]]
y = df["target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Parameters
n_estimators = 100
max_depth = 5

with mlflow.start_run():

    # Train model
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    # Evaluate
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds)

    # Log with MLflow
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1_score", f1)

    # Save and log model
    os.makedirs("mlflow/models", exist_ok=True)
    model_path = "mlflow/models/random_forest.pkl"
    joblib.dump(model, model_path)
    mlflow.log_artifact(model_path)

    print(f"✅ Model trained and logged — Accuracy: {acc:.4f}, F1: {f1:.4f}")
