from helpers import DataGenerator




class TestData:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    COURIER_URL = 'courier'
    ORDERS_URL = 'orders'
    COURIER_LOGIN_CONFLICT = "Этот логин уже используется"
    COURIER_CREATION_MISSING_FIELD = "Недостаточно данных для создания учетной записи"

    ORDER_DATA_BASE={
        "firstName": "Raisa",
        "lastName": "Ivanova",
        "address": "Fruktovaya, 12",
        "metroStation": 4,
        "phone": "+7 111 222 33 45",
        "rentTime": 5,
        "deliveryDate": "2025-05-17",
        "comment": "Call before delivery"}

    ORDER_DATA_WITH_COLOR = [
        {**ORDER_DATA_BASE, "color": ["BLACK"]},
        {**ORDER_DATA_BASE, "color": ["GREY"]},
        {**ORDER_DATA_BASE, "color": ["BLACK", "GREY"]},
        {**ORDER_DATA_BASE, "color": []}
    ]


    @staticmethod
    def get_courier_data():
        return {
            "login": DataGenerator.generate_random_string(10),
            "password": DataGenerator.generate_random_string(10),
            "firstName": DataGenerator.generate_random_string(10)
        }


