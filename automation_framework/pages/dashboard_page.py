from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver # gan driver tu base_test.py

    def is_dashboard_displayed(self):
        sleep(5)
        return "dashboard" in self.driver.current_url # kiem tra url co chua dashboard khong
    
    