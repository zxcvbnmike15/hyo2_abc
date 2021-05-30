import logging

from PySide2.QtCore import QEventLoop, QTimer, QUrl
from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView

logger = logging.getLogger(__name__)


class WebRenderer(QWebEngineView):

    def __init__(self, make_app: bool = False):
        if make_app:
            self._app = QApplication([])
        QWebEngineView.__init__(self)

    def open(self, url: str, timeout: int = 10):
        """Wait for download to complete and return result"""
        loop = QEventLoop()
        timer = QTimer()
        timer.setSingleShot(True)
        # noinspection PyUnresolvedReferences
        timer.timeout.connect(loop.quit)
        # noinspection PyUnresolvedReferences
        self.loadFinished.connect(loop.quit)
        self.load(QUrl(url))
        # noinspection PyArgumentList
        timer.start(timeout * 1000)
        loop.exec_()  # delay here until download finished
        if timer.isActive():
            # downloaded successfully
            timer.stop()
        else:
            logger.info('Request timed out: %s' % url)
