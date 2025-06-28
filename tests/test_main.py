from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

def test_hello():
    response = client.get("/hello/Nathan")
    assert response.status_code == 200
    assert response.json() == {"message": "Bonjour, Nathan !"}

def test_add():
    response = client.post("/add", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_reverse():
    response = client.post("/reverse", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json() == {"reversed": "olleh"}
