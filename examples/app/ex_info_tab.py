import time
import sys
import logging

from PySide2 import QtWidgets

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.app.info.info_tab import InfoTab

app = QtWidgets.QApplication([])

mw = QtWidgets.QMainWindow()

t = InfoTab(main_win=mw)
t.show()

sys.exit(app.exec_())
