import importlib
import os
import platform
import subprocess
import sys
import logging

from appdirs import user_data_dir

logger = logging.getLogger(__name__)

from hyo2.abc.lib.lib_info import LibInfo


class Helper:
    """ A collection class with many helper functions, in alphabetic order """

    def __init__(self, lib_info: LibInfo):
        self._li = lib_info

    @classmethod
    def explore_folder(cls, path: str) -> bool:
        """Open the passed path using OS-native commands"""
        if cls.is_url(path):
            import webbrowser
            webbrowser.open(path)
            return True

        if not os.path.exists(path):
            logger.warning('invalid path to folder: %s' % path)
            return False

        path = os.path.normpath(path)

        if cls.is_darwin():
            subprocess.call(['open', '--', path])
            return True

        elif cls.is_linux():
            subprocess.call(['xdg-open', path])
            return True

        elif cls.is_windows():
            subprocess.call(['explorer', path])
            return True

        logger.warning("Unknown/unsupported OS")
        return False

    def explore_package_folder(self):
        self.explore_folder(self.package_folder())

    @classmethod
    def is_64bit_os(cls) -> bool:
        """ Check if the current OS is at 64 bits """
        return platform.machine().endswith('64')

    @classmethod
    def is_64bit_python(cls) -> bool:
        """ Check if the current Python is at 64 bits """
        return platform.architecture()[0] == "64bit"

    @classmethod
    def is_darwin(cls) -> bool:
        """ Check if the current OS is Mac OS """
        return sys.platform == 'darwin'

    @classmethod
    def is_linux(cls) -> bool:
        """ Check if the current OS is Linux """
        return sys.platform in ['linux', 'linux2']

    @classmethod
    def is_pydro(cls) -> bool:
        try:
            # noinspection PyUnresolvedReferences
            import HSTB as _
            return True

        except ImportError:
            return False

    @classmethod
    def is_url(cls, value) -> bool:
        if len(value) > 7:

            https = "https"
            if value[:len(https)] == https:
                return True

        return False

    @classmethod
    def is_windows(cls) -> bool:
        """ Check if the current OS is Windows """
        return (sys.platform == 'win32') or (os.name is "nt")

    @classmethod
    def python_path(cls):
        """ Return the python site-specific directory prefix (the temporary folder for PyInstaller) """

        # required by PyInstaller
        if hasattr(sys, '_MEIPASS'):
            if cls.is_windows():
                import win32api
                # noinspection PyProtectedMember
                return win32api.GetLongPathName(sys._MEIPASS)
            else:
                # noinspection PyProtectedMember
                return sys._MEIPASS

        # check if in a virtual environment
        if hasattr(sys, 'real_prefix'):

            if cls.is_windows():
                import win32api
                # noinspection PyProtectedMember
                return win32api.GetLongPathName(sys.real_prefix)
            else:
                return sys.real_prefix

        return sys.prefix

    def package_info(self, qt_html: bool=False) -> str:

        def style_row(raw_row: str, is_h1: bool=False, is_h2: bool=False) -> str:
            if qt_html:
                if is_h1:
                    return "<h1>%s</h1>" % raw_row
                elif is_h2:
                    return "<h2>%s</h2>" % raw_row
                else:
                    return "<p>%s</p>" % raw_row
            else:
                if is_h1:
                    return "%s:\n" % raw_row
                elif is_h2:
                    return "[%s]\n" % raw_row
                else:
                    return "  - %s\n" % raw_row

        def style_url(text: str, url: str) -> str:
            if qt_html:
                return "<a href=\"%s\">%s</a>" % (url, text,)
            else:
                return "%s(%s)" % (text, url)

        def style_mailto(text: str, url: str) -> str:
            if qt_html:
                return "<a href=\"mailto:%s?Subject=%s%%20v.%s\" target=\"_top\">%s</a>" \
                       % (url, self._li.lib_name, self._li.lib_version, text,)
            else:
                return "%s(%s)" % (text, url)

        def package_version(package: str) -> str:
            try:
                return importlib.import_module("%s" % package).__version__
            except ImportError:
                return "N/A"

        msg = str()

        msg += style_row("General Info", is_h2=True)
        msg += style_row("author: %s" % style_mailto(self._li.lib_author, self._li.lib_author_email))
        msg += style_row("support: %s" % style_mailto(self._li.lib_support_email, self._li.lib_support_email))
        msg += style_row("website: %s" % style_url(self._li.lib_url, self._li.lib_url))
        msg += style_row("license: %s" % style_url(self._li.lib_license, self._li.lib_license_url))

        msg += style_row("Hosting Environment", is_h2=True)
        msg += style_row("os: %s %s-bit" % (os.name, "64" if self.is_64bit_os() else "32"))
        msg += style_row("python: %s %s-bit" % (platform.python_version(), "64" if self.is_64bit_python() else "32"))
        msg += style_row("pydro: %s" % self.is_pydro())

        msg += style_row("Dependencies", is_h2=True)
        for key in self._li.lib_dep_dict.keys():
            msg += style_row("%s: %s" % (key, package_version(self._li.lib_dep_dict[key]), ))

        return msg

    def package_folder(self):
        _dir = user_data_dir(self._li.lib_name, "HydrOffice")
        if not os.path.exists(_dir):  # create it if it does not exist
            os.makedirs(_dir)

        return _dir
