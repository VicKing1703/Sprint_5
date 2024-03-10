from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import login, driver
from locators import Locators


class TestLogout:

    def test_logout(self, login, driver):
        driver = login
        driver.find_element(*Locators.KEY_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.KEY_LOGOUT)).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Вход')]")))
