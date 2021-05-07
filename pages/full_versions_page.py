from locators import FullVersionsPageLocators
from pages.base_page import BasePage
from tests.test_utils import TestUtils


class FullVersionsPage(BasePage):

    def _verify_page(self):
        super()._verify_page()
        print("Weryfikacja z FullVersionPage - nadpisująca _verify_page() z BasePage")
        # title_txt = self._get_page_title_txt()
        title_txt = TestUtils.get_page_title_txt(self.driver)
        assert (title_txt.upper() == TestUtils.fw_title)

    def get_buy_button1(self):
        btn = self.driver.find_element(*FullVersionsPageLocators.BUY_BUTTON_1)
        return btn

    def get_buy_button2(self):
        btn = self.driver.find_element(*FullVersionsPageLocators.BUY_BUTTON_2)
        return btn
