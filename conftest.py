import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from locators import Locators


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.BUTTON_LOGIN).click()
    driver.find_element(*Locators.INPUT_EMAIL).send_keys("VictorKorol6123@yandex.ru")
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys("123456")
    driver.find_element(*Locators.BUTTON_IN).click()
    return driver
