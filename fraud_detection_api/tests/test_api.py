import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Fraud Detection API is running"}

def test_prediction():
    """Test the prediction endpoint"""
    input_data = {"feature1": 1.5, "feature2": 2.3}  # Replace with actual feature names and test values
    response = client.post("/predict", json=input_data)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)  # Ensure the response is a JSON object
    assert "prediction" in response.json()  # Check for the expected key
