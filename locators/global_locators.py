from selenium.webdriver.common.by import By


class HeaderPageLocators:
    PERSONAL_ACCOUNT_BTN = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")
    CONSTRUCTOR_BTN = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")
    ORDER_LIST_BTN = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")
