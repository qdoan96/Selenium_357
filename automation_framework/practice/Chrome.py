import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
class BaseTest:
    @pytest.fixture(scope="class", autouse=True) # tu dong thuc thi truoc va sau class
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")
        slogan = self.driverfind_element(By.CLASS_NAME, "_8eso")
        print(slogan.text)
        sleep
        self.driver.quit()