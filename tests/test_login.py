from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import driver


class TestLogin:

    # авторизация через "Войти в аккаунт"
    def test_login_by_key_enter_in_account(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys("VictorKorol6123@yandex.ru")
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.BUTTON_IN).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element(
            Locators.BUTTON_ORDER, "Оформить заказ"))

    # авторизация через "Личный кабинет"
    def test_login_by_key_personal_account(self, driver):
        driver.find_element(*Locators.KEY_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys("VictorKorol6123@yandex.ru")
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.BUTTON_IN).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element(
            Locators.BUTTON_ORDER, "Оформить заказ"))

    # авторизация через кнопку в форме регистрации
    def test_login_by_key_registration(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.KEY_REGISTRATION).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.KEY_INSERT_REG)).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys("VictorKorol6123@yandex.ru")
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.BUTTON_IN).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element(
            Locators.BUTTON_ORDER, "Оформить заказ"))

    # авторизация через "Восстановление пароля"
    def test_login_by_recover_password(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.KEY_RECOVER_PASSWORD).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.KEY_INSERT_REC)).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys("VictorKorol6123@yandex.ru")
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.BUTTON_IN).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element(
            Locators.BUTTON_ORDER, "Оформить заказ"))
