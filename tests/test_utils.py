from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage


class TestUtils:

    WAIT_TIME = 5  # system-wide implicit wait
    # Pages' titles:
    PAGE_TITLE = (By.XPATH, '// *[ @ id = "content"] / div[1] / h1')  # same location on each page
    hp_title = "STRONA GŁÓWNA"
    dp_title = "DO POBRANIA"
    fw_title = "PEŁNE WERSJE"

    good_email = "mskib77@gmail.com"
    bad_email = "mskib77*gmail.com"

    # error info on download page:
    dp_error_info = "We wprowadzonych danych wystąpiły błędy"
    # info text about email sent correctly:
    dp_info_text = "WYSLANO LINKI NA ADRES"

    @classmethod
    def go_to_download_page(cls, driver):
        """ Auxiliary; brings up the Download Page. """
        WebDriverWait(driver, cls.WAIT_TIME).until(EC.presence_of_element_located(cls.PAGE_TITLE))
        hp = HomePage(driver)
        hp.click_download_link()
        sleep(3)

    @classmethod
    def get_page_title_txt(cls, driver):
        page_title = driver.find_element(*cls.PAGE_TITLE)
        return page_title.txt

