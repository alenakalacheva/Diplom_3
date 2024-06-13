import allure
from data.urls import Urls
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Переход по клику на кнопку "Конструктор"')
    @allure.description('''
                        Проверка перехода на страницу конструктора по клику на кнопку в шапке
                        ''')
    def test_go_to_constructor_page(self, driver):
        header = MainPage(driver)
        main_page = MainPage(driver)
        main_page.move_to_personal_account_btn_and_click()
        header.click_constructor_btn()
        assert main_page.check_constructor_form() and main_page.get_current_url() == Urls.MAIN_PAGE_URL

    @allure.title('Переход в «Ленту заказов»')
    @allure.description('''
                        Проверка перехода в Ленту заказов по клику на кнопку в шапке
                        ''')
    def test_follow_to_orders_feed_page(self, driver):
        header = MainPage(driver)
        main_page = MainPage(driver)
        header.click_order_list_btn()
        assert main_page.check_orders_feed_form() and main_page.get_current_url() == (Urls.MAIN_PAGE_URL + Urls.ORDER_LIST)

    @allure.title('Появление всплывающего окна с информацией об ингридиенте')
    @allure.description('''
                        Проверка появления всплывающего окна при клике на ингридиент
                        ''')
    def test_check_ingredient_info(self, driver):
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun_btn()
        assert main_page.check_fluorescent_bun_form()

    @allure.title('Закрытие всплывающего окна с информацией об ингридиенте')
    @allure.description('''
                        Проверка закрытия всплывающего окна при клике на крестик
                        ''')
    def test_close_ingredient_info(self, driver):
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun_btn()
        main_page.close_popup_form()
        assert main_page.check_close_fluorescent_bun_form()

    @allure.title('Проверка счетчика ингридиентов')
    @allure.description('''
                        При добавлении ингридиента в корзину колличество в счетчике увеличивается
                        ''')
    def test_counter_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.add_bun()
        assert int(main_page.check_counter_ingredient()) > 0

    @allure.title('Оформление заказа залогиненым пользователем')
    @allure.description('''
                        Проверка оформления заказа залогиненым пользователем
                        ''')
    def test_create_order(self, driver, create_new_user, login):
        header = MainPage(driver)
        main_page = MainPage(driver)
        header.click_constructor_btn()
        main_page.add_bun()
        main_page.create_order()
        assert main_page.get_order_number() != '9999'




