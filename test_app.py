import pytest
import json
from app import app
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test del endpoint principal"""
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert 'endpoints' in data

def test_health_endpoint(client):
    """Test del endpoint de salud"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_ai_endpoint(client):
    """Test del endpoint de IA"""
    os.environ['TESTING'] = 'true'
    response = client.post('/ai',
                          data=json.dumps({'prompt': 'Test prompt'}),
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'response' in data
    assert 'prompt' in data