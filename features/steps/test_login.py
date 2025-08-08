import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
import os


# Link this file to the feature file
scenarios('login.feature')

@pytest.fixture
def driver():
    options = Options()

    # Default is headed, unless HEADLESS=true is set
    if os.getenv('HEADLESS') == 'true':
        options.add_argument('--headless')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # driver.maximize_window()
    yield driver
    driver.quit()


@given('the user is on the login page')
def open_login_page(driver):
    login_page = LoginPage(driver)
    login_page.load()

@when('the user logs in with username "standard_user" and password "secret_sauce"')
def perform_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

@then('the user should be redirected to the products page')
def verify_login_success(driver):
    assert "inventory" in driver.current_url
