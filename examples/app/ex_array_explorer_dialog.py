import numpy as np
import sys
import logging

from PySide2 import QtWidgets

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.app.dialogs.array_explorer.array_explorer import ArrayExplorer

# arr = np.zeros((40, ), dtype=np.float32)
# arr = np.zeros((30, 40), dtype=np.float32)
# arr = np.zeros((20, 30, 40), dtype=np.float32)
arr = np.random.rand(20, 30, 40)

app = QtWidgets.QApplication([])

mw = QtWidgets.QMainWindow()
mw.show()

d = ArrayExplorer(array=arr, parent=mw)
ret = d.exec_()
logger.debug("returned: %s" % ret)
logger.debug("array shape: %s" % (d.array.shape, ))

sys.exit(app.exec_())
