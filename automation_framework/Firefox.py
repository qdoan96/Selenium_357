import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        yield
        self.driver.quit()