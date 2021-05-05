import unittest

from pages.download_page import DownloadPage
from pages.home_page import HomePage
from pages.full_versions_page import FullVersionsPage
from tests.base_test import BaseTest
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from tests.test_utils import TestUtils


class HomePageTest(BaseTest):

    def setUp(self):
        """Creating HomePage object before each test"""
        super().setUp()
        self.hp = HomePage(self.driver)

    # @unittest.skip
    def test_download_page_appears(self):
        """ Fails if _verify_page() in DownloadPage class reports an error in its assert"""
        hp = self.hp
        hp.click_download_link()
        sleep(1)
        # this will instantiate DownloadPage object and will call its _verify_page() method:
        DownloadPage(self.driver)

    # @unittest.skip
    def test_full_versions_page_appears(self):
        """ Fails if _verify_page() in FullVersions class reports an error in its assert"""
        hp = self.hp
        hp.click_full_versions_link()
        sleep(1)
        # this will instantiate FullVersionPage object and will call its _verify_page() method:
        FullVersionsPage(self.driver)

    # @unittest.skip
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

    # # @unittest.skip
    def test_liczykropka_js_opens(self):
        """Test whether javascript application LiczyKropka opens"""
        """Passed if:
        1. a big number appears AND
        2. 5 buttons appear
        """
        NUM_BUTTONS = 5  # how many buttons should appear
        hp = self.hp
        hp.go_to_liczykropka_js()
        sleep(3)

        # Testing condition No 1:
        test_1_ok = False
        try:
            buttons_list = hp.get_buttons_list_from_liczykropka()
            if len(buttons_list) == NUM_BUTTONS:
                test_1_ok = True
        except NoSuchElementException:
            test_1_ok = False

        # Testing condition No 2:
        test_2_ok = False
        try:
            number = hp.get_number_from_liczykropka()
            if number.text.isnumeric():
                test_2_ok = True
            # print(f"Liczba: {number.text}")
        except NoSuchElementException:
            test_2_ok = False

        # Determining the reason of negative test (if any):
        reasons = []
        if not test_1_ok:
            reasons.append(f"Number of buttons different than {NUM_BUTTONS} or buttons did not appear.")
        if not test_2_ok:
            reasons.append(f"Big number did not appear on the screen.")

        test_ok = test_1_ok and test_2_ok

        if not test_ok:
            TestUtils.screen_shot(self.driver, "Error in liczykropka.js")

        self.assertTrue(test_ok, f"Error in liczykropka.js {reasons} See picture.")

    # # @unittest.skip
    def test_prof_marcin_js_opens(self):
        """Test whether javascript application profMarcin opens"""
        hp = self.hp
        hp.go_to_prof_marcin_js()
        sleep(3)

