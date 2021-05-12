from tests.test_utils import TestUtils


class BasePage:

    def __init__(self, driver):
        print("Metoda inicjalizacyjna z BasePage")
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        print("Weryfikacja z BasePage")
        # assert "Programy komputerowe dla dziecka autystycznego" in self.driver.title
        assert TestUtils.WEBSITE_HEADER in self.driver.title

