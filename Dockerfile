FROM python:3.10-slim

WORKDIR /app

COPY requirements-prod.txt .
RUN pip install --no-cache-dir -r requirements-prod.txt

COPY mlflow/models/random_forest.pkl ./mlflow/models/
COPY app/main.py ./main.py

EXPOSE 5000
CMD ["python", "main.py"]
