import pytest
from selenium import webdriver
class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print(f"The website URL is: {self.driver.current_url}")
        request.cls.driver = self.driver
        yield
        self.driver.quit()