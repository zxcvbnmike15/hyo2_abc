import sys
import logging

from PySide2 import QtWidgets

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.app.tabs.info.info_tab import InfoTab
from hyo2.abc.lib.lib_info import LibInfo
from hyo2.abc.app.app_info import AppInfo

app = QtWidgets.QApplication([])

mw = QtWidgets.QMainWindow()

t = InfoTab(main_win=mw,
            lib_info=LibInfo(), app_info=AppInfo(),
            with_online_manual=True,
            with_offline_manual=True,
            with_bug_report=True,
            with_hydroffice_link=True,
            with_ccom_link=True,
            with_noaa_link=True,
            with_unh_link=True,
            with_license=True
            )
t.show()

sys.exit(app.exec_())
