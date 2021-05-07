from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.full_versions_page import FullVersionsPage
from pages.home_page import HomePage
from tests.base_test import BaseTest
from tests.test_utils import TestUtils
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
        self.fw = FullVersionsPage(self.driver)

    # dtt as there are 2 buttons that should have same effect
    @data(1, 3)
    def test_click_buy_buttons_without_choosing_items(self, button_number):

        # parameter sanitization:
        if button_number not in range(1, 3):
            raise ValueError(f"Improper method parameter. Must be 1 or 2 but {button_number} was given!")

        fw = self.fw
        if button_number == 1: btn = fw.get_buy_button1()
        if button_number == 2: btn = fw.get_buy_button2()
        btn.click()
        sleep(2)  # unnecessary, for better visual effect ;)

        try:
            WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.alert_is_present())
            test_ok = True
            # dismissing the alert, unnecessary :
            # alert = self.driver.switch_to.alert
            # alert.accept()
        except TimeoutException:
            # print("alert does not Exist in page")
            test_ok = False

        self.assertTrue(test_ok, "Alert does not exist in page!")


