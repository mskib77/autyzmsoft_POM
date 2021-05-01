from selenium.webdriver.common.by import By


class HomePageLocators:
    DOWNLOAD_LINK = (By.PARTIAL_LINK_TEXT, "Pobieranie")
    PELNE_WERSJE_LINK = (By.PARTIAL_LINK_TEXT, "PEŁNE WERSJE")
    COOKIE_BTN = (By.ID, "catapultCookie")

    VISIBLE_LINKS = (By.TAG_NAME, "a")
    IMAGES = (By.TAG_NAME, "img")




class DownloadPageLocators:
    EMAIL_FIELD = (By.ID, "id_Email")
    SEND_BTN = (By.ID, "bWyslij")
    ERROR_INFO = (By.ID, "email_err_1")
    MAIL_SENT_INFO = (By.ID, "links_sent_1")
    ADDRESSEE = (By.ID, 'email_sent_1')


class FullVersionsPageLocators:
    pass