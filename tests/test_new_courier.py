import pytest
import requests
from data import TestData
from conftest import courier_data
import allure

class TestCourierCreationApi:

    @allure.title("Успешное создание нового курьера")
    def test_create_courier_success(self, courier_data):
        response = requests.post(f"{TestData.BASE_URL}{TestData.COURIER_URL}",
                                 data=courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Ошибка 409 при попытке создать курьера с существующим логином")
    def test_create_duplicate_courier(self, courier_data):
        response = requests.post(f"{TestData.BASE_URL}{TestData.COURIER_URL}",
                                 data=courier_data)

        response2 = requests.post(f"{TestData.BASE_URL}{TestData.COURIER_URL}",
                                 data=courier_data)
        assert response2.status_code == 409
        assert TestData.COURIER_LOGIN_CONFLICT in response2.text

    @allure.title("Ошибка 400 при отсутствии обязательного поля")
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_missing_field(self, courier_data, missing_field):
        data = courier_data.copy()
        del data[missing_field]
        response = requests.post(f"{TestData.BASE_URL}{TestData.COURIER_URL}",
                                 json=data)
        assert response.status_code == 400
        assert TestData.COURIER_CREATION_MISSING_FIELD in response.text