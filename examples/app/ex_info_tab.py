import time
import sys
import logging

from PySide2 import QtWidgets

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.app.info.info_tab import InfoTab
from hyo2.abc.lib.lib_info import LibInfo
from hyo2.abc.app.app_info import AppInfo

app = QtWidgets.QApplication([])

mw = QtWidgets.QMainWindow()

t = InfoTab(main_win=mw,
            lib_info=LibInfo(), app_info=AppInfo())
t.show()

sys.exit(app.exec_())
