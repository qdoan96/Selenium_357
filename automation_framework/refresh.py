import pytest
from selenium import webdriver
from time import sleep
class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print(f"The website title is: {self.driver.current_url}")
        self.driver.refresh()
        print(f"The website title after refresh is: {self.driver.current_url}")