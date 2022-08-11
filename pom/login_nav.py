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
        self.__ca_first_name_fild_locator: str = '#ca-profile-firstname'
        self.__ca_last_name_fild_locator: str = '#ca-profile-lastname'
        self.__ca_email_fild_locator: str = '#ca-profile-email'
        self.__ca_password_fild_locator: str = '#ca-profile-password'
        self.__ca_birthday_month_locator: str = '//select[@id="ca-profile-birth-month"]/option[text()="January"]'
        self.__ca_birthday_day_locator: str = '//select[@id="ca-profile-birth-day"]/option[text()="01"]'
        self.__ca_button_locator: str = '#ca-profile-submit'
        self.__notification_message_locator: str = '//div[@class="show"]//*[@class="notification-body"]'


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

    def get_ca_first_name_fild(self):
        return self.is_visible('css', self.__ca_first_name_fild_locator)

    def get_ca_last_name_fild(self):
        return self.is_visible('css', self.__ca_last_name_fild_locator)

    def get_ca_email_fild(self):
        return self.is_visible('css', self.__ca_email_fild_locator)

    def get_ca_password_fild(self):
        return self.is_visible('css', self.__ca_password_fild_locator)

    def get_ca_birthday_month(self):
        return self.is_present('xpath', self.__ca_birthday_month_locator)

    def get_ca_birthday_day(self):
        return self.is_present('xpath', self.__ca_birthday_day_locator)

    def get_ca_button(self):
        return self.is_visible('css', self.__ca_button_locator)

    def get_ca_notification_message(self) -> WebElement:
        return self.is_present('xpath', self.__notification_message_locator)

