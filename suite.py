# -*- coding: utf-8" -*
import unittest
from tests.tests_on_home_page import HomePageTest
from tests.tests_on_download_page import DownloadPageTest
from tests.tests_on_fullversion_page import FullVersionsPageTest

# Pobierz wszystkie testy:
HP_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
DP_tests = unittest.TestLoader().loadTestsFromTestCase(DownloadPageTest)
FV_tests = unittest.TestLoader().loadTestsFromTestCase(FullVersionsPageTest)

# Stwórz Test Suita łączac testy
test_suite = unittest.TestSuite([HP_tests, FV_tests, DP_tests])
# test_suite = unittest.TestSuite([DP_tests])

# odpal:
# unittest.TextTestRunner(verbosity=2).run(test_suite)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)
