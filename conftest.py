import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from locators import Locators
from constants import Constants


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument(Constants.WINDIW_SIZE)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(Constants.BACE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.BUTTON_LOGIN).click()
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.TEST_EMAIL)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.TEST_PASSWORD)
    driver.find_element(*Locators.BUTTON_IN).click()
    return driver
