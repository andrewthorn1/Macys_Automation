import pytest
from pom.search_nav import SearchNav
from pom.homepage_nav import HomepageNav
from selenium.webdriver import Keys

@pytest.mark.usefixtures('setup')
class TestSearch:

    def test_search(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.get_search().send_keys('Men shoes')
        homepage_nav.get_search().send_keys(Keys.RETURN)
        search_nav = SearchNav(self.driver)
        search_first_item = search_nav.get_first_item()
        assert search_first_item is not None

    def test_search_not_found(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.get_search().send_keys(']]')
        homepage_nav.get_search().send_keys(Keys.RETURN)
        search_nav = SearchNav(self.driver)
        search_not_found = search_nav.get_not_found_message()
        assert 'We couldn’t find a match for your search.' in search_not_found.text








