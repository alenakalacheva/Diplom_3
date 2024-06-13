from selenium.webdriver.common.by import By


class OrderListPageLocators:
    ORDERS_LIST_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')  # Заголовок страницы
    ORDERS_INFO = (By.XPATH, '//p[text()="Cостав"]')  # Окно детали заказа
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")  # Счетчик заказов за все время
    DAILY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")  # Счетчик заказов за сегодня
    NUMBER_ORDER_UNDERWAY = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")  # Заказы "В работе"
    ORDER_INFO_WINDOW = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")  # 1 заказ в истории
    ORDER_LIST = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')  # Все заказы в истории
