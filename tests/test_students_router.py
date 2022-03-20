from urllib import response
from fastapi.testclient import TestClient
import sys
sys.path.insert(0, "../lab_test06")
from main import app
client = TestClient(app)

def test_post_insert(db):
    response = client.post(
        "/students/",
        json={
            "name": "string2",
            "description": "string",
            "completed": "true",
            "date": "string"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "string2"
    assert response.json()[0]["description"] == "string"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "string"

def test_put_update(db):
    response = client.put(
        "/students/6236b15b8fb7d9333de04f2c",
        json={
            "name": "string",
            "description": "string2",
            "completed": "true",
            "date": "string"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "string"
    assert response.json()[0]["description"] == "string2" 

def test_delete(db):
    response = client.delete(
        "/students/622ff7fb77d67697c3b248af"
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}