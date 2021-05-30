import unittest

from PySide2 import QtWidgets

from hyo2.abc.app.web_renderer import WebRenderer


class TestWebRenderer(unittest.TestCase):

    def test_init(self):
        # noinspection PyArgumentList
        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])
        wr = WebRenderer(make_app=False)
        wr.open("https://www.hydroffice.org")


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestWebRenderer))
    return s
