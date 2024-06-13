from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from seletools.actions import drag_and_drop
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ждем кликабельности элемента')
    def wait_element_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    @allure.step('Ждем загрузки элемента')
    def wait_for_load_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))

    @allure.step('Нажимаем на элемент')
    def click_element(self, locator):
        self.wait_element_clickable(locator)
        self.driver.find_element(*locator).click()

    @allure.step('Передаем текст в элемент')
    def send_keys_to_element(self, locator, text):
        self.wait_element_clickable(locator)
        self.driver.find_element(*locator).send_keys(text)


    @allure.step('Получаем текст элемента')
    def get_text_locator(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    @allure.step('Получаем текст элементов')
    def get_text_locators(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Получаем наличие элемента')
    def check_element(self, locator):
        self.wait_for_load_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Проверяем отсутствие элемента')
    def check_element_is_not_visible(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Перетаскиваем элемент')
    def drag_and_drop(self, element_one, element_two):
        driver = self.driver
        source = self.driver.find_element(*element_one)
        target = self.driver.find_element(*element_two)
        drag_and_drop(driver, source, target)

    @allure.step('Переход к элементу и клик на него')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()