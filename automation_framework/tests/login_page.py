from selenium.webdriver.common.by import By
from time import sleep
from automation_framework.base.base_test import BaseTest

class LoginPage(BaseTest):
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_login_successful(self):
        return "dashboard" in self.driver.current_url

    def test_login_valid(self):
        self.enter_username("Admin")
        self.enter_password("admin123")
        self.click_login()
        sleep(3)
        return self.is_login_successful()

    def test_login_invalid(self):
        self.enter_username("sai_user")
        self.enter_password("sai_pass")
        self.click_login()
        sleep(2)
        return not self.is_login_successful()