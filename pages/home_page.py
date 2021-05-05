from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

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

    def _hover_over_online_versions(self):
        el_to_hover = self.driver.find_element(*HomePageLocators.WERSJE_ONLINE)
        action = ActionChains(self.driver)
        action.move_to_element(el_to_hover).perform()

    def _get_prof_marcin_js_link(self):
        link = self.driver.find_element(*HomePageLocators.PROF_MARCIN_JS)
        return link

    def _get_liczykropka_js_link(self):
        link = self.driver.find_element(*HomePageLocators.LICZYKROPKA_JS)
        return link

    def go_to_prof_marcin_js(self):
        self._hover_over_online_versions()
        sleep(2)
        link = self._get_prof_marcin_js_link()
        link.click()
        sleep(5)
        print("szukam bstartuj....")

        # frame = self.driver.find_element_by_xpath('//*[@id="gsft_main"]')
        # self.driver.switch_to.frame(frame)


        b_startuj = self.driver.find_element(*HomePageLocators.STARTUJ_PROF_MARCIN)
        print("PO szukam bstartuj....")
        sleep(5)
        b_startuj.click()
        sleep(5)

    def go_to_liczykropka_js(self):
        self._hover_over_online_versions()
        sleep(4)
        link = self._get_liczykropka_js_link()
        link.click()
        sleep(5)

        # self.driver.quit()
        sleep(2)
        # self.driver = webdriver.Chrome()
        self.driver.get('https://autyzmsoft.pl/js/liczykropka/liczykropka.html')
        self.driver.maximize_window()
        sleep(3)


        bStartuj = self.driver.find_element(*HomePageLocators.STARTUJ_LICZYKROPKA)
        bStartuj.click()
        sleep(4)




