from conftest import driver
from locators import Locators


class TestConstructor:

    def test_constructor_transitions_to_sections_bread(self, driver):
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*Locators.SAUCE_LIST))
        driver.find_element(*Locators.KEY_BREAD).click()
        assert driver.find_element(*Locators.BREAD_LIST).is_displayed()

    def test_constructor_transitions_to_sections_sauce(self, driver):
        driver.find_element(*Locators.KEY_SAUCE).click()
        assert driver.find_element(*Locators.SAUCE_LIST).is_displayed()

    def test_constructor_transitions_to_sections_filling(self, driver):
        driver.find_element(*Locators.KEY_FILLING).click()
        assert driver.find_element(*Locators.FILLING_LIST).is_displayed()

