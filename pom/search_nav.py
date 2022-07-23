from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from base.utils import Utils


class SearchNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__first_item_locator: str = '//*[@class="cell"]//*//li'
        self.__not_found_message_locator: str = '//*[@id="resultsFoundMessage"]'

    def get_first_item(self) -> WebElement:
        return self.is_visible('xpath', self.__first_item_locator)

    def get_not_found_message(self) -> WebElement:
        return self.is_visible('xpath', self.__not_found_message_locator)

