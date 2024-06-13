import allure
from locators.main_page_locators import MainPageLocators
from locators.global_locators import HeaderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MainPage(BasePage):

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_btn(self):
        self.move_to_element_and_click(HeaderPageLocators.CONSTRUCTOR_BTN)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_order_list_btn(self):
        self.move_to_element_and_click(HeaderPageLocators.ORDER_LIST_BTN)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_profile_area_btn(self):
        self.move_to_element_and_click(HeaderPageLocators.PERSONAL_ACCOUNT_BTN)

    @allure.step('Переход к кнопке "Личный Кабинет" и клик на нее')
    def move_to_personal_account_btn_and_click(self):
        self.move_to_element_and_click(HeaderPageLocators.PERSONAL_ACCOUNT_BTN)

    @allure.step('Проверка отображения формы конструктор')
    def check_constructor_form(self):
        return self.check_element(MainPageLocators.CONSTRUCTOR_FORM)

    @allure.step('Проверка отображения формы ленты заказов')
    def check_orders_feed_form(self):
        return self.check_element(MainPageLocators.ORDER_LIST_FORM)

    @allure.step('Клик по Флюорисцентной булке RD-D3')
    def click_fluorescent_bun_btn(self):
        self.click_element(MainPageLocators.BUN_BTN)

    @allure.step('Проверка отображения формы "Информации о булке"')
    def check_fluorescent_bun_form(self):
        return self.check_element(MainPageLocators.INGREDIENTS_INFO)

    @allure.step('Проверка закрытия формы "Информация о булке"')
    def check_close_fluorescent_bun_form(self):
        return self.check_element_is_not_visible(MainPageLocators.INGREDIENTS_INFO)

    @allure.step('Закрытие формы информации об ингридиенте')
    def close_popup_form(self):
        self.move_to_element_and_click(MainPageLocators.CLOSE_POPUP_FORM)

    @allure.step('Добавить булку в корзину')
    def add_bun(self):
        self.drag_and_drop(MainPageLocators.BUN_BTN, MainPageLocators.ORDER_BASKET)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_place_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Создание заказа')
    def create_order(self):
        self.add_bun()
        self.click_place_order_button()

    @allure.step('Получение значения счетчика ингредиента')
    def check_counter_ingredient(self):
        return self.get_text_locator(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Проверка отображения формы Оформление заказа')
    def check_order_form(self):
        return self.check_element(MainPageLocators.ORDER_FORM)

    @allure.step('Получение номера оформленного заказа')
    def get_order_number(self):
        WebDriverWait(self.driver, 10).until(EC.none_of(EC.text_to_be_present_in_element(MainPageLocators.ORDER_NUM, '9999')))
        return self.get_text_locator(MainPageLocators.ORDER_NUM)

    @allure.step('Ожидание загрузки кнопки Оформить заказ')
    def wait_load_main_page(self):
        self.wait_for_load_element(MainPageLocators.ORDER_BUTTON)
