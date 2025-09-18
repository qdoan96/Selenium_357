
from ..pages.recruitment_page import RecruitmentPage
from time import sleep
import pytest
from ..base.base_test import BaseTest
from ..pages.login_page_new import LoginPage

@pytest.mark.usefixtures("setup")

class TestRecruitment(BaseTest):
    def test_login_check_recruitment_and_select_dropdowns(self):
        login_page = LoginPage(self.driver)
        login_page.login('Admin', 'admin123')
        sleep(2)
        recruitment_page = RecruitmentPage(self.driver)
        recruitment_page.click_recruitment()
        sleep(2)
        assert recruitment_page.is_recruitment_displayed(), "Recruitment page is not displayed!"
        recruitment_page.click_vacancies()
        sleep(2)
        assert recruitment_page.is_vacancies_displayed(), "Vacancies page is not displayed!"


        recruitment_page.select_job_title("Automation Tester")
        recruitment_page.select_vacancy("Software Engineer")
        recruitment_page.select_hiring_manager("Timothy Amiano")
        recruitment_page.select_status("Active")

        recruitment_page.click_search()
        sleep(2)

        results = recruitment_page.get_search_results()
        assert isinstance(results, list), "No Records Found"
        print("Search Results:", results)

