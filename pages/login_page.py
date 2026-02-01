import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.base_url = base_url

        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")
        self.error = (By.CSS_SELECTOR, '[data-test="error"]')

    @allure.step("Открыть страницу логина")
    def open(self):
        self.driver.get(self.base_url)
        self.wait.until(EC.visibility_of_element_located(self.username))

    @allure.step("Выполнить логин: {username}")
    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_btn).click()

    @allure.step("Отправить форму с пустыми полями")
    def submit_empty(self):
        self.driver.find_element(*self.login_btn).click()

    def get_error_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.error)
        ).text
