from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from base.utils import Utils


class SearchNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__first_item_locator: str = '//*[@class="cell"]//*//li'
        self.__add_to_bag_locator: str = '//*[@data-auto="add-to-bag"]'
        self.__notification_message_locator: str = '//*[@class="notification-body"]'
        self.__not_found_message_locator: str = '//*[@id="resultsFoundMessage"]'

    def get_first_item(self) -> WebElement:
        return self.is_visible('xpath', self.__first_item_locator)

    def get_not_found_message(self) -> WebElement:
        return self.is_visible('xpath', self.__not_found_message_locator)

    def get_add_to_bag_button(self) -> WebElement:
        return self.is_visible('xpath', self.__add_to_bag_locator)

    def get_notification_message(self) -> WebElement:
        return self.is_visible('xpath', self.__notification_message_locator)


