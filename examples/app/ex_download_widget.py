import sys
import logging

from PySide2 import QtCore, QtWidgets, QtWebEngineWidgets

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.app.widgets.browser.download_widget import DownloadWidget


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
