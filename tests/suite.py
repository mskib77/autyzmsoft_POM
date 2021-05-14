# -*- coding: utf-8" -*

import unittest
from tests_on_fullversion_page import FullVersionsPageTest
from tests_on_download_page import DownloadPageTest

# Pobierz wszystkie testy z FullVersionsPageTest i DownloadPageTest
FullVersionsPageTest_text = unittest.TestLoader().loadTestsFromTestCase(FullVersionsPageTest)
DownloadPageTest_page_text = unittest.TestLoader().loadTestsFromTestCase(DownloadPageTest)

# Stwórz Test Suita łączac testy
test_suite = unittest.TestSuite([FullVersionsPageTest_text, DownloadPageTest_page_text])

# odpal
unittest.TextTestRunner(verbosity=2).run(test_suite)
