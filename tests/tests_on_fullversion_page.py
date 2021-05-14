import unittest
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.full_versions_page import FullVersionsPage
from pages.home_page import HomePage
from pages.order_detail_page import OrderDetailsPage
from tests.base_test import BaseTest
from tests.test_utils import TestUtils
from random import randint
from ddt import ddt, data


@ddt
class FullVersionsPageTest(BaseTest):

    def setUp(self):
        """Going to FullVersions Page before each test"""
        super().setUp()
        # Bringing up FullVersions page:
        hp = HomePage(self.driver)
        hp.click_full_versions_link()
        # Creating FullVersionsPage object for each test:
        self.fv = FullVersionsPage(self.driver)

    def _determine_button_to_click(self, number):
        """Auxiliary; returns button 1 or 2 as specified by the 'number' parameter"""
        # parameters sanitization:
        if number not in range(1, 3):
            raise ValueError(f"Improper method parameter. Must be 1 or 2 but {number} was given!")
        fv = self.fv
        if number == 1: btn = fv.get_order_button1()
        if number == 2: btn = fv.get_order_button2()
        return btn

    # Test case id FV_01
    # @unittest.skip
    @data(1, 2)
    def test_click_order_buttons_without_choosing_items(self, button_number):
        """Passed if Alert window appears"""
        """ddt is used as there are 2 buttons that clicking on them should have same effect"""

        btn = self._determine_button_to_click(button_number)
        btn.click()
        sleep(2)  # unnecessary, for better visual effect ;)

        try:
            WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            txt = alert.text
            test_ok = TestUtils.ALERT_TEXT.upper() in txt.upper()
            # dismissing the alert (unnecessary) :
            # alert.accept()
        except TimeoutException:
            test_ok = False

        self.assertTrue(test_ok, "Alert does not exist in page!")

    # Test case id FV_02
    # @unittest.skip
    @data(1, 2)
    def test_click_order_buttons_after_choosing_items(self, button_number):
        """Passed if Order Details page appears"""
        """ddt is used as there are 2 buttons that clicking on them should have same effect"""

        fv = self.fv
        cb_list = fv.get_all_checkboxes_list()
        # clicking on randomly chosen checkbox:
        max_val = len(cb_list) - 1
        rnd = randint(0, max_val)
        cb = cb_list[rnd]
        ActionChains(self.driver).move_to_element(cb).perform()
        self.driver.execute_script("window.scrollBy(0, 150)")  # sometimes move_to_element is not enough to fully show the element
        cb.click()
        # print(f"element {rnd} isDisplayed: {cb.is_displayed()}")
        # print(f"element {rnd} isSelected: {cb.is_selected()}")
        # Bring up the Order Details page:
        btn = self._determine_button_to_click(button_number)
        sleep(1)    # unnecessary, for better visual effect
        btn.click()
        sleep(1)    # this is necessary for the html page to open
        # This will instantiate OrderDetailsPage object and will call its _verify_page() method (error, if any,
        # will be reported by it):
        OrderDetailsPage(self.driver)



