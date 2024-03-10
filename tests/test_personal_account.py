from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import login, driver
from locators import Locators


class TestPersonalAccount:

    # переход в личный кабинет с главной страницы по клику на "Личный кабинет"
    def test_transfer_to_personal_account_with_main_page(self, login, driver):
        driver = login
        driver.find_element(*Locators.KEY_PERSONAL_ACCOUNT).click()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.KEY_LOGOUT))

    # переход в конструктор с личного кабинета по клику на кнопку "Конструктор"
    def test_transfer_to_constructor_with_personal_account_from_button_constructor(self, login, driver):
        driver = login
        driver.find_element(*Locators.KEY_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.KEY_CONSTRUCTOR).click()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))

    # переход в конструктор с личного кабинета по клику на логотип "Stellar Burgers"
    def test_transfer_to_constructor_with_personal_account_from_logo(self, login, driver):
        driver = login
        driver.find_element(*Locators.KEY_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.KEY_LOGO).click()
        assert WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))

