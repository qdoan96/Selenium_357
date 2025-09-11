from automation_framework.pages.recruitment_page import RecruitmentPage
from time import sleep
import pytest
from automation_framework.practice.close import BaseTest
from automation_framework.pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestRecruitment(BaseTest):
    def test_recruitment_page(self):
        login_page = LoginPage(self.driver) # khoi tao login_page
        login_page.login() # goi ham login
        sleep (3)
        recruitment_page = RecruitmentPage(self.driver)
        recruitment_page.click_recruitment()
        sleep(5)