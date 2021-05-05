import os
from datetime import datetime
from selenium.webdriver.common.by import By
from urllib.request import urlopen


class TestUtils:
    WAIT_TIME = 25  # system-wide implicit wait
    # Pages' titles (same location on each page):
    PAGE_TITLE = (By.XPATH, '//*[@id = "content"]/div[1]/h1')
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
    def get_page_title_txt(cls, driver):
        page_title = driver.find_element(*cls.PAGE_TITLE)
        return page_title.text

    @classmethod
    def screen_shot(cls, driver, file_name):
        time_now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        store_file = f'{os.getcwd()}/screenshots/' + time_now + '_' + file_name + '.png'
        # print(f"Sciezka: {store_file}")
        driver.get_screenshot_as_file(store_file)

    @classmethod
    def get_link_status(cls, url_param):
        """Returns True if url (given as string) points to an active address"""
        try:
            urlopen(url_param)
            print(f"{url_param} - ok")
            return True
        except:
            print(f"{url_param} - problem....")
            return False
