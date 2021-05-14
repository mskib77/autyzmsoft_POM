<<<<<<< HEAD
import unittest
from HtmlTestRunner import HTMLTestRunner
=======
import HtmlTestRunner

from /home/deveoper/.local/lib.python3.8/site-packages import HtmlTestRunner

import unittest
>>>>>>> 53f9eb1ba396d1a82d624cc369bcd329c6081017
from tests.tests_on_home_page import HomePageTest
from tests.tests_on_fullversion_page import FullVersionsPageTest
from tests.tests_on_download_page import DownloadPageTest
import os

##############
# pip3 install html-testRunner
###########

# Pobierz z systemu katalog, w którym pracujemy
<<<<<<< HEAD
# (będziemy tam zapisywali wyniki testów)
default_dir = os.getcwd()

# Pobierz wszystkie testy z SearchText i HomePageTest
HP_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
DP_tests = unittest.TestLoader().loadTestsFromTestCase(DownloadPageTest)
FV_tests = unittest.TestLoader().loadTestsFromTestCase(FullVersionsPageTest)

# Stwórz Test Suita łączac testy:
test_suite = unittest.TestSuite([HP_tests, DP_tests, FV_tests])
# test_suite = unittest.TestSuite([DP_tests])

# Uruchomenie suite:
if __name__ == "__main__":
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='tests_results', verbosity=2)) -> problemy....
    wyniki = f"{default_dir}/test_results"
    runner = HTMLTestRunner(output=wyniki, verbosity=2)
    runner.run(test_suite)
=======
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
>>>>>>> 53f9eb1ba396d1a82d624cc369bcd329c6081017
