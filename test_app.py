from fastapi.testclient import TestClient
from app import doble, app

client = TestClient(app)

def test_doble():
    assert doble(2) == 4
    assert doble(0) == 0
    assert doble(-3) == -6

def test_obtener_doble():
    response = client.get("/doble?numero=5")
    assert response.status_code == 200
    assert response.json() == {"resultado": 10}

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Taller CI/CD - Agustin Martinez"