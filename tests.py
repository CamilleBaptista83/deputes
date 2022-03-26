import pytest
import requests
from app import create_app


@pytest.fixture
def app():
    appli = create_app()
    yield appli


@pytest.fixture()
def client(app):
    return app.test_client()


def test_ws_response():
    response = requests.get('https://www.nosdeputes.fr/synthese/data/json')
    assert response.status_code == 200


def test_ws_key_exist():
    response = requests.get('https://www.nosdeputes.fr/synthese/data/json')
    assert "deputes" in response.json()


def test_home_response(client):
    response = client.get('/')
    assert response.status_code == 200


def test_groupe_politique_response(client):
    response = client.get('/groupe-politique')
    assert response.status_code == 200