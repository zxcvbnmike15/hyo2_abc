from typing import Optional
import logging

from PySide2.QtCore import (QUrl, Qt)
from PySide2.QtGui import (QIcon, QKeySequence)
from PySide2.QtWidgets import (
    QAction,QLineEdit, QMainWindow, QToolBar, QWidget
)
from PySide2.QtWebEngineWidgets import (QWebEnginePage, QWebEngineView, QWebEngineDownloadItem)

logger = logging.getLogger(__name__)

from hyo2.abc.app.browser.download_widget import DownloadWidget


class Browser(QMainWindow):

    def __init__(self, parent: Optional[QWidget]=None, url: str="https://www.hydroffice.org") -> None:
        super().__init__(parent)

        self.setWindowTitle('Browser')

        self._actions = {}
        self._create_menu()

        self._tool_bar = QToolBar()
        self.addToolBar(self._tool_bar)
        for action in self._actions.values():
            if not action.icon().isNull():

                self._tool_bar.addAction(action)

        self.address_line_edit = QLineEdit()
        self.address_line_edit.setClearButtonEnabled(True)
        # noinspection PyUnresolvedReferences
        self.address_line_edit.returnPressed.connect(self._load)
        self._tool_bar.addWidget(self.address_line_edit)

        self.view = QWebEngineView()
        page = self.view.page()
        page.titleChanged.connect(self.setWindowTitle)
        page.urlChanged.connect(self._url_changed)
        page.profile().downloadRequested.connect(self._download_requested)
        self.view.setPage(page)
        self.setCentralWidget(self.view)

        # self.addressLineEdit.setText(url)
        # self.view.load(QUrl(url))
        self.change_url(url=url)

    def _create_menu(self) -> None:
        style_icons = ':/qt-project.org/styles/commonstyle/images/'

        # noinspection PyCallByClass,PyTypeChecker
        back_action = QAction(QIcon.fromTheme("go-previous", QIcon(style_icons + 'left-32.png')), "Back", self,
                              shortcut=QKeySequence(QKeySequence.Back),
                              triggered=self.back)

        self._actions[QWebEnginePage.Back] = back_action

        # noinspection PyCallByClass,PyTypeChecker
        forward_action = QAction(QIcon.fromTheme("go-next", QIcon(style_icons + 'right-32.png')), "Forward", self,
                                 shortcut=QKeySequence(QKeySequence.Forward),
                                 triggered=self.forward)
        self._actions[QWebEnginePage.Forward] = forward_action

        reload_action = QAction(QIcon(style_icons + 'refresh-32.png'), "Reload", self,
                                shortcut=QKeySequence(QKeySequence.Refresh),
                                triggered=self.reload)
        self._actions[QWebEnginePage.Reload] = reload_action

    def change_url(self, url: str) -> None:
        self.address_line_edit.setText(url)
        self._load()

    def url(self) -> str:
        return self.address_line_edit.text()

    def _load(self) -> None:
        url = QUrl.fromUserInput(self.address_line_edit.text().strip())
        if url.isValid():
            self.view.load(url)

    def back(self) -> None:
        self.view.page().triggerAction(QWebEnginePage.Back)

    def forward(self) -> None:
        self.view.page().triggerAction(QWebEnginePage.Forward)

    def reload(self) -> None:
        self.view.page().triggerAction(QWebEnginePage.Reload)

    def _url_changed(self, url: QUrl) -> None:
        self.address_line_edit.setText(url.toString())

    def _download_requested(self, item: QWebEngineDownloadItem) -> None:

        # Remove old downloads before opening a new one
        for old_download in self.statusBar().children():
            if type(old_download).__name__ == 'download_widget' and \
                    old_download.state() != QWebEngineDownloadItem.DownloadInProgress:
                self.statusBar().removeWidget(old_download)
                del old_download

        item.accept()
        download_widget = DownloadWidget(item)
        download_widget.remove_requested.connect(self._remove_download_requested,
                                                 Qt.QueuedConnection)

        self.statusBar().addWidget(download_widget)

    def _remove_download_requested(self):
        download_widget = self.sender()
        self.statusBar().removeWidget(download_widget)
        del download_widget
