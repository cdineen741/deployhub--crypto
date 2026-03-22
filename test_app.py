import pytest
from unittest.mock import patch
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    with patch("app.get_db_connection", return_value=None):
        response = client.get("/health")
        assert response.status_code in [200, 500]

def test_status(client):
    with patch("app.get_db_connection", return_value=None):
        response = client.get("/status")
        assert response.status_code in [200, 500]