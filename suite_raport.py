import HtmlTestRunner

from /home/deveoper/.local/lib.python3.8/site-packages import HtmlTestRunner

import unittest
from tests.tests_on_home_page import HomePageTest
from tests.tests_on_fullversion_page import FullVersionsPageTest
from tests.tests_on_download_page import DownloadPageTest
import os

##############
# pip3 install html-testRunner
###########

# Pobierz z systemu katalog, w którym pracujemy
# (będziemy zapisywali wyniki testów)
dir = os.getcwd()

# Pobierz wszystkie testy z SearchText i HomePageTest
HomePageTests_text = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
FullVersionsPageTests_text = unittest.TestLoader().loadTestsFromTestCase(FullVersionsPageTest)
DownloadPAgeTests_text = unittest.TestLoader().loadTestsFromTestCase(DownloadPageTest)

# Stwórz Test Suita łączac testy
test_suite = unittest.TestSuite([HomePageTests_text, FullVersionsPageTests_text, DownloadPAgeTests_text])

# Uruchom suite
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ski_ski_example_test_results'))
