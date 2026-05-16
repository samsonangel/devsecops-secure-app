import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/api/v1/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_process_data_success(client):
    response = client.post('/api/v1/data', json={"input": "hello"})
    assert response.status_code == 200
    assert response.get_json()["processed"] == "HELLO"

def test_process_data_missing_input(client):
    response = client.post('/api/v1/data', json={})
    assert response.status_code == 400
    assert "error" in response.get_json()