import time

import pytest
from pom.search_nav import SearchNav
from pom.homepage_nav import HomepageNav
from selenium.webdriver import Keys

@pytest.mark.usefixtures('setup')
class TestBag:

    def test_add_to_bag_without_size(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.go_to_item_page()
        search_nav = SearchNav(self.driver)
        search_nav.get_add_to_bag_button().click()
        assert 'Please select a size.' in search_nav.get_notification_message().text
