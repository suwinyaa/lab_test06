from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../lab_test06')        
from main import app

client = TestClient(app)

def test_year_get_api():
    input = "2540"
    output = 25
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}

def test_input_zero_api():
    input = "0"
    output = "Prohibited years less than 0"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"msg": output}





