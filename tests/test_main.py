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


def test_predict_endpoint_valid_data(client):
    """Test predict endpoint with valid data"""
    # Create sample features (adjust size based on your model's expected input)
    sample_features = [1.0, 2.0, 3.0, 4.0]  # Adjust based on model input size

    response = client.post(
        '/predict',
        json={'features': sample_features},
        content_type='application/json'
    )

    assert response.status_code == 200
    data = response.get_json()
    assert 'prediction' in data
    assert isinstance(data['prediction'], int)


def test_predict_endpoint_invalid_data(client):
    """Test predict endpoint with invalid data"""
    # Test with missing features
    response = client.post(
        '/predict',
        json={},
        content_type='application/json'
    )
    assert response.status_code == 400

    # Test with invalid feature format
    response = client.post(
        '/predict',
        json={'features': 'invalid'},
        content_type='application/json'
    )
    assert response.status_code == 400


def test_predict_endpoint_wrong_feature_size(client):
    """Test predict endpoint with wrong feature size"""
    # Create features with wrong size (adjust based on your model's expected input)
    wrong_size_features = [1.0, 2.0]  # Smaller than expected

    response = client.post(
        '/predict',
        json={'features': wrong_size_features},
        content_type='application/json'
    )
    assert response.status_code == 400


def test_model_loading():
    """Test that the model file exists and can be loaded"""
    model_path = os.path.join("mlflow", "models", "random_forest.pkl")
    assert os.path.exists(model_path), "Model file not found"

    try:
        model = joblib.load(model_path)
        assert model is not None, "Model loaded successfully"
    except Exception as e:
        pytest.fail(f"Failed to load model: {str(e)}") 
