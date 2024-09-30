from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_hand_history():
    response = client.get("/hand-history")
    assert response.status_code == 200
    
    response_data = response.json()
    for hand in response_data:
        assert "id" in hand
        assert "stack" in hand
        assert "setup" in hand
        assert "hole_cards" in hand
        assert "winnings" in hand
        assert "actions" in hand
