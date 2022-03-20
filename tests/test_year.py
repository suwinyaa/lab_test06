from fastapi.testclient import TestClient
from datetime import date
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
    output = "Years not less than 0"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"msg": output}

def test_year_non_input():
    input = ""
    output = "Years not less than 0"
    response = client.get("/service/getage"+input)
    assert response.status_code == 200
    assert response.json() == {"msg": output}

def test_year_underflow_api():
    input = "-1"
    output = "Years not less than 0"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"msg": output}

def test_year_unable_calculate_api():
    input = date.today().year + 543 + 1
    output = "Unable to calculate"
    response = client.get("/service/getage?year="+str(input))
    assert response.status_code == 200
    assert response.json() == {"msg": output}

def test_year_error_empty():
    input = ""
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 422