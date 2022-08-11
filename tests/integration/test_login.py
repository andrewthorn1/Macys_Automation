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

    def test_create_account_bot_protect(self):
        homepage_nav = HomepageNav(self.driver)
        login_nav = LoginNav(self.driver)
        search_nav = SearchNav(self.driver)
        homepage_nav.get_login().click()
        login_nav.get_create_account_button().click()
        login_nav.refresh_page()
        login_nav.get_ca_first_name_fild().send_keys("Test Name")
        login_nav.get_ca_last_name_fild().send_keys("Test Surname")
        login_nav.get_ca_email_fild().send_keys("Testemail@gmail.com")
        login_nav.get_ca_password_fild().send_keys("Testpassword1")
        login_nav.get_ca_birthday_month().click()
        login_nav.get_ca_birthday_day().click()
        login_nav.get_ca_button().click()
        assert "We're sorry, but we cannot display your information" \
               " at this time." in login_nav.get_ca_notification_message().text
