# MLOps Project for Innovate Analytics Inc.

A comprehensive MLOps pipeline that demonstrates the end-to-end machine learning lifecycle from data ingestion to model deployment.

## Project Overview

This project implements a complete MLOps workflow using modern tools and practices. It includes data ingestion, cleaning, model training, experiment tracking, continuous integration, containerization, and Kubernetes deployment.


### Components

- **Data Ingestion & ETL**: Apache Airflow
- **Data Version Control**: DVC
- **Model Training & Tracking**: MLflow
- **Model Serving**: Flask API
- **Containerization**: Docker
- **CI/CD**: GitHub Actions & Jenkins
- **Deployment**: Kubernetes

## Machine Learning Model

- **Algorithm**: Random Forest Classifier
- **Task**: Binary classification predicting if a person's height is > 66 inches based on height/weight data
- **Metrics**: Accuracy and F1 score (both achieved 1.0 on test data)
- **Parameters**: n_estimators=100, max_depth=5

## Project Structure

```
├── airflow/                   # Airflow DAGs and data
│   ├── dags/                  # ETL pipeline definition
│   └── data/                  # Raw and processed data
├── app/                       # Flask application for model serving
├── k8s/                       # Kubernetes deployment manifests
├── mlflow/                    # Model training scripts and artifacts
│   └── models/                # Serialized model files
├── scripts/                   # Utility scripts
└── tests/                     # Unit tests
```

## Getting Started

### Prerequisites

- Python 3.10+
- Docker and Docker Compose
- Kubernetes cluster (for deployment)
- DVC
- Airflow
- MLflow

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mlops-innovate-analytics
   ```

2. Set up virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements-dev.txt
   ```

### Running the Pipeline

1. **Data Ingestion and Cleaning**:
   ```
   # Start Airflow
   airflow standalone
   # Navigate to Airflow UI and trigger the etl_pipeline dag
   ```
   
2. **Train the Model**:
   ```
   python mlflow/train_model.py
   ```
   
3. **Run the API Locally**:
   ```
   python app/main.py
   ```

4. **Build and Run Docker Container**:
   ```
   docker build -t mlops-model:latest .
   docker run -p 5000:5000 mlops-model:latest
   ```

5. **Deploy to Kubernetes**:
   ```
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   ```

## API Usage

Make predictions using the REST API:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [68.22, 142.34]}'
```

## CI/CD Pipeline

The project includes:
1. **GitHub Actions** for linting and testing on the dev branch
2. **Jenkins** for building and pushing Docker images

## Data Versioning

Data is versioned using DVC. To pull the latest version:

```
dvc pull
```

To track changes after modifying the data:

```
dvc add airflow/data/raw/raw_data.csv
dvc push
```

## Experiment Tracking

MLflow is used for tracking model experiments. View the dashboard:

```
mlflow ui
```

## License

This project is licensed under the MIT License - see the [`LICENSE`](LICENSE) file for details.
