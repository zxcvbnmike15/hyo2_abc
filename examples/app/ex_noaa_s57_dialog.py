import sys
import logging

from PySide2 import QtWidgets

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.app.dialogs.noaa_s57.noaa_s57 import NOAAS57Dialog
from hyo2.abc.lib.lib_info import LibInfo
from hyo2.abc.app.app_info import AppInfo

app = QtWidgets.QApplication([])

d = NOAAS57Dialog(lib_info=LibInfo(), app_info=AppInfo())
d.show()

sys.exit(app.exec_())
