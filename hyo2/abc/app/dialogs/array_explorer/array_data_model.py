from typing import Optional, Union, ByteString
from PySide2 import QtCore, QtGui, QtWidgets
import numpy as np
QVariant = lambda value=None: value

from collections import OrderedDict

ArrayType = Union[np.ndarray, ByteString]


class ArrayDataModel(QtCore.QAbstractTableModel):

    def __init__(self, array: ArrayType, parent: QtWidgets.QWidget):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.array = array
        self.editable = False
        self.depth = 0

        if (self.array.ndim == 0) or (self.array.ndim > 3):
            raise RuntimeError("Unsupported array shape: %d" % self.array.ndim)

    def setEditable(self, value: bool) -> None:
        self.editable = value

    def flags(self, index):
        flags = super(ArrayDataModel, self).flags(index)
        if self.editable:
            flags |= QtCore.Qt.ItemIsEditable
        return flags

    def rowCount(self, parent=None) -> int:
        return self.array.shape[0]

    def columnCount(self, parent=None) -> int:
        if self.array.ndim == 1:
            return 1
        return self.array.shape[1]

    def signalUpdate(self):
        """This is full update, not efficient"""
        # noinspection PyUnresolvedReferences
        self.layoutChanged.emit()

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QVariant()
        if orientation == QtCore.Qt.Horizontal:
            try:
                return '%05d' % section
            except IndexError:
                return QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                return '%05d' % section
            except IndexError:
                return QVariant()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QVariant()
        if not index.isValid():
            return QVariant()

        # if index.column() == self.data_dict['Pressure']:
        #     return QVariant(str(self.prj.cur.proc.pressure[index.row()]))
        # elif index.column() == self.data_dict['Depth']:
        #     return QVariant(str(self.prj.cur.proc.depth[index.row()]))
        # elif index.column() == self.data_dict['Speed']:
        #     return QVariant(str(self.prj.cur.proc.speed[index.row()]))
        # elif index.column() == self.data_dict['Temp']:
        #     return QVariant(str(self.prj.cur.proc.temp[index.row()]))
        # elif index.column() == self.data_dict['Cond']:
        #     return QVariant(str(self.prj.cur.proc.conductivity[index.row()]))
        # elif index.column() == self.data_dict['Sal']:
        #     return QVariant(str(self.prj.cur.proc.sal[index.row()]))
        # elif index.column() == self.data_dict['Source']:
        #     return QVariant("%.0f [%s]" % (self.prj.cur.proc.source[index.row()],
        #                                   Dicts.first_match(Dicts.sources, self.prj.cur.proc.source[index.row()])))
        # elif index.column() == self.data_dict['Flag']:
        #     return QVariant("%.0f [%s]" % (self.prj.cur.proc.flag[index.row()],
        #                                   Dicts.first_match(Dicts.flags, self.prj.cur.proc.flag[index.row()])))
        # else:

        if self.array.ndim == 1:
            return QVariant("%s" % self.array[index.row()])

        elif self.array.ndim == 2:
            return QVariant("%s" % self.array[index.row(), index.column()])

        return QVariant("%s" % self.array[index.row(), index.column(), self.depth])

    def setData(self, index, value, role):
        if not index.isValid():
            return False

        r = index.row()
        c = index.column()
        # test user input value
        try:
            user_value = float(value)
        except ValueError:
            msg = "invalid input: %s" % value
            QtWidgets.QMessageBox.critical(self.parent(), "Spreadsheet", msg, QtWidgets.QMessageBox.Ok)
            return False

        # # switch among columns
        # if c == self.data_dict['Pressure']:
        #     if (user_value > 20000) or (user_value < 0):
        #         ret = QtGui.QMessageBox.warning(self.table, "Spreadsheet",
        #                                         "Do you really want to set the pressure to %s?" % user_value,
        #                                         QtGui.QMessageBox.Ok|QtGui.QMessageBox.No)
        #         if ret == QtGui.QMessageBox.No:
        #             return False
        #     self.prj.cur.proc.pressure[r] = user_value
        #
        # elif c == self.data_dict['Depth']:
        #     # check to maintain depth monotonically descendant
        #     if r == 0:  # first sample
        #         if self.prj.cur.proc.depth[1] < user_value:
        #             QtGui.QMessageBox.critical(self.table, "Spreadsheet",
        #                                        "Invalid input: %s" % user_value,
        #                                        QtGui.QMessageBox.Ok)
        #             return False
        #     elif r == (self.prj.cur.proc.num_samples - 1):  # last sample
        #         if self.prj.cur.proc.depth[-2] > user_value:
        #             QtGui.QMessageBox.critical(self.table, "Spreadsheet",
        #                                        "Invalid input: %s" % user_value,
        #                                        QtGui.QMessageBox.Ok)
        #             return False
        #     else:
        #         if (self.prj.cur.proc.depth[r - 1] > user_value) or (self.prj.cur.proc.depth[r + 1] < user_value):
        #             QtGui.QMessageBox.critical(self.table, "Spreadsheet",
        #                                        "Invalid input: %s" % user_value,
        #                                        QtGui.QMessageBox.Ok)
        #             return False
        #     self.prj.cur.proc.depth[r] = user_value
        #
        # elif c == self.data_dict['Speed']:
        #     if (user_value > 2000) or (user_value < 1000):
        #         ret = QtGui.QMessageBox.warning(self.table, "Spreadsheet",
        #                                         "Do you really want to set the speed to %s?" % user_value,
        #                                         QtGui.QMessageBox.Ok|QtGui.QMessageBox.No)
        #         if ret == QtGui.QMessageBox.No:
        #             return False
        #     self.prj.cur.proc.speed[r] = user_value
        #
        # elif c == self.data_dict['Temp']:
        #     if (user_value < 0) or (user_value > 100):
        #         ret = QtGui.QMessageBox.warning(self.table, "Spreadsheet",
        #                                         "Do you really want to set the temperature to %s?" % user_value,
        #                                         QtGui.QMessageBox.Ok|QtGui.QMessageBox.No)
        #         if ret == QtGui.QMessageBox.No:
        #             return False
        #     self.prj.cur.proc.temp[r] = user_value
        #
        # elif c == self.data_dict['Cond']:
        #     if (user_value < 0) or (user_value > 10000):
        #         ret = QtGui.QMessageBox.warning(self.table, "Spreadsheet",
        #                                         "Do you really want to set the conductivity to %s?" % user_value,
        #                                         QtGui.QMessageBox.Ok|QtGui.QMessageBox.No)
        #         if ret == QtGui.QMessageBox.No:
        #             return False
        #     self.prj.cur.proc.conductivity[r] = user_value
        #
        # elif c == self.data_dict['Sal']:
        #     if (user_value < 0) or (user_value > 100):
        #         ret = QtGui.QMessageBox.warning(self.table, "Spreadsheet",
        #                                         "Do you really want to set the salinity to %s?" % user_value,
        #                                         QtGui.QMessageBox.Ok|QtGui.QMessageBox.No)
        #         if ret == QtGui.QMessageBox.No:
        #             return False
        #     self.prj.cur.proc.sal[r] = user_value
        #
        # elif c == self.data_dict['Source']:
        #     if (user_value < 0) or (user_value >= len(Dicts.sources)):
        #         ret = QtGui.QMessageBox.warning(self.table, "Spreadsheet",
        #                                         "Do you really want to set the data source to %s?" % user_value,
        #                                         QtGui.QMessageBox.Ok|QtGui.QMessageBox.No)
        #         if ret == QtGui.QMessageBox.No:
        #             return False
        #     self.prj.cur.proc.source[r] = user_value
        #
        # elif c == self.data_dict['Flag']:
        #     if (user_value < 0) or (user_value >= len(Dicts.flags)):
        #         ret = QtGui.QMessageBox.warning(self.table, "Spreadsheet",
        #                                         "Do you really want to set the data flag to %s?" % user_value,
        #                                         QtGui.QMessageBox.Ok|QtGui.QMessageBox.No)
        #         if ret == QtGui.QMessageBox.No:
        #             return False
        #     self.prj.cur.proc.flag[r] = user_value
        #
        # else:
        #     return False
        return True
