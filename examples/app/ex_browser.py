import sys
import logging

from PySide2 import QtWidgets

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.app.widgets.browser.browser import Browser

app = QtWidgets.QApplication([])

w = Browser()
w.show()

# w.change_url("https://www.google.com")
# logger.debug("current url: %s" % w.url())

sys.exit(app.exec_())
