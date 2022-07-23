import time

import pytest

from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validating Header Nav Links Text'


        # for indx in range(13):
        #     homepage_nav.get_nav_links()[indx].click()
        #     homepage_nav.driver.delete_cookie('ak_bmsc')




