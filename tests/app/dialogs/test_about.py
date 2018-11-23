import unittest

from PySide2.QtWidgets import (
    QApplication, qApp
)

from hyo2.abc.app.browser.browser import Browser


class TestAppBrowserBrowser(unittest.TestCase):

    def test_show(self):

        if not qApp:
            QApplication([])

        w = Browser()
        w.show()


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppBrowserBrowser))
    return s
