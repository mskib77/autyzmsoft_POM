from locators import HomePageLocators
from pages.base_page import BasePage
from tests.test_utils import TestUtils


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
        links_to_click = []
        elements = self.driver.find_elements(*HomePageLocators.VISIBLE_LINKS)
        images = self.driver.find_elements(*HomePageLocators.IMAGES)
        # images can also be links:
        elements = [*elements, *images]
        # only 'real' links:
        for e in elements:
            if e.get_attribute('href') is not None:
                links_to_click.append(e)

        # for i in range(0, len(links_to_click)):
        #     print(i, links_to_click[i].get_attribute('href'))

        # try:
        #     if elements[i].get_attribute('href') is not None:
        #         links_to_click.append(elements[i])
        #         print(i, " ", elements[i].text, " | ", elements[i].get_attribute('href'), " Licznosc listy links_to_click = ", len(links_to_click))
        # except Exception as e:
        #     print(f"wyjatek przy {i} , {e.__class__}")

        return links_to_click
