import pytest
from pom.search_nav import SearchNav
from pom.homepage_nav import HomepageNav

@pytest.mark.usefixtures('setup')
class TestBag:

    def test_add_to_bag_without_size(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.go_to_item_page()
        search_nav = SearchNav(self.driver)
        search_nav.get_add_to_bag_button().click()
        assert 'Please select a size.' in search_nav.get_notification_message().text

    def test_add_to_bag_with_size(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.go_to_item_page()
        search_nav = SearchNav(self.driver)
        search_nav.get_size_9_button().click()
        search_nav.get_add_to_bag_button().click()
        assert 'Please select a size.' not in search_nav.get_notification_message().text
