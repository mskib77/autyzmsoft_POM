from pages.download_page import DownloadPage
from pages.home_page import HomePage
from tests.base_test import BaseTest
from tests.test_utils import TestUtils
from time import sleep


class DownloadPageTest(BaseTest):

    def setUp(self):
        """Going to Download Page before each test"""
        super().setUp()
        # Bringing up download page:
        hp = HomePage(self.driver)
        hp.click_download_link()
        # Creating DownloadPage object for each test:
        self.dp = DownloadPage(self.driver)

    # Test case id DP_01
    # @unittest.skip
    def test_getting_download_links_with_correct_email(self):
        """Passed if:
        1. Text "WYSLANO LINKI NA ADRES" appears AND
        2. Address email appears as text on the screen. The address is the same as the address given in the form.
        """
        dp = self.dp
        dp.fill_email(TestUtils.good_email)
        sleep(1)
        dp.click_send_button()
        sleep(1)
        info_text = dp.get_mail_sent_info_text()
        addressee = dp.get_addressee_text()
        ok_1 = info_text.upper() == TestUtils.dp_info_text.upper()
        ok_2 = addressee == TestUtils.good_email
        # Determining the reason of negative test (if any):
        reason = []
        if not ok_1: reason.append("Lack of or Error in message about successfully sending email.")
        if not ok_2: reason.append("Email has been sent do different address than the one specified in the html form.")
        test_ok = ok_1 and ok_2
        self.assertTrue(test_ok, reason)

    # Test case id DP_02
    # @unittest.skip
    def test_getting_download_links_with_incorrect_email(self):
        """Passed if:
        Text "We wprowadzonych danych wystąpiły błędy" appears
        """
        dp = self.dp
        dp.fill_email(TestUtils.bad_email)
        sleep(1)
        dp.click_send_button()
        sleep(1)
        info = dp.get_error_info_text()
        test_ok = TestUtils.dp_error_info.upper() in info.upper()
        if not test_ok:
            TestUtils.screen_shot(self.driver, "Improper reaction to erroneous email")
        self.assertTrue(test_ok, "Improper reaction to erroneous email address.See screenshot.")
