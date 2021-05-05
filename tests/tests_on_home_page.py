import unittest

from pages.download_page import DownloadPage
from pages.home_page import HomePage
from pages.full_versions_page import FullVersionsPage
from tests.base_test import BaseTest
from time import sleep

from tests.test_utils import TestUtils


class HomePageTest(BaseTest):

    def setUp(self):
        """Creating HomePage object before each test"""
        super().setUp()
        self.hp = HomePage(self.driver)

    @unittest.skip
    def test_download_page_appears(self):
        """ Fails if _verify_page() in DownloadPage class reports an error in its assert"""
        hp = self.hp
        hp.click_download_link()
        sleep(1)
        # this will instantiate DownloadPage object and will call its _verify_page() method:
        DownloadPage(self.driver)

    @unittest.skip
    def test_full_versions_page_appears(self):
        """ Fails if _verify_page() in FullVersions class reports an error in its assert"""
        hp = self.hp
        hp.click_full_versions_link()
        sleep(1)
        # this will instantiate FullVersionPage object and will call its _verify_page() method:
        FullVersionsPage(self.driver)

    @unittest.skip
    def test_all_links_are_active(self):
        """Checking whether all links on the Home Page are active."""
        hp = self.hp
        clickable_links = hp.get_clickable_links()
        test_ok = True
        inactive_links = []
        for url_str in clickable_links:
            status_ok = TestUtils.get_link_status(url_str)
            if not status_ok:
                test_ok = False
                inactive_links.append(url_str)
        self.assertTrue(test_ok, f"Inactive links on Home Page detected: {inactive_links}")

    def test_prof_marcin_js_opens(self):
        """Test whether javascript application profMarcin opens"""
        hp = self.hp
        hp.go_to_prof_marcin_js()
        sleep(5)

    def test_liczykropka_js_opens(self):
        """Test whether javascript application LiczyKropka opens"""
        hp = self.hp
        hp.go_to_liczykropka_js()
        sleep(2)








