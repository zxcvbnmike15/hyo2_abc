import logging
import sys
from PySide2 import QtWidgets, QtGui

from hyo2.abc.lib.lib_info import LibInfo
from hyo2.abc.app.app_style import AppStyle
from hyo2.abc.app.app_info import AppInfo
from hyo2.abc.app.tabs.info.info_tab import InfoTab

def set_logging(default_logging=logging.WARNING, hyo2_logging=logging.INFO, abc_logging=logging.DEBUG):
    logging.basicConfig(
        level=default_logging,
        format="%(levelname)-9s %(name)s.%(funcName)s:%(lineno)d > %(message)s"
    )
    logging.getLogger("hyo2").setLevel(hyo2_logging)
    logging.getLogger("hyo2.abc").setLevel(abc_logging)


set_logging()
app_info = AppInfo()

app = QtWidgets.QApplication([])
app.setApplicationName('%s' % app_info.app_name)
app.setOrganizationName("HydrOffice")
app.setOrganizationDomain("hydroffice.org")
app.setStyleSheet(AppStyle.load_stylesheet())

mw = QtWidgets.QMainWindow()
mw.setObjectName(app_info.app_main_window_object_name)
mw.setWindowTitle('%s v.%s' % (app_info.app_name, app_info.app_version))
mw.setWindowIcon(QtGui.QIcon(app_info.app_icon_path))

tabs = QtWidgets.QTabWidget()
mw.setCentralWidget(tabs)

t = InfoTab(app_info=app_info, lib_info=LibInfo(),
            with_online_manual=True,
            with_offline_manual=True,
            with_bug_report=True,
            with_hydroffice_link=True,
            with_ccom_link=True,
            with_noaa_link=True,
            with_unh_link=True,
            with_license=True,
            with_noaa_57=True,
            main_win=mw)

tabs.insertTab(0, t, "Info")
mw.show()

sys.exit(app.exec_())
