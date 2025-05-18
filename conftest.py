import pytest
import requests
from data import TestData



@pytest.fixture
def courier_data():
    return TestData.get_courier_data()




@pytest.fixture
def create_courier():
    data_courier = TestData.get_courier_data()
    response = requests.post(f"{TestData.BASE_URL}{TestData.COURIER_URL}", json=data_courier)

    login_response = requests.post(
        f"{TestData.BASE_URL}{TestData.COURIER_URL}/login",
        json={
            "login": data_courier["login"],
            "password": data_courier["password"]
        }
    )
    courier_id = login_response.json()["id"]

    yield  {"id": courier_id, "data": data_courier}

    requests.delete(f"{TestData.BASE_URL}{TestData.COURIER_URL}/{courier_id}")




@pytest.fixture
def get_order_id(create_test_order):
    track = create_test_order
    response = requests.get(f"{TestData.BASE_URL}{TestData.ORDERS_URL}/track?t={track}")
    return response.json()["order"]["id"]




@pytest.fixture
def accept_order(create_courier, get_order_id):
    order_id = get_order_id
    courier_id = create_courier
    response = requests.put(
       f"{TestData.BASE_URL}{TestData.ORDERS_URL}/{order_id}/accept",
        params={"courierId": courier_id})
    return order_id