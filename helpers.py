from faker import Faker
import requests
import allure
from data.urls import Urls


@allure.step("Создать данные для нового пользователя")
def create_correct_user_data():
    faker = Faker('ru_RU')
    data = {
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.first_name()
    }
    return data


class Order:

    @allure.step('Создание нового заказа пользователя через API')
    def create_order(self, create_new_user, create_list_of_ingredients):
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        data = create_list_of_ingredients
        requests.post(Urls.MAIN_PAGE_URL + Urls.ORDER_ENDPOINT, headers=headers,
                      data=data)

    @allure.step('Получение заказов пользователя через API')
    def get_user_orders(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        response = requests.get(Urls.MAIN_PAGE_URL + Urls.ORDER_ENDPOINT, headers=headers)
        return response.json()["orders"][0]["number"]
