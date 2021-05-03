from selenium.webdriver.common.by import By


class HomePageLocators:
    DOWNLOAD_LINK = (By.PARTIAL_LINK_TEXT, "Pobieranie")
    PELNE_WERSJE_LINK = (By.PARTIAL_LINK_TEXT, "PEŁNE WERSJE")
    COOKIE_BTN = (By.ID, "catapultCookie")

    LINKS = (By.TAG_NAME, "a")
    IMAGES = (By.TAG_NAME, "img")

    # Elements to start and navigate in prof.Marcin Java Script application:
    WERSJE_ONLINE = (By.LINK_TEXT, "wersje online")
    PROF_MARCIN_JS = (By.PARTIAL_LINK_TEXT, "prof.Marcin")
    # STARTUJ = (By.XPATH, '//a[@href="plansza.html"]')
    # STARTUJ = (By.XPATH, '//section[@class="start"]')
    # STARTUJ = (By.XPATH, '//*[@id="container"]/section[2]/a')
    STARTUJ = (By.LINK_TEXT, "Startuj")


class DownloadPageLocators:
    EMAIL_FIELD = (By.ID, "id_Email")
    SEND_BTN = (By.ID, "bWyslij")
    ERROR_INFO = (By.ID, "email_err_1")
    MAIL_SENT_INFO = (By.ID, "links_sent_1")
    ADDRESSEE = (By.ID, 'email_sent_1')


class FullVersionsPageLocators:
    pass
