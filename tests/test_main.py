import pytest
from app.main import app
# import numpy as np
import joblib
import os


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Test the home endpoint returns correct message"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'ML model server is running!' in response.data

def test_model_loading():
    """Test that the model file exists and can be loaded"""
    model_path = os.path.join("mlflow", "models", "random_forest.pkl")
    assert os.path.exists(model_path), "Model file not found"

    try:
        model = joblib.load(model_path)
        assert model is not None, "Model loaded successfully"
    except Exception as e:
        pytest.fail(f"Failed to load model: {str(e)}")
