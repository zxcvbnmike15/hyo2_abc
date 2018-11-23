import time
import sys
import logging

from PySide2.QtWidgets import (
    QApplication
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.app.about.about_dialog import AboutDialog
from hyo2.abc.lib.lib_info import LibInfo
from hyo2.abc.app.app_info import AppInfo

app = QApplication([])

d = AboutDialog(lib_info=LibInfo(), app_info=AppInfo(),
                with_locale_tab=True, with_gdal_tab=True)
d.show()

sys.exit(app.exec_())
