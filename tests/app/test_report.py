import platform
import unittest

from PySide2 import QtWidgets

from hyo2.abc.app.report import Report
from hyo2.abc.lib.lib_info import LibInfo


class TestABCLibReport(unittest.TestCase):

    @unittest.skipIf(platform.system() in ['Linux', ], "It crashes on Linux")
    def test_init(self):

        if not QtWidgets.qApp:
            QtWidgets.QApplication([])

        li = LibInfo()
        _ = Report(lib_name=li.lib_name, lib_version=li.lib_version)


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibReport))
    return s
