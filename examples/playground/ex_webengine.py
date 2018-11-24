import sys
from PySide2 import QtWidgets, QtWebEngineWidgets


def download_requested(item):
    print("url: %s" % item.url())


app = QtWidgets.QApplication([])

mw = QtWidgets.QMainWindow()
view = QtWebEngineWidgets.QWebEngineView()
view.page().profile().downloadRequested.connect(download_requested)
#view.setUrl("https://pypi.org/project/PySide2/#files")
view.setUrl("https://www.hydroffice.org/soundspeed")
mw.setCentralWidget(view)
mw.show()

sys.exit(app.exec_())