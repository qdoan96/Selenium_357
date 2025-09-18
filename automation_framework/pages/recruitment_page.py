
from selenium.webdriver.common.by import By
from time import sleep
from ..base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RecruitmentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.recruitment = (By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']")
        self.header = (By.XPATH, "//h6[text()='Recruitment']")
        # Locators cho các dropdown
        self.job_title_dropdown = (By.XPATH, "//div[label[text()='Job Title']]/following-sibling::div//div[@class='oxd-select-text-input']")
        self.vacancy_dropdown = (By.XPATH, "//div[label[text()='Vacancy']]/following-sibling::div//div[@class='oxd-select-text-input']")
        self.hiring_manager_dropdown = (By.XPATH, "//div[label[text()='Hiring Manager']]/following-sibling::div//div[@class='oxd-select-text-input']")
        self.status_dropdown = (By.XPATH, "//div[label[text()='Status']]/following-sibling::div//div[@class='oxd-select-text-input']")

    def click_recruitment(self):
        self.get_element(self.recruitment).click()

    def is_recruitment_displayed(self):
        try:
            return self.get_element(self.header).is_displayed()
        except:
            return False

    def click_vacancies(self):
        vacancies_tab = (By.XPATH, "//a[text()='Vacancies']")
        self.get_element(vacancies_tab).click()

    def is_vacancies_displayed(self):
        sleep(5)
        return "viewJobVacancy" in self.driver.current_url

    def _select_from_dropdown(self, dropdown_locator, option_text):
        dropdown_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(dropdown_locator)
        )
        dropdown_element.click()

        option_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']/span[text()='{option_text}']"))
        )
        option_element.click()
        sleep(2)

    def select_job_title(self, job_title):
        self._select_from_dropdown(self.job_title_dropdown, job_title)

    def select_vacancy(self, vacancy):
        self._select_from_dropdown(self.vacancy_dropdown, vacancy)
    
    def select_hiring_manager(self, hiring_manager):
        self._select_from_dropdown(self.hiring_manager_dropdown, hiring_manager)

    def select_status(self, status):
        self._select_from_dropdown(self.status_dropdown, status)

    def click_search(self):
        search_button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button)
        )
        search_button_element.click()
        sleep(3)

    def get_search_results(self):
        results = []
        try:
            wait = WebDriverWait(self.driver, 15)
            table_container = wait.until(EC.visibility_of_element_located(self.results_table))
            rows = table_container.find_elements(By.XPATH, ".//div[@role='row'][position() > 1]")
            header_elements = table_container.find_elements(By.XPATH, ".//div[@role='rowgroup']/div[@role='row']/div/div")
            headers = [h.text.strip() for h in header_elements]

            for row in rows:
                row_data = row.find_elements(By.XPATH, ".//div[@role='cell']")
                cells = [cell.text.strip() for cell in row_data[1:]] 
                row_dict = dict(zip(headers, cells))
                results.append(row_dict)

            return results
        except Exception as e:
            print(f"Lỗi khi lấy kết quả tìm kiếm: {e}")
            return []