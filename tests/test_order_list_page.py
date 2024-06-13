import allure
import pytest
from pages.order_list_page import OrderListPage
from locators.order_list_page_locators import OrderListPageLocators

from helpers import Order
from pages.main_page import MainPage


class TestOrderListPage:

    @allure.title('Появление всплывающего окна с деталями заказа')
    @allure.description('''
                        Проверка открытия окна с деталями заказа при клике на заказ в Ленте заказов
                        ''')
    def test_check_order_info_window(self, driver):
        header = MainPage(driver)
        order_list = OrderListPage(driver)
        header.click_order_list_btn()
        order_list.click_order_info()
        assert order_list.check_order_info_window()

    @allure.title('Появление заказа в разделе "в работе"')
    @allure.description('''
                        Проверка, что после создания заказа его номер появляется в разделе "в работе"
                        ''')
    def test_check_user_order_underway(self, driver, create_new_user, login, create_list_of_ingredients):

        order = Order()
        header = MainPage(driver)
        order_list = OrderListPage(driver)
        header.click_order_list_btn()
        order.create_order(create_new_user, create_list_of_ingredients)
        orders_underway = order_list.get_orders_underway()
        user_order = str(order.get_user_orders(create_new_user))
        assert user_order in orders_underway

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('''
                        Проверка что созданные пользователем заказы отображаются в Ленте заказов
                        ''')
    def test_check_user_orders_in_orders_list(self, driver, create_new_user, login, create_list_of_ingredients):
        order = Order()
        header = MainPage(driver)
        order_list = OrderListPage(driver)
        header.click_order_list_btn()
        order.create_order(create_new_user, create_list_of_ingredients)
        user_order = str(order.get_user_orders(create_new_user))
        history_orders_in_feed = order_list.get_orders_history()
        assert user_order in history_orders_in_feed

    @allure.title('При создании нового заказа счетчики Выполнено за всё время / Выполнено за сегодня увеличиваются')
    @allure.description('''
                        Проверка, что после создания нового заказа счетчик увеличивается на 1
                        ''')
    @pytest.mark.parametrize('counter',
                             [OrderListPageLocators.DAILY_ORDERS_COUNTER, OrderListPageLocators.TOTAL_ORDERS_COUNTER])
    def test_update_counter_orders(self, driver, create_new_user, login, counter, create_list_of_ingredients):
        order = Order()
        header = MainPage(driver)
        feed_order = OrderListPage(driver)
        header.click_order_list_btn()
        now_counter = int(feed_order.check_counter_orders(counter))
        order.create_order(create_new_user, create_list_of_ingredients)
        new_counter = int(feed_order.check_counter_orders(counter))
        assert new_counter == now_counter + 1
