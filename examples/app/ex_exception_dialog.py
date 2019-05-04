import sys
import logging

from PySide2 import QtWidgets

from hyo2.abc.app.dialogs.exception.exception_dialog import ExceptionDialog
from hyo2.abc.lib.lib_info import LibInfo
from hyo2.abc.app.app_info import AppInfo
from hyo2.abc.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc"])

app = QtWidgets.QApplication([])

d = ExceptionDialog(lib_info=LibInfo(), app_info=AppInfo())
d.show()

sys.exit(app.exec_())
