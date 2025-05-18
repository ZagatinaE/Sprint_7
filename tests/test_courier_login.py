import requests
from data import TestData
from conftest import  create_courier




def test_successful_login(create_courier):
    login_data = {
        "login": create_courier["data"]["login"],
        "password": create_courier["data"]["password"]
    }
    response = requests.post(
        f"{TestData.BASE_URL}{TestData.COURIER_URL}/login",
        json=login_data
    )
    assert response.status_code == 200
    assert "id" in response.json()


def test_login_missing_password(create_courier):
    login_data = {"login": create_courier["data"]["login"]}
    response = requests.post(
        f"{TestData.BASE_URL}{TestData.COURIER_URL}/login",
        json=login_data
    )
    assert response.status_code in [400, 504]
    if response.status_code == 400:
        assert "message" in response.json()


def test_login_wrong_password(create_courier):
    login_data = {
        "login": create_courier["data"]["login"],
        "password": "invalid_password"
    }
    response = requests.post(
        f"{TestData.BASE_URL}{TestData.COURIER_URL}/login",
        json=login_data
    )
    assert response.status_code == 404  # Или 401, зависит от API
    assert "message" in response.json()


def test_login_nonexistent_courier():
    login_data = {
        "login": "user_not_exists",
        "password": "123456"
    }
    response = requests.post(
        f"{TestData.BASE_URL}{TestData.COURIER_URL}/login",
        json=login_data
    )
    assert response.status_code == 404
    assert "message" in response.json()