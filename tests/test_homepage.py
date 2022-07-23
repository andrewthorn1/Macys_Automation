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









