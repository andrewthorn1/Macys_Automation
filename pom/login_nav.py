from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class LoginNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__email_fild_locator: str = '#email'
        self.__password_fild_locator: str = '#pw-input'
        self.__sign_in_button_locator: str = '#sign-in'
        self.__create_account_button_locator: str = '#standard-sign-up'

    def get_email_fild(self):
        return self.is_visible('css', self.__email_fild_locator)

    def get_password_fild(self):
        return self.is_visible('css', self.__password_fild_locator)

    def get_sign_in_button(self):
        return self.is_visible('css', self.__sign_in_button_locator)

    def get_create_account_button(self):
        return self.is_visible('css', self.__create_account_button_locator)

    def refresh_page(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
