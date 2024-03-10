from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import driver
from randomizer import generate_random_email, random_password


class TestRegistration:

    # регистрация нового пользователя с именем, имейлом и паролем из 6 символов
    def test_registration_with_name_and_right_email_password(self, driver):

        # задаём рандомный email
        email = generate_random_email()
        # задаём рандомный пароль из 6 символов
        password = random_password(6)

        # нажимем кнопку "Войти в аккаунт"
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        # нажимаем кнопку "Зарегестрироваться"
        driver.find_element(*Locators.KEY_REGISTRATION).click()
        # вводим данные для регистрации, используя переменные email и password
        driver.find_element(*Locators.INPUT_NAME).send_keys("Гость")
        driver.find_element(*Locators.INPUT_EMAIL_REG).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD_REG).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGIST).click()

        # переход на экран логина после нажатия кнопки "Зарегестрироваться"
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Вход')]")))
        # вводим данные из регистрации
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD_REG).send_keys(password)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_IN)).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(Locators.KEY_LOGO))

    # проверка ошибки "Некорректный пароль", если пароль менее 6 символов
    def test_error_registration_with_short_password(self, driver):
        email = generate_random_email()
        # задаём рандомный пароль из 3 символов
        password = random_password(5)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.KEY_REGISTRATION).click()
        driver.find_element(*Locators.INPUT_NAME).send_keys("Гость")
        driver.find_element(*Locators.INPUT_EMAIL_REG).send_keys(email)
        # вводим пароль менее 6 символов
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGIST).click()
        # ловим ошибку "Некорректный пароль"
        assert driver.find_element(By.XPATH, "//*[text()='Некорректный пароль']").is_displayed()
