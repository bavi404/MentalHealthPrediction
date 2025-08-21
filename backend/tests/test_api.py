import os

os.environ.setdefault("MOCK_PREDICT", "true")

from fastapi.testclient import TestClient

from backend.app.main import create_app


def test_health():
    client = TestClient(create_app())
    r = client.get("/api/v1/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "ok"
    assert isinstance(data["model_loaded"], bool)


def test_meta():
    client = TestClient(create_app())
    r = client.get("/api/v1/meta")
    assert r.status_code == 200
    data = r.json()
    assert "feature_schema" in data and "example_payload" in data


def test_predict_mock():
    client = TestClient(create_app())
    r = client.post("/api/v1/predict", json={"inputs": ["I feel stressed"]})
    assert r.status_code == 200
    data = r.json()
    assert "predictions" in data
    assert len(data["predictions"]) == 1
    item = data["predictions"][0]
    assert "label" in item and "score" in item

