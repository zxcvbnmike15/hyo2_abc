import sys
import logging

from PySide2 import QtWidgets, QtWebEngineWidgets
from hyo2.abc.app.widgets.browser.download_widget import DownloadWidget
from hyo2.abc.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc"])


def download_requested(item):
    item.accept()
    w = DownloadWidget(download_item=item)
    mw.statusBar().addWidget(w)


app = QtWidgets.QApplication([])

mw = QtWidgets.QMainWindow()
view = QtWebEngineWidgets.QWebEngineView()
view.page().profile().downloadRequested.connect(download_requested)
mw.setCentralWidget(view)
mw.show()

view.page().download("https://www.hydroffice.org/static/mycommon/img/logo.png")

sys.exit(app.exec_())
