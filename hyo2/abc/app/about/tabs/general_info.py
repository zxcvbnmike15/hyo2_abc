from PySide2 import QtWidgets

import logging

logger = logging.getLogger(__name__)

from hyo2.abc.lib.lib_info import LibInfo
from hyo2.abc.app.app_style import AppStyle
from hyo2.abc.lib.helper import Helper


class GeneralInfoTab(QtWidgets.QWidget):

    def __init__(self, lib_info: LibInfo, parent: QtWidgets.QWidget=None):
        super().__init__(parent)
        self._li = lib_info

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.text = QtWidgets.QTextBrowser()
        self.text.setReadOnly(True)
        self.text.setMinimumWidth(200)
        self.text.setOpenLinks(True)
        self.text.setOpenExternalLinks(True)
        self.text.document().setDefaultStyleSheet(AppStyle.html_css())
        self.text.setHtml(Helper(lib_info=lib_info).package_info(qt_html=True))
        self.layout.addWidget(self.text)