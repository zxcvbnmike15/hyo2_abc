import os
import unittest

from PySide2 import QtWidgets

# import logging
# logging.basicConfig(level=logging.DEBUG)

from hyo2.abc.app.dialogs.noaa_s57.noaa_s57 import NOAAS57Dialog
from hyo2.abc.app.dialogs.noaa_s57.noaa_support import NOAASupport
from hyo2.abc.lib.lib_info import LibInfo
from hyo2.abc.app.app_info import AppInfo


class TestAppNOAAS57Dialog(unittest.TestCase):

    def test_visibility(self):

        if not QtWidgets.qApp:
            QtWidgets.QApplication([])

        d = NOAAS57Dialog(lib_info=LibInfo(), app_info=AppInfo())
        d.show()

    def test_init(self):

        noaa_support = NOAASupport(lib_info=LibInfo(), app_info=AppInfo())

        self.assertTrue("_" in noaa_support.underscored_version())
        self.assertTrue(os.path.exists(noaa_support.internal_zip_path()))
        self.assertTrue(noaa_support.internal_zip_path_exists())


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppNOAAS57Dialog))
    return s
