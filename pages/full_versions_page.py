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
