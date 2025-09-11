from selenium.webdriver.common.by import By


class RecruitmentPage:
    def __init__(self, driver):
        self.driver = driver # gan driver tu base_test.py #3
    recruitment = (By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']")
    
    def is_recruitment(self):
        self.driver.find_element(*self.recruitment).click()
    