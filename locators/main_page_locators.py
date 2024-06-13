from selenium.webdriver.common.by import By


class MainPageLocators:

    ORDER_LIST_FORM = (By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']")                    # Форма ленты заказа
    CONSTRUCTOR_FORM = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']") # Форма конструктора
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")                          # Кнопка оформить заказ
    BUN_BTN = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")                  # Кнопка флюорисцентной булки
    CLOSE_POPUP_FORM = (By.XPATH, '//button[contains(@class,"close")]')                              # Крестик на модульном окне
    INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")         # Счетчик ингредиента
    ORDER_FORM = (By.XPATH, ".//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")   # Форма оформленного заказа
    ORDER_BASKET = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")             # Корзина
    ORDER_NUM = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")            # Номер заказа
    LOGIN_BTN = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")              # Кнопка личного кабинета
    INGREDIENTS_INFO = (By.XPATH, "//h2[text()= 'Детали ингредиента']")



