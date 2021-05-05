from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def _hover_over(self, element):
        el = self.driver.find_element(*element)
        action = ActionChains(self.driver)
        action.move_to_element(el).perform()

    def _get_prof_marcin_js_link(self):
        link = self.driver.find_element(*HomePageLocators.PROF_MARCIN_JS)
        return link

    def _get_liczykropka_js_link(self):
        link = self.driver.find_element(*HomePageLocators.LICZYKROPKA_JS)
        return link

    def _start_js_app_settings_screen(self, link_to_app):
        """Opens the first screen of Java Script app given in the link_to_app parameter"""
        """Used to start the js applications from there by finding and clicking links"""
        self._hover_over(HomePageLocators.WERSJE_ONLINE)  # uncovering menu items
        self._hover_over(link_to_app)  # unnecessary, but better visual effect ;)
        link = WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(link_to_app))
        # Page needs to be reloaded, otherwise selenium can't locate elements:
        url = link.get_attribute('href')
        self.driver.get(url)

    def go_to_prof_marcin_js(self):
        self._start_js_app_settings_screen(HomePageLocators.PROF_MARCIN_JS)
        bStartuj = self.driver.find_element(*HomePageLocators.STARTUJ_PROF_MARCIN)
        bStartuj.click()

    def get_buttons_list_from_liczykropka(self):
        blist = self.driver.find_elements(*HomePageLocators.KLAWISZE)
        return blist

    def get_number_from_liczykropka(self):
        number = self.driver.find_element(*HomePageLocators.LICZBA)
        return number

    def go_to_liczykropka_js(self):
        self._start_js_app_settings_screen(HomePageLocators.LICZYKROPKA_JS)
        bStartuj = self.driver.find_element(*HomePageLocators.STARTUJ_LICZYKROPKA)
        bStartuj.click()




