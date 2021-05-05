from selenium.webdriver.common.by import By


class HomePageLocators:
    DOWNLOAD_LINK = (By.PARTIAL_LINK_TEXT, "Pobieranie")
    PELNE_WERSJE_LINK = (By.PARTIAL_LINK_TEXT, "PEŁNE WERSJE")
    COOKIE_BTN = (By.ID, "catapultCookie")

    LINKS = (By.TAG_NAME, "a")
    IMAGES = (By.TAG_NAME, "img")

    # Links to start settings screens of some Java Script application:
    WERSJE_ONLINE = (By.LINK_TEXT, "wersje online")  # to hover over to uncover ;)
    PROF_MARCIN_JS = (By.LINK_TEXT, "prof.Marcin")  # to start prof.Marcin settings page
    LICZYKROPKA_JS = (By.LINK_TEXT, "LiczyKropka")  # to start LiczyKropka settings page

    # Links to start js applications:
    STARTUJ_PROF_MARCIN = (By.ID, "b_start_id")
    STARTUJ_LICZYKROPKA = (By.ID, "bStartuj")

    # elements on Liczykropka js application:
    LICZBA = (By.XPATH, '//div[@class="div-liczba-klasa div-liczba-klasa-growing"]')
    KLAWISZE = (By.CLASS_NAME, "klawisz-klasa")


class DownloadPageLocators:
    EMAIL_FIELD = (By.ID, "id_Email")
    SEND_BTN = (By.ID, "bWyslij")
    ERROR_INFO = (By.ID, "email_err_1")
    MAIL_SENT_INFO = (By.ID, "links_sent_1")
    ADDRESSEE = (By.ID, 'email_sent_1')


class FullVersionsPageLocators:
    pass
