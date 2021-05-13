from locators import FullVersionsPageLocators
from pages.base_page import BasePage
from tests.test_utils import TestUtils


class FullVersionsPage(BasePage):

    def _verify_page(self):
        super()._verify_page()
        print("Weryfikacja z FullVersionPage - nadpisująca _verify_page() z BasePage")
        # title_txt = self._get_page_title_txt()
        title_txt = TestUtils.get_page_title_txt(self.driver)
        assert (title_txt.upper() == TestUtils.fv_title)

    def get_order_button1(self):
        btn = self.driver.find_element(*FullVersionsPageLocators.ORDER_BUTTON_1)
        return btn

    def get_order_button2(self):
        btn = self.driver.find_element(*FullVersionsPageLocators.ORDER_BUTTON_2)
        return btn

    def get_all_checkboxes_list(self):
        cb_list = self.driver.find_elements(*FullVersionsPageLocators.ALL_CHECKBOXES)
        return cb_list

    def get_checkbox_of_number(self, no):
        cbl = self.get_all_checkboxes_list()
        return cbl[no]



