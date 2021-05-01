from locators import HomePageLocators
from pages.base_page import BasePage
from tests.test_utils import TestUtils
import validators


class HomePage(BasePage):

    def _verify_page(self):
        super()._verify_page()
        print("Weryfikacja z HomePage - nadpisująca _verify_page() z BasePage")
        title_txt = TestUtils.get_page_title_txt(self.driver)
        assert (title_txt.upper() == TestUtils.hp_title.upper())

    def _get_download_link(self):
        link = self.driver.find_element(*HomePageLocators.DOWNLOAD_LINK)
        return link

    def _get_full_versions_link(self):
        link = self.driver.find_element(*HomePageLocators.PELNE_WERSJE_LINK)
        return link

    def click_download_link(self):
        link = self._get_download_link()
        link.click()

    def click_full_versions_link(self):
        link = self._get_full_versions_link()
        link.click()

    def get_clickable_links(self):
        """Returns string list of urls found on Home Page"""
        links_to_click = []  # urls as string to be returned
        elements = self.driver.find_elements(*HomePageLocators.LINKS)
        images = self.driver.find_elements(*HomePageLocators.IMAGES)
        # images can also be links, so we add them:
        elements = [*elements, *images]
        # getting 'real' links only:
        for e in elements:
            if e.get_attribute('href') is not None:
                link_str = e.get_attribute('href')
                if validators.url(link_str):  # filtering out a few 'strange' urls + javascripts etc. ;)
                    links_to_click.append(link_str)
        # Duplicate removal:
        links_to_click = list(dict.fromkeys(links_to_click))
        #
        return links_to_click

