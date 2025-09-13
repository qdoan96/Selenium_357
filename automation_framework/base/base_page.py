from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def get_element(self, xpath):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*xpath)
    
    def click(self, element):
        self.driver.click(element)
        self.driver.implicitly_wait(10)
        
    def send_key(self, element, text):
        self.driver.send_keys(element, text)
        

    def drop_down(self, element, text):
        self.driver.select_by_visible_text(element, text)
        
