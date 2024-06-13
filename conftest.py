import pytest
import requests
import helpers
from data.urls import Urls
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Urls.MAIN_PAGE_URL)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(Urls.MAIN_PAGE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def create_new_user():
    payload = helpers.create_correct_user_data()
    response = requests.post(Urls.MAIN_PAGE_URL + Urls.CREATE_USER_ENDPOINT, data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(Urls.MAIN_PAGE_URL + Urls.CREATE_USER_ENDPOINT, headers={"Authorization": token})


@pytest.fixture
def login(driver, create_new_user):
    create_user_data = create_new_user[0]
    header_page = MainPage(driver)
    login_page = LoginPage(driver)
    header_page.click_profile_area_btn()
    login_page.login(create_user_data["email"], create_user_data["password"])
    main_page = MainPage(driver)
    main_page.wait_load_main_page()


@pytest.fixture
def create_list_of_ingredients():
    response = requests.get(Urls.MAIN_PAGE_URL + Urls.INGREDIENTS_ENDPOINT)
    data = {"ingredients": [response.json()["data"][0]["_id"]]}
    return data