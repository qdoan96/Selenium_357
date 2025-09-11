import pytest
from automation_framework.tests.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin(LoginPage):
    def test_login_valid(self):
        assert self.test_login_valid()

    def test_login_invalid(self):
        assert self.test_login_invalid()
