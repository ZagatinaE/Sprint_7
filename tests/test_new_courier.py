import pytest
import requests
from data import TestData
from conftest import courier_data


class TestCourierCreationApi:
    def test_create_courier_success(self, courier_data):
        response = requests.post(f"{TestData.BASE_URL}{TestData.COURIER_URL}",
                                 data=courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    def test_create_duplicate_courier(self, courier_data):
        response = requests.post(f"{TestData.BASE_URL}{TestData.COURIER_URL}",
                                 data=courier_data)
        assert response.status_code == 201

        response2 = requests.post(f"{TestData.BASE_URL}{TestData.COURIER_URL}",
                                 data=courier_data)
        assert response2.status_code == 409
        assert "Этот логин уже используется" in response2.text

    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_missing_field(self, courier_data, missing_field):
        data = courier_data.copy()
        del data[missing_field]
        response = requests.post(f"{TestData.BASE_URL}{TestData.COURIER_URL}",
                                 json=data)
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.text