
import pytest
from datetime import datetime
from ..pages.login_page_new import LoginPage
from ..pages.recruitment_page import RecruitmentPage
from ..base.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setup")
class TestVacancy(BaseTest):
    def test_create_and_verify_vacancy(self):
        driver = self.driver
        login_page = LoginPage(driver)
        recruitment_page = RecruitmentPage(driver)

        # Step 1: Login
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login_page.login("Admin", "admin123")

        # Lấy tên user hiện tại sau khi login
        current_user = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'oxd-userdropdown-name')]"))
        ).text

        # Step 2: Go to Recruitment > Vacancies
        recruitment_page.click_recruitment()
        recruitment_page.click_vacancies()

        # Step 3: Click +Add
        recruitment_page.click_add_vacancy()

        # Step 4: Verify Add Vacancy page
        assert recruitment_page.is_add_vacancy_displayed(), "Add Vacancy page not displayed"

        # Step 5: Input all fields
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        vacancy_name = f"Automation Tester For {current_date}"
        recruitment_page.input_vacancy_name(vacancy_name)
        #recruitment_page.select_job_title("Automation Tester")
        recruitment_page.input_description("Automation Test Is Running")
        recruitment_page.select_hiring_manager(current_user)
        recruitment_page.input_number_of_positions(1)
        recruitment_page.set_active(False)
        recruitment_page.set_publish_checkbox("Publish in RSS Feed", True)
        recruitment_page.set_publish_checkbox("Publish in Web Page", True)

        # Step 6: Save
        recruitment_page.click_save_vacancy()

        # Step 7: Verify Edit Vacancy page
        assert recruitment_page.is_edit_vacancy_displayed(), "Edit Vacancy page not displayed"

        # Step 8: Cancel
        recruitment_page.click_cancel_vacancy()

        # Step 9: Verify Vacancies page
        assert recruitment_page.is_vacancies_displayed(), "Vacancies page not displayed"

        # Step 10: Search for created vacancy
        recruitment_page.select_job_title("Automation Tester")
        recruitment_page.select_hiring_manager(current_user)
        recruitment_page.click_search()

        # Step 11: Verify at least one result
        results = recruitment_page.get_search_results()
        assert len(results) > 0, "No search results found"

        # Step 12: Verify data matches
        found = False
        for row in results:
            if row.get("Job Title") == "Automation Tester" and row.get("Vacancy Name") == vacancy_name:
                found = True
                break
        assert found, "Created vacancy not found in search results"

        # Step 13: Logout
        recruitment_page.logout()
        assert "login" in driver.current_url.lower(), "Logout failed"

