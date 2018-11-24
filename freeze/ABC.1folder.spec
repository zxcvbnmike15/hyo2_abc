# Builds a single-folder EXE for distribution.
# Note that an "unbundled" distribution launches much more quickly, but
# requires an installer program to distribute.
#
# To compile, execute the following within the source directory:
#
# python /path/to/pyinstaller.py --clean -y ABC.1folder.spec
#
# The resulting .exe file is placed in the dist/FigLeaf folder.
#
# - It may require to manually copy DLL libraries.
# - Uninstall PyQt and sip
# - For QtWebEngine:
#   . copy QtWebEngineProcess.exe in the root
#   . copy in PySide2 both "resources" and "translations" folder
#

from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT, BUNDLE, TOC
from PyInstaller.compat import is_darwin

import os
import sys
sys.modules['FixTk'] = None

from hyo2.abc import __version__ as abc_version


def collect_pkg_data(package, include_py_files=False, subdir=None):
    import os
    from PyInstaller.utils.hooks import get_package_paths, remove_prefix, PY_IGNORE_EXTENSIONS

    # Accept only strings as packages.
    if type(package) is not str:
        raise ValueError

    pkg_base, pkg_dir = get_package_paths(package)
    if subdir:
        pkg_dir = os.path.join(pkg_dir, subdir)
    # Walk through all file in the given package, looking for data files.
    data_toc = TOC()
    for dir_path, dir_names, files in os.walk(pkg_dir):
        for f in files:
            extension = os.path.splitext(f)[1]
            if include_py_files or (extension not in PY_IGNORE_EXTENSIONS):
                source_file = os.path.join(dir_path, f)
                dest_folder = remove_prefix(dir_path, os.path.dirname(pkg_base) + os.sep)
                dest_file = os.path.join(dest_folder, f)
                data_toc.append((dest_file, source_file, 'DATA'))

    return data_toc


abc_data = collect_pkg_data('hyo2.abc')
pyside2_data = collect_pkg_data('PySide2')

icon_file = os.path.join('freeze', 'ABC.ico')
if is_darwin:
    icon_file = os.path.join('freeze', 'ABC.icns')

a = Analysis(['ABC.py'],
             pathex=[],
             hiddenimports=["PIL", "scipy._lib.messagestream"],
             excludes=["IPython", "PyQt4", "pandas", "sphinx", "sphinx_rtd_theme", "OpenGL_accelerate",
                       "FixTk", "tcl", "tk", "_tkinter", "tkinter", "Tkinter",
                       "wx"],
             hookspath=None,
             runtime_hooks=None)

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='ABC.%s' % abc_version,
          debug=False,
          strip=None,
          upx=True,
          console=True,
          icon=icon_file)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               abc_data,
               pyside2_data,
               strip=None,
               upx=True,
               name='ABC.%s' % abc_version)
