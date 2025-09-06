from selenium import webdriver
def setup(self, request):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(f"The website URL is: {self.driver.title}")