from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver # gan driver tu base_test.py
    user = (By.XPATH, "//input[@name='username']") # locator
    password = (By.XPATH, "//input[@name='password']") # locator 
    login_button = (By.XPATH, "//button[@type='submit']") # locator


    def login(self): # action
        self.driver.find_element(*self.user).send_keys('Admin') # * de unpacking
        self.driver.find_element(*self.password).send_keys('admin123') # action
        self.driver.find_element(*self.login_button).click() # action #

