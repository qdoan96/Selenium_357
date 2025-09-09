import pytest
from selenium import webdriver
class BaseTest:
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        request.cls.driver = self.driver
        yield
        self.driver.quit()