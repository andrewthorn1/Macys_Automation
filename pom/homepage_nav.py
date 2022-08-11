from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from base.utils import Utils
from selenium.webdriver.common.keys import Keys
import time

from pom.search_nav import SearchNav


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#mainNavigationFobs>li'
        self.__search_locator: str = '//*[@id="globalSearchInputField"]'
        self.__sign_in_locator: str = 'Sign In'
        self.NAV_LINK_TEXT = 'Women,Men,Kids,Home,Beauty,Shoes,Handbags,Jewelry,' \
                             'Furniture,Toys,Gifts,Own Your Style,Sale'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)

    def get_nav_link_by_name(self, name: str) -> WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)

    def get_search(self) -> WebElement:
        return self.is_visible('xpath', self.__search_locator, 'Search')

    def go_to_item_page(self):
        self.get_search().send_keys('Men shoes')
        self.get_search().send_keys(Keys.RETURN)
        search_nav = SearchNav(self.driver)
        search_nav.get_first_item().click()
        time.sleep(1)
        search_nav.driver.delete_all_cookies()
        search_nav.driver.refresh()
        time.sleep(3)

    def get_login(self) -> WebElement:
        return self.is_visible('link_text', self.__sign_in_locator, 'Sign In')


