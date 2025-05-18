import requests
from data import TestData
import allure


class TestGetOrders:

    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        response = requests.get(f"{TestData.BASE_URL}{TestData.ORDERS_URL}")

        assert response.status_code == 200
        body = response.json()

        assert "orders" in body, "Ответ не содержит ключ 'orders'"
        assert isinstance(body["orders"], list), "'orders' должен быть списком"