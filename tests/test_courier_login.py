import requests
from data import TestData
from conftest import  create_courier, courier_data
import allure




class TestCourierLogin:

    @allure.title("Успешная авторизация курьера с корректными логином и паролем")
    def test_successful_login(self,create_courier):
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

    @allure.title("Ошибка 400 при отсутствии пароля")
    def test_login_missing_password(self,create_courier):
        login_data = {"login": create_courier["data"]["login"], "password": ""}
        response = requests.post(
            f"{TestData.BASE_URL}{TestData.COURIER_URL}/login",
            json=login_data
        )
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для входа"


    @allure.title("Ошибка 404 при неправильном пароле")
    def test_login_wrong_password(self,create_courier):
        login_data = {
            "login": create_courier["data"]["login"],
            "password": "invalid_password"
        }
        response = requests.post(
            f"{TestData.BASE_URL}{TestData.COURIER_URL}/login",
            json=login_data
        )
        assert response.status_code == 404
        assert response.json().get("message") == "Учетная запись не найдена"

    @allure.title("Ошибка 404 при авторизации несуществующего курьера")
    def test_login_nonexistent_courier(self):
        login_data = {
            "login": "user_not_exists",
            "password": "123456"
        }
        response = requests.post(
            f"{TestData.BASE_URL}{TestData.COURIER_URL}/login",
            json=login_data
        )
        assert response.status_code == 404
        assert response.json().get("message") == "Учетная запись не найдена"