import pytest
import requests
from data import TestData
import allure





class TestCreateOrder:

    @allure.title("Создание заказа с параметрами цвета")
    @pytest.mark.parametrize('order_data', TestData.ORDER_DATA_WITH_COLOR)
    def test_create_order(self, order_data):
        response = requests.post(
            f"{TestData.BASE_URL}{TestData.ORDERS_URL}", json=order_data)
        assert response.status_code == 201
        assert "track" in response.json()
