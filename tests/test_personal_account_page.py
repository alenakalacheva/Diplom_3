import allure
from data.urls import Urls

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccountPage:

    @allure.title('Переход в "Личный кабинет"')
    @allure.description('''
                        Проверка перехода в личный кабинет с главной страницы
                        ''')
    def test_go_to_personal_account_page(self, driver, create_new_user, login):
        header = MainPage(driver)
        personal_account = PersonalAccountPage(driver)
        header.click_profile_area_btn()
        assert personal_account.check_profile_area_form() and personal_account.get_current_url() == (Urls.MAIN_PAGE_URL + Urls.ACCOUNT_PAGE)

    @allure.title('Переход из личного кабинета в "Историю Заказов"')
    @allure.description('''
                        Проверка перехода из личного кабинета в историю заказов кликом по кнопке
                        ''')
    def test_go_to_orders_history(self, driver, create_new_user, login):
        header = MainPage(driver)
        personal_account = PersonalAccountPage(driver)
        header.click_profile_area_btn()
        personal_account.click_orders_history_btn()
        assert personal_account.check_profile_area_form() and personal_account.get_current_url() == (Urls.MAIN_PAGE_URL + Urls.ORDER_HISTORY)

    @allure.title('Выход из аккаунта')
    @allure.description('''
                        Проверка возможности разлогиниться кликом по кнопке "Выход"
                        ''')
    def test_exit_profile_area(self, driver, create_new_user, login):
        header = MainPage(driver)
        personal_account = PersonalAccountPage(driver)
        login_page = LoginPage(driver)
        header.click_profile_area_btn()
        personal_account.click_logout_btn()
        assert login_page.check_authorization_form_verification() and login_page.get_current_url() == (Urls.MAIN_PAGE_URL + Urls.LOGIN_PAGE)