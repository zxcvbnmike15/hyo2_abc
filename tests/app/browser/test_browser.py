import unittest
import os

from PySide2.QtCore import (Qt, QPoint)
from PySide2.QtWidgets import (
    QApplication, qApp
)
from PySide2.QtTest import QTest

# import logging
# logging.basicConfig(level=logging.DEBUG)

from hyo2.abc.app.browser.browser import Browser
from hyo2.abc.lib.helper import Helper


class TestAppBrowserBrowser(unittest.TestCase):

    def test_change_url(self):

        if not qApp:
            QApplication([])

        w = Browser()
        initial_url = w.url()
        self.assertGreater(len(initial_url), 0)

        new_url = "https://www.google.com/"
        w.change_url(new_url)
        self.assertEqual(new_url, w.url())

    def test_type_url(self):

        if not qApp:
            QApplication([])

        w = Browser()
        initial_url = w.url()
        new_url = "https://www.google.com/"
        QTest.keyClick(w.address_line_edit, Qt.Key_Enter)

        # remove current characters
        for _ in initial_url:
            QTest.keyClick(w.address_line_edit, Qt.Key_Backspace)
        QTest.keyClicks(w.address_line_edit, new_url, 0, 1)
        QTest.keyClick(w.address_line_edit, Qt.Key_Enter)
        self.assertEqual(new_url, w.url())


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppBrowserBrowser))
    return s
