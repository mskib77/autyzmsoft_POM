import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators
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

    # Test case id HP_01   (HP stands for Home Page test)
    # @unittest.skip
    def test_download_page_appears(self):
        """ Fails if _verify_page() in DownloadPage class reports an error in its assert"""
        hp = self.hp
        hp.click_download_link()
        sleep(1)
        # this will instantiate DownloadPage object and will call its _verify_page() method:
        DownloadPage(self.driver)

    # Test case id HP_02
    # @unittest.skip
    def test_full_versions_page_appears(self):
        """ Fails if _verify_page() in FullVersions class reports an error in its assert"""
        hp = self.hp
        hp.click_full_versions_link()
        sleep(1)
        # this will instantiate FullVersionPage object and will call its _verify_page() method:
        FullVersionsPage(self.driver)

    # Test case id HP_03
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

    # Test case id HP_04
    # @unittest.skip
    def test_liczykropka_js_opens(self):
        """Test whether javascript application LiczyKropka opens"""
        """Passed if:
        1. 5 buttons appear AND
        2. a big number appears
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
            reasons.append("Big number did not appear on the screen.")

        test_ok = test_1_ok and test_2_ok

        if not test_ok:
            TestUtils.screen_shot(self.driver, "Error in liczykropka.js")

        self.assertTrue(test_ok, f"Error in liczykropka.js {reasons} See screenshot.")

    # Test case id HP_05
    # @unittest.skip
    def test_profmarcin_js_opens(self):
        """Test whether javascript application profMarcin opens"""
        """Passed if:
        1. 4 buttons appear AND
        2. a picture appear
        """
        NUM_BUTTONS = 4  # how many buttons should appear
        hp = self.hp
        hp.go_to_profmarcin_js()
        sleep(3)

        # Testing condition No 1:
        test_1_ok = False
        try:
            buttons_list = hp.get_buttons_list_from_profmarcin()
            if len(buttons_list) == NUM_BUTTONS:
                test_1_ok = True
        except NoSuchElementException:
            test_1_ok = False

        # Testing condition No 2:
        test_2_ok = hp.is_picture_visible_from_profmarcin()

        # Determining the reason(s) of negative test (if any):
        reasons = []
        if not test_1_ok:
            reasons.append(f"Number of buttons different than {NUM_BUTTONS} or buttons did not appear.")
        if not test_2_ok:
            reasons.append("Picture did not appear on the screen.")

        test_ok = test_1_ok and test_2_ok

        if not test_ok:
            TestUtils.screen_shot(self.driver, "Error in prof.Marcin.js")

        self.assertTrue(test_ok, f"Error in prof.Marcin.js {reasons} See screenshot.")

    def _is_font_size_greater_than(self, style, number):
        """ Auxiliary; accepts style as string, number as integer; style is css style of an element """
        """ Expects style to include font-size in %, otherwise rises exception """
        # parameters sanitization:
        if 'font-size:' not in style:
            raise ValueError(f"Improper method parameter. style parameter does not include 'font-size' substring")
        else:
            str_tmp = style.partition('font-size:')[2]
            if '%' not in str_tmp:
                raise ValueError(f"font-size is not in % (percentage units)")
        str_tmp = str_tmp.partition('%')[0]
        return int(str_tmp) > number

    def test_clicking_correct_button_in_profmarcin_js(self):
        """Passed if:
        1. All texts on buttons with improper words are printed in 'font-weigh: normal'; text on button(s) with proper
           word are printed in font-size > 100% AND
        2. There appear a text element under the picture. The element contains proper word AND
        3. Big green button with right arrow appears
        """
        hp = self.hp
        hp.go_to_profmarcin_js()
        sleep(3)
        buttons_list = hp.get_buttons_list_from_profmarcin()
        pict = hp.get_picture_from_profmarcin()
        # getting picture name (== the correct word on the buttons):
        style = pict.get_attribute('style')
        word = style.partition("zasoby/")[2].partition(".")[0]

        # clicking on the button containing 'word':
        for b in buttons_list:
            if b.text == word:
                b.click()
                break
        sleep(3)  # unnecessary, but better visual effect ;)

        # Testing condition No 1:
        test_1_ok = True
        for b in buttons_list:
            style = b.get_attribute('style')
            # print(b.text, " : ", style)
            if b.text != word:
                if 'font-weight: normal' not in style:
                    test_1_ok = False
                    break
            if b.text == word:
                if not self._is_font_size_greater_than(style, 100):
                    test_1_ok = False
                    break

        # Testing condition No 2:
        test_2_ok = False
        try:
            word_under_picture = hp.get_text_under_picture_profmarcin()
            if word_under_picture == word:
                test_2_ok = True
        except NoSuchElementException:
            test_2_ok = False

        # Testing condition No 3:
        green_btn = hp.get_green_button_from_profmarcin()
        style = green_btn.get_attribute("style")
        test_3_ok = 'transparent' not in style

        # Determining the reason(s) of negative test (if any):
        reasons = []
        if not test_1_ok: reasons.append("Buttons improperly blocked.")
        if not test_2_ok: reasons.append("Improper word or no word under the picture.")
        if not test_3_ok: reasons.append("Green button did not appear.")

        test_ok = test_1_ok and test_2_ok and test_3_ok

        if not test_ok:
            TestUtils.screen_shot(self.driver, "test_clicking_correct_button_in_profmarcin_js()")

        self.assertTrue(test_ok,
                        f"Test: test_clicking_correct_button_in_profmarcin_js(): Errors detected: {reasons} See screenshot.")

    def test_clicking_correct_button_in_liczykropka_js(self):
        """Passed if:
        1. All buttons with numbers except the proper one(s) are disabled AND
        2. Big green button with @ sign appears
        """
        hp = self.hp
        hp.go_to_liczykropka_js()
        sleep(3)
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(
            EC.presence_of_element_located(HomePageLocators.KLAWISZE_LK))
        # Clicking proper button:
        number = hp.get_number_from_liczykropka().text
        proper_btn = hp.get_button_with_number_from_liczykropka(number)
        proper_btn.click()
        sleep(3)

        # Testing condition No 1:
        test_1_ok = True
        buttons_list = hp.get_buttons_list_from_liczykropka()
        for b in buttons_list:
            # print(b.get_attribute('disabled'))
            b_value = b.get_attribute("wartosc")
            if b_value != number:
                if b.get_attribute('disabled') == 'false':
                    test_1_ok = False
                    break
            if b_value == number:
                if b.get_attribute('disabled') == 'true':
                    test_1_ok = False
                    break

        # Testing condition No 2:
        green_btn = hp.get_green_button_from_liczykropka()
        style = green_btn.get_attribute("style")
        test_2_ok = 'visible' in style

        # Determining the reason(s) of negative test (if any):
        reasons = []
        if not test_1_ok: reasons.append("Buttons improperly disabled.")
        if not test_2_ok: reasons.append("Green button did not appear.")

        test_ok = test_1_ok and test_2_ok

        if not test_ok:
            TestUtils.screen_shot(self.driver, "test_clicking_correct_button_in_liczykropka_js()")

        self.assertTrue(test_ok,
                        f"Test: test_clicking_correct_button_in_liczykropka_js(): Errors detected: {reasons} See screenshot.")
