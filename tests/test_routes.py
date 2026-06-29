from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Healthcare ML API"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_risk_route_exists():
    response = client.post("/predict/risk", json={})
    # Expect validation error since body is required
    assert response.status_code in [200, 422]


def test_claim_route_exists():
    response = client.post("/predict/claim", json={})
    # Expect validation error since body is required
    assert response.status_code in [200, 422]


def test_monitoring_psi():
    response = client.get("/monitor/psi")
    assert response.status_code == 200