import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_success(driver, base_url):
    login = LoginPage(driver, base_url)
    login.open()

    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.assert_opened()


def test_login_wrong_password(driver, base_url):
    login = LoginPage(driver, base_url)
    login.open()

    login.login("standard_user", "wrong_pass")

    assert "do not match" in login.get_error_text()


def test_login_locked_out_user(driver, base_url):
    login = LoginPage(driver, base_url)
    login.open()

    login.login("locked_out_user", "secret_sauce")

    assert "locked out" in login.get_error_text()


def test_login_empty_fields(driver, base_url):
    login = LoginPage(driver, base_url)
    login.open()

    login.submit_empty()

    assert "Username is required" in login.get_error_text()


def test_login_performance_glitch_user(driver, base_url):
    login = LoginPage(driver, base_url)
    login.open()

    login.login("performance_glitch_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.assert_opened()
