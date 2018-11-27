import sys
import logging

from PySide2 import QtWidgets

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.app.report import Report
from hyo2.abc.lib.lib_info import LibInfo
from hyo2.abc.app.app_info import AppInfo

app = QtWidgets.QApplication([])

r = Report()

sys.exit(app.exec_())
