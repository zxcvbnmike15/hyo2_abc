import os
from typing import Optional

from PySide2 import QtCore, QtGui, QtWidgets

from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QAction, QDialog, QLabel, QVBoxLayout, QHBoxLayout

import logging

logger = logging.getLogger(__name__)

from hyo2.abc.lib.helper import Helper
from hyo2.figleaf.app import app_info
from hyo2.figleaf.app.tabs.abstract_tab import AbstractTab
from hyo2.abc.app.browser.browser import Browser
from hyo2.abc.app.about.about_dialog import AboutDialog


class InfoTab(QtWidgets.QMainWindow):

    def __init__(self, main_win: QtWidgets.QMainWindow,
                 # tab_name: str="App Info Tab", start_url: Optional[str]=None,
                 default_url: str="http://www.hydroffice.org"):
        super().__init__(main_win)
        # self.tab_idx = 10
        # self.defaul_url = default_url

    #     if start_url is None:
    #         start_url = "%s%s" % (app_info.app_url, app_info.app_version.replace(".", "_"))
    #     self.start_url = start_url
    #
    #     # add about dialog
    #     self.about_dlg = AboutDialog(self)
    #     self.about_dlg.hide()
    #
    #     icon_size = QSize(app_info.app_toolbars_icon_size, app_info.app_toolbars_icon_size)
    #
    #     self.toolbar = self.addToolBar('Shortcuts')
    #     self.toolbar.setIconSize(icon_size)
    #
    #     # home
    #     home_action = QAction(QIcon(os.path.join(app_info.app_media_path, 'home.png')), 'Home page', self)
    #     # noinspection PyUnresolvedReferences
    #     home_action.triggered.connect(self.load_default)
    #     self.toolbar.addAction(home_action)
    #
    #     # online manual
    #     open_online_manual = QAction(QIcon(os.path.join(app_info.app_media_path, 'online_manual.png')),
    #                                  'Online Manual', self)
    #     open_online_manual.setStatusTip('Open the online manual')
    #     # noinspection PyUnresolvedReferences
    #     open_online_manual.triggered.connect(self.open_online_manual)
    #     self.toolbar.addAction(open_online_manual)
    #     self.main_win.menu_help.addAction(open_online_manual)
    #
    #     # offline manual
    #     open_offline_manual = QAction(QIcon(os.path.join(app_info.app_media_path, 'offline_manual.png')),
    #                                   'Offline Manual', self)
    #     open_offline_manual.setStatusTip('Open the offline manual')
    #     # noinspection PyUnresolvedReferences
    #     open_offline_manual.triggered.connect(self.open_offline_manual)
    #     self.toolbar.addAction(open_offline_manual)
    #     self.main_win.menu_help.addAction(open_offline_manual)
    #
    #     # bug report
    #     fill_bug_report = QAction(QIcon(os.path.join(app_info.app_media_path, 'bug.png')), 'Bug Report', self)
    #     fill_bug_report.setStatusTip('Fill a bug report')
    #     # noinspection PyUnresolvedReferences
    #     fill_bug_report.triggered.connect(self.fill_bug_report)
    #     self.toolbar.addAction(fill_bug_report)
    #     self.main_win.menu_help.addAction(fill_bug_report)
    #
    #     self.toolbar.addSeparator()
    #     self.main_win.menu_help.addSeparator()
    #
    #     # HydrOffice.org
    #     hyo_action = QAction(QIcon(os.path.join(app_info.app_media_path, 'hyo.png')), 'HydrOffice.org', self)
    #     # noinspection PyUnresolvedReferences
    #     hyo_action.triggered.connect(self.load_hydroffice_org)
    #     self.toolbar.addAction(hyo_action)
    #
    #     # noaa
    #     noaa_action = QAction(QIcon(os.path.join(app_info.app_media_path, 'noaa.png')), 'nauticalcharts.noaa.gov', self)
    #     # noinspection PyUnresolvedReferences
    #     noaa_action.triggered.connect(self.load_noaa_ocs_gov)
    #     self.toolbar.addAction(noaa_action)
    #
    #     # ccom.unh.edu
    #     ccom_action = QAction(QIcon(os.path.join(app_info.app_media_path, 'ccom.png')), 'ccom.unh.edu', self)
    #     # noinspection PyUnresolvedReferences
    #     ccom_action.triggered.connect(self.load_ccom_unh_edu)
    #     self.toolbar.addAction(ccom_action)
    #
    #     # unh.edu
    #     unh_action = QAction(QIcon(os.path.join(app_info.app_media_path, 'unh.png')), 'unh.edu', self)
    #     # noinspection PyUnresolvedReferences
    #     unh_action.triggered.connect(self.load_unh_edu)
    #     self.toolbar.addAction(unh_action)
    #
    #     self.toolbar.addSeparator()
    #     self.main_win.menu_help.addSeparator()
    #
    #     # license
    #     license_action = QAction(QIcon(os.path.join(app_info.app_media_path, 'license.png')), 'License', self)
    #     license_action.setStatusTip('License info')
    #     # noinspection PyUnresolvedReferences
    #     license_action.triggered.connect(self.load_license)
    #     self.toolbar.addAction(license_action)
    #     self.main_win.menu_help.addAction(license_action)
    #
    #     # authors
    #     self.authors_dialog = None
    #     authors_action = QAction(QIcon(os.path.join(app_info.app_media_path, 'authors.png')), 'Contacts', self)
    #     authors_action.setStatusTip('Contact Authors')
    #     # noinspection PyUnresolvedReferences
    #     authors_action.triggered.connect(self.show_authors)
    #     self.toolbar.addAction(authors_action)
    #     self.main_win.menu_help.addAction(authors_action)
    #
    #     # about
    #     show_about_dialog = QAction(QIcon(os.path.join(app_info.app_media_path, 'app_icon.png')), 'About', self)
    #     show_about_dialog.setStatusTip('Info about %s' % app_info.app_name)
    #     # noinspection PyUnresolvedReferences
    #     show_about_dialog.triggered.connect(self.about_dlg.switch_visible)
    #     self.toolbar.addAction(show_about_dialog)
    #     self.main_win.menu_help.addAction(show_about_dialog)
    #
    #     # add browser
    #     self.browser = Browser(url=self.start_url)
    #     self.frame_layout.addWidget(self.browser)
    #
    # # ### ICON RESIZE ###
    #
    # def set_toolbars_icon_size(self, icon_size: int) -> None:
    #     self.toolbar.setIconSize(QSize(icon_size, icon_size))
    #
    # # ### ACTIONS ###
    #
    # def load_default(self):
    #     self.browser.change_url(self.defaul_url)
    #
    # def open_online_manual(self) -> None:
    #     logger.debug("open online manual")
    #     Helper.explore_folder(app_info.app_manual_url)
    #
    # @classmethod
    # def open_offline_manual(cls) -> None:
    #     logger.debug("open offline manual")
    #     pdf_path = os.path.join(app_info.app_media_path, "manual.pdf")
    #     if not os.path.exists(pdf_path):
    #         logger.warning("unable to find offline manual at %s" % pdf_path)
    #         return
    #
    #     Helper.explore_folder(pdf_path)
    #
    # def fill_bug_report(self) -> None:
    #     logger.debug("fill bug report")
    #     raise RuntimeError("USER")
    #
    # def load_license(self):
    #     self.main_win.switch_to_info_tab()
    #     url = 'https://www.hydroffice.org/license/'
    #     self.browser.change_url(url)
    #
    # def load_hydroffice_org(self):
    #     url = 'https://www.hydroffice.org'
    #     self.browser.change_url(url)
    #
    # def load_noaa_ocs_gov(self):
    #     url = 'http://www.nauticalcharts.noaa.gov/'
    #     self.browser.change_url(url)
    #
    # def load_ccom_unh_edu(self):
    #     url = 'http://ccom.unh.edu'
    #     self.browser.change_url(url)
    #
    # def load_unh_edu(self):
    #     url = 'http://www.unh.edu'
    #     self.browser.change_url(url)
    #
    # def show_authors(self):
    #     self.main_win.switch_to_info_tab()
    #
    #     if self.authors_dialog is None:
    #         # create an author dialog
    #         self.authors_dialog = QDialog(self)
    #         self.authors_dialog.setWindowTitle("Write us")
    #         self.authors_dialog.setMaximumSize(QSize(150, 120))
    #         self.authors_dialog.setMaximumSize(QSize(300, 240))
    #         vbox = QVBoxLayout()
    #         self.authors_dialog.setLayout(vbox)
    #
    #         hbox = QHBoxLayout()
    #         vbox.addLayout(hbox)
    #         hbox.addStretch()
    #         logo = QLabel()
    #         logo.setPixmap(QPixmap(app_info.app_icon_path))
    #         hbox.addWidget(logo)
    #         hbox.addStretch()
    #
    #         vbox.addSpacing(10)
    #
    #         text0 = QLabel(self.authors_dialog)
    #         text0.setOpenExternalLinks(True)
    #         vbox.addWidget(text0)
    #         text0.setText("""
    #         <b>For bugs and troubleshooting:</b><br>
    #         <a href=\"mailto:figleaf@hydroffice.org?Subject=FigLeaf\">figleaf@hydroffice.org</a>
    #         <br>
    #         <b>For comments and ideas for new features:</b><br>
    #         Giuseppe Masetti  <a href=\"mailto:gmasetti@ccom.unh.edu?Subject=Hydroffice%20SoundSpeed\">
    #         gmasetti@ccom.unh.edu</a><br>
    #         Glen Rice  <a href=\"mailto:glen.rice@noaa.gov?Subject=Hydroffice%20FigLeaf\">glen.rice@noaa.gov</a><br>
    #         """)
    #
    #     self.authors_dialog.show()
