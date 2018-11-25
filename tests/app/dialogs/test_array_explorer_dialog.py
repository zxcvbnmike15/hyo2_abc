import numpy as np
import unittest

from PySide2 import QtCore, QtWidgets

# import logging
# logging.basicConfig(level=logging.DEBUG)

from hyo2.abc.app.dialogs.array_explorer.array_explorer import ArrayExplorer


class TestAppArrayExplorerDialog(unittest.TestCase):

    def test_visibility(self):

        if not QtWidgets.qApp:
            QtWidgets.QApplication([])

        mw = QtWidgets.QMainWindow()
        mw.show()

        arr = np.zeros((20, 30, 40), dtype=np.float32)
        d = ArrayExplorer(array=arr, parent=mw)
        QtCore.QTimer.singleShot(1, d.accept)
        ret = d.exec_()
        self.assertGreaterEqual(ret, 0)


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppArrayExplorerDialog))
    return s
