import pytest
from selenium import webdriver
from time import sleep

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request): 
        self.driver = webdriver.Chrome() # khoi tao trinh duyet
        self.driver.maximize_window() # mo to cua so trinh duyet
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # mo trang web      
        request.cls.driver = self.driver   # gan driver cho class
        yield # doi nhung test case khac chay xong
        self.driver.quit() # dong trinh duyet sau khi chay nhung test case khac xong #