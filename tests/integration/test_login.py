import pytest
from pom.search_nav import SearchNav
from pom.homepage_nav import HomepageNav
from pom.login_nav import LoginNav
import time


@pytest.mark.usefixtures('setup')
class TestLogin:

    def test_login_bot_protect(self):
        homepage_nav = HomepageNav(self.driver)
        login_nav = LoginNav(self.driver)
        search_nav = SearchNav(self.driver)
        homepage_nav.get_login().click()
        login_nav.get_email_fild().send_keys('WRONGEMAIL@GMAIL.COM')
        login_nav.get_password_fild().send_keys('WRONGPASSWORD')
        login_nav.get_sign_in_button().click()
        assert "Sorry, it looks like there's a problem on our end. " \
               "For assistance, please call" in search_nav.get_notification_message().text

    def test_create_account(self):
        homepage_nav = HomepageNav(self.driver)
        login_nav = LoginNav(self.driver)
        search_nav = SearchNav(self.driver)
        homepage_nav.get_login().click()
        login_nav.get_create_account_button().click()
        login_nav.refresh_page()
        time.sleep(3)
