from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    RECOVER_BTN = (By.XPATH, ".//button[text() = 'Восстановить']")  # Кнопка восстановить
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Введите новый пароль']")  # Поле ввода нового пароля
    LOGIN_ACCOUNT_BTN = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка войти
    CODE_FROM_MAIL_INPUT = (By.XPATH, ".//label[text() = 'Введите код из письма']")  # Поле ввода кода из письма
    SAVE_BTN = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка Сохранить
    RECOVERY_TEXT_FORM = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")  # ФОрма восстановления пароля
    SHOW_BTN = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")  # Показать пароль
    INPUT_FIELD_ACTIVE = (By.CSS_SELECTOR, ".input.input_status_active")  # Подсветка поля пароль
