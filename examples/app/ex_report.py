import sys
import logging

from PySide2 import QtWidgets

from hyo2.abc.app.report import Report
from hyo2.abc.lib.lib_info import LibInfo
from hyo2.abc.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc"])

app = QtWidgets.QApplication([])

li = LibInfo()
r = Report(lib_name=li.lib_name, lib_version=li.lib_version)

# sys.exit(app.exec_())
