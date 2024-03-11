from selenium.webdriver.common.by import By


class Locators:

    # Локаторы для главной страницы
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт" на главной странице
    BUTTON_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка "Оформить заказ" на главной странице
    KEY_BREAD = (By.XPATH, "//span[text()='Булки']")  # кнопка "Булки" в конструктуре
    BREAD_LIST = (By.XPATH, "//h2[contains(text(),'Булки')]")  # список булок
    KEY_SAUCE = (By.XPATH, "//span[text()='Соусы']")  # кнопка "Соусы" в конструктуре
    SAUCE_LIST = (By.XPATH, "//h2[contains(text(),'Соусы')]")  # список соусов
    KEY_FILLING = (By.XPATH, "//span[text()='Начинки']")  # кнопка "Начинки" в конструктуре
    FILLING_LIST = (By.XPATH, "//h2[contains(text(),'Начинки')]")  # список начинок
    LABLE_CREATE_BURGER = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")  # надпись "Соберите бургер"

    # Локаторы для хедера
    KEY_PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')  # кнопка "Личный кабинет" в хедере
    KEY_CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')  # кнопка "Конструктор" в хедере
    KEY_LOGO = (By.CSS_SELECTOR, '.AppHeader_header__logo__2D0X2')  # центральная кнопка "Stellar Burgers" в хедере

    # Локаторы для логина
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")  # поле "Email" на экране логина
    INPUT_PASSWORD = (By.NAME, "Пароль")  # поле "Пароль" на экранах логина
    BUTTON_IN = (By.XPATH, '//button[text()="Войти"]')  # кнопка "Войти" на эжкране логина
    KEY_REGISTRATION = (By.XPATH, '//*[@href="/register"]')  # кнопка "Зарегестрироваться" на экране входа
    KEY_RECOVER_PASSWORD = (By.XPATH, '//*[@href="/forgot-password"]')  # кнопка "Восстановить пароль" на экране логина
    LABLE_LOGIN = (By.XPATH, "//h2[contains(text(),'Вход')]")  # надпись "Вход" на экране логина

    # Локаторы для регистрации
    INPUT_NAME = (By.XPATH, "//fieldset[1]/div/div/input")  # поле "имя" на экране регистрации
    INPUT_EMAIL_REG = (By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")  # поле "Email" на экране регистрации
    INPUT_PASSWORD_REG = (By.NAME, "Пароль")  # поле "Пароль" на экране регистрации (одинаковый локатор в паролем на экране входа и восстановления пароля, но вынес отдельно)
    BUTTON_REGIST = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка "Зарегестрироваться" на экране регистрации
    KEY_INSERT_REG = (By.XPATH, "//a[@href='/login']")  # кнопка "Войти" на экране регистрации у "Уже зарегестрированны?"
    ERROR_PASSWORD = (By.XPATH, "//*[text()='Некорректный пароль']")  # ошибка "Некорректный пароль"

    # Локаторы для восстановления пароля
    BUTTON_RECOVER = (By.XPATH, "//button[text()='Восстановить']")  # кнопка "Восстановить" на экране восстановления пароля
    KEY_INSERT_REC = (By.XPATH, "//a[@href='/login']")  # кнопка "Войти" на экране восстановления пароля (одинаковый локатор в паролем на экране входа и восстановления пароля, но вынес отдельно)

    # Локаторы для личного кабинета
    KEY_LOGOUT = (By.XPATH, "//button[text()='Выход']")  # кнопка "Выйти" в личном кабинете
