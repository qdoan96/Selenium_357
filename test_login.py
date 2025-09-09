import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
@pytest.fixture
def setup():
    # Setup: Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Teardown: Quit the WebDriver
    driver.quit()
def test_login(setup):
    driver = setup
    
    driver.get("https://opensource-demo.orangehrmlive.com/")
    username = driver.find_element(By.XPATH, "//input[@name='username']")
    password = driver.find_element(By. XPATH, "//input[@name='password']")
    username.send_keys("Admin")
    password.send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
    sleep(3)  # Wait for login to complete
    assert "dashboard" in driver.current_url
