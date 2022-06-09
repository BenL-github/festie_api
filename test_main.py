from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_state():
    response = client.post('/us_states', json = {'state_name':'Lousiana'})
    assert response.status_code == 201
    assert response.json() == {"Entry":"Lousiana"}

def test_get_states():
    response = client.get("/us_states")
    assert response.status_code == 200

def test_create_user():
    body = {"f_name": "Tina", 
            "l_name": "Belcher",
            "email": "tbelcher@gmail.com",
            "state_id": 1}
    response = client.post("/users", json = body)
    assert response.status_code == 201 
