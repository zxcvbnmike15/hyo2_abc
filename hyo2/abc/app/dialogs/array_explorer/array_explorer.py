from typing import Optional, Union, ByteString
import numpy as np
import os
import logging

from PySide2 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

logger = logging.getLogger(__name__)

from hyo2.abc.lib.lib_info import LibInfo
from hyo2.abc.lib.helper import Helper

ArrayType = Union[np.ndarray, ByteString]


class ArrayExplorer(QtWidgets.QDialog):

    media = os.path.join(os.path.dirname(__file__), "media")

    def __init__(self, array: ArrayType, parent: Optional[QtWidgets.QWidget]=None) -> None:
        super().__init__(parent)

        self.setWindowTitle('ArrayExplorer')
        self.resize(600, 400)
        self._arr = array

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setMenuBar(QtWidgets.QMenuBar())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.file_menu = self.layout().menuBar().addMenu("File")
        self.view_menu = self.layout().menuBar().addMenu("View")
        self.edit_menu = self.layout().menuBar().addMenu("Edit")
        self.help_menu = self.layout().menuBar().addMenu("Help")

        self.top_layout = QtWidgets.QHBoxLayout()
        self.layout().addLayout(self.top_layout)
        self.main_tb = QtWidgets.QToolBar("Main")
        self.main_tb.setIconSize(QtCore.QSize(32, 32))
        self.main_tb.setAutoFillBackground(True)
        self.top_layout.addWidget(self.main_tb)
        self.info_action = self.main_tb.addAction(
            QtGui.QIcon(os.path.join(self.media, 'info.png')), "Info", self.do_info)
        self.file_menu.addAction(self.info_action)
        self.help_action = self.main_tb.addAction(
            QtGui.QIcon(os.path.join(self.media, 'help.png')), "Help", self.do_help)
        self.help_menu.addAction(self.help_action)

        self.main_wdg = QtWidgets.QSplitter(self)
        self.main_wdg.setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self.main_wdg)

        self.left_wdg = QtWidgets.QWidget(self)
        self.left_wdg.setMinimumWidth(80)
        self.left_wdg.setMaximumWidth(120)
        self.main_wdg.addWidget(self.left_wdg)
        self.main_wdg.setStretchFactor(0, 1)
        self.left_layout = QtWidgets.QVBoxLayout()
        self.left_wdg.setLayout(self.left_layout)
        self.left_layout.addStretch()
        self.left_label = QtWidgets.QLabel()
        self.left_label.setStyleSheet("font-size: small;")
        self.left_label.setAlignment(QtCore.Qt.AlignCenter)
        self.left_label.setText(self.array_info())
        self.left_layout.addWidget(self.left_label)
        self.left_layout.addStretch()

        self.right_wdg = QtWidgets.QWidget(self)
        self.right_wdg.setAutoFillBackground(True)
        right_palette = self.main_wdg.palette()
        right_palette.setColor(self.main_wdg.backgroundRole(), QtCore.Qt.white)
        self.right_wdg.setPalette(right_palette)
        self.main_wdg.addWidget(self.right_wdg)
        self.main_wdg.setStretchFactor(1, 5)

    @property
    def array(self) -> ArrayType:
        return self._arr

    def array_info(self) -> str:
        if isinstance(self._arr, np.ndarray):
            txt = "%s\n" % (self._arr.shape, )
            txt += "%s" % (self._arr.dtype, )
        else:
            txt = "N/A"
        return txt

    def do_help(self) -> None:
        logger.debug("help")

    def do_info(self) -> None:
        logger.debug("help")
