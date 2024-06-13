import allure
from pages.base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PasswordRecoveryPage(BasePage):
    """Методы взаимодействия со страницей 'Восстановление пароля'"""

    @allure.step('Проверка формы восстановления пароля')
    def check_recovery_form(self):
        return self.check_element(PasswordRecoveryPageLocators.RECOVERY_TEXT_FORM)

    @allure.step('Заполнение формы Email')
    def send_email_to_email_field(self, email):
        self.send_keys_to_element(PasswordRecoveryPageLocators.EMAIL_INPUT, email)

    @allure.step('Клик по кнопке Восстановить')
    def click_recovery_btn(self):
        self.click_element(PasswordRecoveryPageLocators.RECOVER_BTN)

    @allure.step('Клик по кнопке Войти')
    def click_login_btn(self):
        self.click_element(PasswordRecoveryPageLocators.LOGIN_ACCOUNT_BTN)

    @allure.step('Заполнение поля Пароль')
    def send_password_to_password_field(self, password):
        self.send_keys_to_element(PasswordRecoveryPageLocators.PASSWORD_INPUT, password)

    @allure.step('Заполнение поля Код из письма')
    def send_code_to_code_field(self, code):
        self.send_keys_to_element(PasswordRecoveryPageLocators.CODE_FROM_MAIL_INPUT, code)

    @allure.step('Клик по кнопке Сохранить')
    def click_save_btn(self):
        self.click_element(PasswordRecoveryPageLocators.SAVE_BTN)

    @allure.step('Проверка подсветки поля Пароль')
    def check_active_password_field(self, password):
        self.send_password_to_password_field(password)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(PasswordRecoveryPageLocators.SHOW_BTN))
        self.click_element(PasswordRecoveryPageLocators.SHOW_BTN)
        return self.check_element(PasswordRecoveryPageLocators.INPUT_FIELD_ACTIVE)

    @allure.step('Проверка отображения кнопки Сохранить')
    def check_save_btn(self):
        return self.check_element(PasswordRecoveryPageLocators.SAVE_BTN)