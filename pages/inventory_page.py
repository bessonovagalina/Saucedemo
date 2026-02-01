import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.container = (By.ID, "inventory_container")
        self.title = (By.CLASS_NAME, "title")
        self.menu = (By.ID, "react-burger-menu-btn")

    @allure.step("Проверить, что Inventory страница открыта")
    def assert_opened(self):
        self.wait.until(EC.url_contains("inventory.html"))
        self.wait.until(EC.visibility_of_element_located(self.container))
        self.wait.until(EC.visibility_of_element_located(self.title))
        self.wait.until(EC.visibility_of_element_located(self.menu))
