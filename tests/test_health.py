from fastapi.testclient import TestClient
from api.main import app

# tests/test_health.py
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health():
    r = client.get("/healthz")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert "correlation_id" in body

def test_echo_with_headers():
    r = client.post(
        "/echo",
        json={"message": "hi"},
        headers={
            "X-Idempotency-Key": "demo-123",
            "X-Correlation-Id": "demo-corr",
            "Content-Type": "application/json",
        },
    )
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["idempotency_key"] == "demo-123"
    assert body["correlation_id"] == "demo-corr"
    assert body["data"]["message"] == "hi"
