import time

import pytest
from pom.search_nav import SearchNav
from pom.homepage_nav import HomepageNav
from selenium.webdriver import Keys

@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validating Header Nav Links Text'

    def test_search(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.get_search().send_keys('Men shoes')
        homepage_nav.get_search().send_keys(Keys.RETURN)
        search_nav = SearchNav(self.driver)
        search_first_item = search_nav.get_first_item()
        assert search_first_item is not None
        print(search_first_item.text)

    def test_search_not_found(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.get_search().send_keys(']]')
        homepage_nav.get_search().send_keys(Keys.RETURN)
        search_nav = SearchNav(self.driver)
        search_not_found = search_nav.get_not_found_message()
        assert 'We couldn’t find a match for your search.' in search_not_found.text








