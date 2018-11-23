import time
import sys
import logging

from PySide2.QtWidgets import (
    QApplication
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from hyo2.abc.app.browser.browser import Browser

app = QApplication([])

w = Browser()
w.show()

# w.change_url("https://www.google.com")
# logger.debug("current url: %s" % w.url())

sys.exit(app.exec_())
