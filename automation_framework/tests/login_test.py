
from ..base.base_test import BaseTest
from ..pages.login_page_new import LoginPage
from ..pages.dashboard_page import DashboardPage
from time import sleep
import pytest
@pytest.mark.usefixtures("setup")
class TestLogin(BaseTest):
    def test_login(self):
        login_page = LoginPage(self.driver) # khoi tao login_page
        login_page.login('Admin', 'admin123') # goi ham login tu login_page
        dashboard_page = DashboardPage(self.driver) # khoi tao dashboard_page
        dashboard_page.is_dashboard_displayed()
        

    