import json


def test_alive(test_client):
    """Ensure the /ping route behaves correctly."""
    response = test_client.get("/wroom/ping")
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert "pong!" in data["message"]
    assert "success" in data["status"]
