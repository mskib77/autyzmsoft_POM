import os
from datetime import datetime
from selenium.webdriver.common.by import By
from urllib.request import urlopen


class TestUtils:
    # system-wide implicit wait:
    WAIT_TIME = 5

    # website header:
    WEBSITE_HEADER = "Programy komputerowe dla dziecka autystycznego"

    # Pages' titles (same location on each page):
    PAGE_TITLE = (By.XPATH, '//*[@id = "content"]/div[1]/h1')
    hp_title = "STRONA GŁÓWNA"
    dp_title = "DO POBRANIA"
    fv_title = "PEŁNE WERSJE"
    od_title = "SZCZEGÓŁY ZAMÓWIENIA"

    # email testing:
    good_email = "mskib77@gmail.com"
    bad_email = "mskib77*gmail.com"

    # info error on download page:
    dp_error_info = "We wprowadzonych danych wystąpiły błędy"
    # info text about email that has been sent correctly:
    dp_info_text = "WYSLANO LINKI NA ADRES"

    # alert text on Full Versions page:
    ALERT_TEXT = "Nie zaznaczyłeś niczego"

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
