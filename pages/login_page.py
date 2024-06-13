import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    @allure.step('Проверка отображения формы логина')
    def check_authorization_form_verification(self):
        return self.check_element(LoginPageLocators.AUTH_FORM)

    @allure.step('Заполнение поля "Email"')
    def send_email_to_email_field(self, email):
        self.send_keys_to_element(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step('Заполнение поля "Password"')
    def send_password_to_password_field(self, password):
        self.send_keys_to_element(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step('Клик на кнопку "Войти"')
    def click_login_btn(self):
        self.move_to_element_and_click(LoginPageLocators.LOGIN_ACCOUNT_BTN)

    @allure.step('Авторизация на сайте')
    def login(self, email, password):
        self.send_email_to_email_field(email)
        self.send_password_to_password_field(password)
        self.click_login_btn()

    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_recovery_btn(self):
        self.move_to_element_and_click(LoginPageLocators.RECOVER_BTN)

    @allure.step('Клик на кнопку "Зарегистрироваться"')
    def click_register_btn(self):
        self.move_to_element_and_click(LoginPageLocators.REGISTRATION_BTN)
