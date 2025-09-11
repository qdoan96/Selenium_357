
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver # gan driver tu base_test.py

    def is_dashboard_displayed(self):
        return "dashboard" in self.driver.current_url # action #