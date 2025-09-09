from selenium import webdriver
driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://automationpractice.com/index.php")
print(driver.title)
driver.get("https://www.google.com")
print(driver.title)

driver.back()
print(driver.title)