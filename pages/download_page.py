from pages.base_page import BasePage
from locators import DownloadPageLocators
from tests.test_utils import TestUtils


class DownloadPage(BasePage):

    def _verify_page(self):
        super()._verify_page()
        print("Weryfikacja z DownloadPage - nadpisująca _verify_page() z BasePage")
        title_txt = TestUtils.get_page_title_txt(self.driver)
        assert (title_txt.upper() == TestUtils.dp_title)

    def _get_email_field(self):
        field = self.driver.find_element(*DownloadPageLocators.EMAIL_FIELD)
        return field

    def _get_send_btn(self):
        btn = self.driver.find_element(*DownloadPageLocators.SEND_BTN)
        return btn

    def fill_email(self, email_text):
        field = self._get_email_field()
        field.send_keys(email_text)

    def click_send_button(self):
        btn = self._get_send_btn()
        btn.click()

    def get_error_info_text(self):
        info = self.driver.find_element(*DownloadPageLocators.ERROR_INFO)
        return info.text

    def get_mail_sent_info_text(self):
        info = self.driver.find_element(*DownloadPageLocators.MAIL_SENT_INFO)
        return info.text

    def get_addressee_text(self):
        info = self.driver.find_element(*DownloadPageLocators.ADDRESSEE)
        return info.text
