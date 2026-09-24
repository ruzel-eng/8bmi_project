from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_calculate_bmi_success():
    response = client.get("/bmi?weight=70&height=1.75")
    assert response.status_code == 200
    assert response.json()["bmi"] == 22.86
