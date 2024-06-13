import allure
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step('Проверка отображения формы "Личного кабинета"')
    def check_profile_area_form(self):
        return self.check_element(PersonalAccountPageLocators.ACCOUNT_FORM)

    @allure.step('Клик по кнопке "Профиль"')
    def click_profile_btn(self):
        self.click_element(PersonalAccountPageLocators.ACCOUNT_BTN)

    @allure.step('Клик по кнопке "История заказов"')
    def click_orders_history_btn(self):
        self.click_element(PersonalAccountPageLocators.ORDER_HISTORY_BTN)

    @allure.step('Проверка отображения формы "История заказов"')
    def check_history_form(self):
        return self.check_element(PersonalAccountPageLocators.ORDER_HISTORY_FORM)

    @allure.step('Клик по кнопке "Выход"')
    def click_logout_btn(self):
        self.click_element(PersonalAccountPageLocators.LOGOUT_BTN)

    @allure.step('Клик по кнопке "Отмена"')
    def click_cansel_btn(self):
        self.click_element(PersonalAccountPageLocators.CANCEL_BTN)

    @allure.step('Клик по кнопке "Сохранить"')
    def click_save_btn(self):
        self.click_element(PersonalAccountPageLocators.SAVE_BTN)

    @allure.step('Получение номера заказа в истории')
    def get_orders_number(self):
        return self.get_text_locator(PersonalAccountPageLocators.ORDER_NUMBER)