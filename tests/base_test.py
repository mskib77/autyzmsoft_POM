import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from locators import HomePageLocators
from tests.test_utils import TestUtils


class BaseTest(unittest.TestCase):
    def setUp(self):
        print("setUp z BaseTest")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(TestUtils.WAIT_TIME)
        # self.driver = webdriver.Firefox()
        self.driver.get('https://autyzmsoft.pl')
        self.driver.maximize_window()
        self._dismiss_cookies()

    def _dismiss_cookies(self):
        """dismissing cookie message (if any) for more clarity on the screen"""
        print("W dismis_cookies z BaseTest")
        try:
            btn = self.driver.find_element(*HomePageLocators.COOKIE_BTN)
            btn.click()
        except NoSuchElementException:
            pass

    def tearDown(self):
        self.driver.quit()
