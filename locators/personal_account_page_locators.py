from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:

    ACCOUNT_FORM = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")  # Форма личного кабинета
    ACCOUNT_BTN = (By.XPATH, ".//a[text() = 'Профиль']")  # Кнопка профиль
    ORDER_HISTORY_BTN = (By.XPATH, ".//a[text() = 'История заказов']")  # Кнопка история заказов
    ORDER_HISTORY_FORM = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")  # Форма истории заказов
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")  # Номер заказа
    CANCEL_BTN = (By.XPATH, ".//button[text() = 'Отмена']")  # Кнопка отмена
    SAVE_BTN = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка сохранить
    LOGOUT_BTN = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка выход
