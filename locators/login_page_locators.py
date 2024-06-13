from selenium.webdriver.common.by import By

class LoginPageLocators:

    AUTH_FORM = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")  # Форма авторизации
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    LOGIN_ACCOUNT_BTN = (By.XPATH, "//button[text() = 'Войти']")  # Кнопка войти
    REGISTRATION_BTN = (By.XPATH, "//a[text() = 'Зарегистрироваться']")  # Кнопка зерегистрироваться
    RECOVER_BTN = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # Кнопка восстановить пароль
