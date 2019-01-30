import sys
import logging

from PySide2 import QtWidgets

from hyo2.abc.app.report import Report
from hyo2.abc.lib.lib_info import LibInfo

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = QtWidgets.QApplication([])

li = LibInfo()
r = Report(lib_name=li.lib_name, lib_version=li.lib_version)

# sys.exit(app.exec_())
