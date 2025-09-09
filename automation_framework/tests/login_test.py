
from automation_framework.base.base_test import BaseTest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep

class Test_login(BaseTest): # ke thua BaseTest
    def test_login(self): # su dung lai ham setup tu BaseTest
        driver = self.driver # su dung driver tu BaseTest
        username = driver.find_element(By.XPATH, "//input[@name='username']") # tim kiem username
        password = driver.find_element(By. XPATH, "//input[@name='password']") # tim kiem password
        username.send_keys("Admin") # nhap username
        password.send_keys("admin123") # nhap password
        driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click() # click login
        sleep(3)  # Wait for login to complete
        assert "dashboard" in driver.current_url # kiem tra login thanh cong
        
        
