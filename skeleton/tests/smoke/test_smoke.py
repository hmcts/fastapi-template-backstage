import os
import httpx

TEST_URL = os.environ.get("TEST_URL", "http://localhost:${{ values.http_port }}")


def test_service_is_healthy():
    response = httpx.get(f"{TEST_URL}/health/liveness")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}
