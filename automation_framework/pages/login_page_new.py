from automation_framework.base.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    username = (By.XPATH, "//input[@name='username']")
    password = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//button[@type='submit']")
    
    def __init__(self, driver):
        super().__init__(driver) # goi constructor cua BasePage

    def login(self, username, password):
        self.get_element(self.username).send_keys(username)
        self.get_element(self.password).send_keys(password)
        self.get_element(self.login_button).click()