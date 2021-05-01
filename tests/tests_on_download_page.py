from pages.download_page import DownloadPage
from tests.base_test import BaseTest
from tests.test_utils import TestUtils
from time import sleep


class DownloadPageTest(BaseTest):

    def setUp(self):
        """Going to Download Page before each test"""
        super().setUp()
        TestUtils.go_to_download_page(self.driver)

    def test_getting_download_links_with_correct_email(self):
        dp = DownloadPage(self.driver)
        dp.fill_email(TestUtils.good_email)
        sleep(1)
        dp.click_send_button()
        sleep(1)
        info_text = dp.get_mail_sent_info_text()
        addressee = dp.get_addressee_text()
        ok_1 = info_text.upper() in TestUtils.dp_info_text.upper()
        ok_2 = addressee == TestUtils.good_email
        # Determining the reason of negative test (if any):
        reason = []
        if not ok_1: reason.append("Lack of or Error in message about successfully sending email.")
        if not ok_2: reason.append("Email has been sent do different address than the one specified in the html form.")
        test_ok = ok_1 and ok_2
        self.assertTrue(test_ok, reason)

    def test_getting_download_links_with_incorrect_email(self):
        dp = DownloadPage(self.driver)
        dp.fill_email(TestUtils.bad_email)
        sleep(1)
        dp.click_send_button()
        sleep(1)
        info = dp.get_error_info_text()
        test_ok = TestUtils.dp_error_info.upper() in info.upper()
        self.assertTrue(test_ok, "Improper reaction to erroneous email address.")



