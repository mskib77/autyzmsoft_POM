import unittest

from pages.download_page import DownloadPage
from pages.home_page import HomePage
from pages.full_versions_page import FullVersionsPage
from tests.base_test import BaseTest
from time import sleep


class HomePageTest(BaseTest):

    def setUp(self):
        """Creating HomePage object begore each test"""
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

    # @unittest.skip
    def test_all_links_active(self):
        """Checking whether all links on the Home Page are active."""
        hp = self.hp
        hp.get_clickable_links()

