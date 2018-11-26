import numpy as np
import sys
import logging

from PySide2 import QtWidgets

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.app.app_style import AppStyle
from hyo2.abc.app.dialogs.array_explorer.array_explorer import ArrayExplorer

# arr = np.zeros((40, ), dtype=np.float32)
# arr = np.zeros((30, 40), dtype=np.float32)
#arr = np.zeros((100, 120, 40), dtype=np.float32)
arr = np.random.rand(1000, 1200, 20)

app = QtWidgets.QApplication([])
app.setStyleSheet(AppStyle.load_stylesheet())

mw = QtWidgets.QMainWindow()
mw.show()

with_menu = False
with_info_button = False
with_help_button = False

d = ArrayExplorer(array=arr, parent=mw,
                  with_menu=with_menu, with_info_button=with_info_button,
                  with_help_button=with_help_button)
ret = d.exec_()
logger.debug("returned: %s" % ret)
logger.debug("array shape: %s" % (d.array.shape, ))

sys.exit(app.exec_())
