
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..base.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class RecruitmentPage(BasePage):
    recruitment = (By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']")
    vacancies_tab = (By.XPATH, "//a[text()='Vacancies']")
    add_vacancy = (By.XPATH, "//button[.=' Add ']")
    add_vacancy_header = (By.XPATH, "//h6[text()='Add Vacancy']")
    vacancy_name = (By.XPATH, "//label[text()='Vacancy Name']/following::input[1]")
    job_title_dropdown = (By.XPATH, "//div[@class='oxd-select-text--after']")
    description = (By.XPATH, "//label[text()='Description']/following::textarea[1]")
    hiring_manager_dropdown = (By.XPATH, "//label[text()='Hiring Manager']/following::div[contains(@class,'oxd-select-text-input')][1]")
    number_of_positions = (By.XPATH, "//label[text()='Number of Positions']/following::input[1]")
    active_checkbox = (By.XPATH, "//label[text()='Active']/following-sibling::div//input[@type='checkbox']")
    save = (By.XPATH, "//button[@type='submit' and .=' Save ']")
    cancel = (By.XPATH, "//button[.=' Cancel ']")
    user_dropdown = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    logout = (By.XPATH, "//a[text()='Logout']")
    search_button = (By.XPATH, "//button[@type='submit']")
    results_table = (By.XPATH, "//div[@class='oxd-table-body']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_recruitment(self):
        self.get_element(self.recruitment).click()

    def click_vacancies(self):
        self.get_element(self.vacancies_tab).click()

    def click_add_vacancy(self):
        self.get_element(self.add_vacancy).click()

    def is_add_vacancy_displayed(self):
        try:
            return self.get_element(self.add_vacancy_header).is_displayed()
        except:
            return False

    def input_vacancy_name(self, name):
        el = self.get_element(self.vacancy_name)
        el.clear()
        el.send_keys(name)

    def select_job_title(self, job_title):
        # Click vào dropdown đúng theo label
        dropdown = self.get_element((By.XPATH, "//label[text()='Job Title']/following::div[contains(@class,'oxd-select-text-input')][1]"))
        dropdown.click()
        # Chờ option xuất hiện và click vào option mong muốn
        option_xpath = f"//div[@role='listbox']//*[normalize-space(text())='{job_title}']"
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )
        option.click()

    def input_description(self, desc):
        el = self.get_element(self.description)
        el.clear()
        el.send_keys(desc)

    def select_hiring_manager(self, current_user):
        dropdown = self.get_element(self.hiring_manager_dropdown)
        dropdown.click()
        # Use ActionChains to select the first suggestion (simulate ARROW_DOWN + ENTER)
        actions = ActionChains(self.driver)
        actions.move_to_element(dropdown)
        actions.click()
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def input_number_of_positions(self, num):
        el = self.get_element(self.number_of_positions)
        el.clear()
        el.send_keys(str(num))

    def set_active(self, value: bool):
        cb = self.get_element(self.active_checkbox)
        if cb.is_selected() != value:
            cb.click()

    def set_publish_checkbox(self, label: str, value: bool):
        cb = self.get_element((By.XPATH, f"//label[contains(text(),'{label}')]/following::input[@type='checkbox'][1]"))
        if cb.is_selected() != value:
            cb.click()

    def click_save_vacancy(self):
        self.get_element(self.save).click()

    def is_edit_vacancy_displayed(self):
        try:
            return self.get_element(self.edit_vacancy_header).is_displayed()
        except:
            return False

    def click_cancel_vacancy(self):
        self.get_element(self.cancel).click()

    def is_vacancies_displayed(self):
        return "viewJobVacancy" in self.driver.current_url

    def click_search(self):
        self.get_element(self.search_button).click()

    def get_search_results(self):
        results = []
        try:
            table = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.results_table)
            )
            rows = table.find_elements(By.XPATH, "./div")
            for row in rows:
                cells = row.find_elements(By.XPATH, ".//div[@role='cell']")
                if len(cells) >= 3:
                    results.append({
                        "Job Title": cells[1].text.strip(),
                        "Vacancy Name": cells[2].text.strip(),
                    })
            return results
        except Exception:
            return []

    def logout(self):
        self.get_element(self.user_dropdown).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.logout)
        ).click()