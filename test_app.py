import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    """Test del endpoint principal"""
    response = client.get('/')
    assert response.status_code == 200
    # Debe contener Dashboard o NeonPanel
    assert b'Dashboard' in response.data or b'NeonPanel' in response.data


def test_support_get(client):
    """Test que el formulario de soporte se carga correctamente"""
    response = client.get('/support')
    assert response.status_code == 200
    assert b'Soporte' in response.data


def test_support_post(client):
    """Test del envío de formulario"""
    response = client.post('/support', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'message': 'Test message'
    }, follow_redirects=True)

    assert response.status_code == 200
    # Después del POST debe volver al formulario
    assert b'Soporte' in response.data
