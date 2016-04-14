"""
Autor: Rene Hollander, Paul Kalauner 5BHIT
"""
from PySide.QtCore import QAbstractTableModel, Qt, SIGNAL, QModelIndex

from PySide import QtCore
from data.wienwahlcsv import WienWahlReader, WienWahlWriter
from natsort import natsorted
from operator import itemgetter


class ContentTableModel(QAbstractTableModel):
    def __init__(self, parent, list, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.list = list
        self.header = []
        self.generate_headers()

    def generate_headers(self):
        if len(self.list) > 0:
            self.header = []
            for key in self.list[0]:
                self.header.append(key)

    def rowCount(self, parent):
        return len(self.list)

    def columnCount(self, parent):
        return len(self.header)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.list[index.row()][self.header[index.column()]]

    def setData(self, *args):
        self.list[args[0].row()][self.header[args[0].column()]] = args[1]
        return True

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def open(self, path, clear=True):
        with open(path) as file:
            reader = WienWahlReader(file)
            if clear:
                self.list.clear()
            reader.collect(self.list)
        self.generate_headers()
        self.reset()

    def save(self, path):
        with open(path, "w") as file:
            writer = WienWahlWriter(file)
            writer.writeAll(self.list)

    def duplicateRow(self, row_index, parent=QModelIndex()):
        self.beginInsertRows(parent, row_index, 1)
        row = self.list[row_index].copy()
        self.list.insert(row_index + 1, {key: "" for key in self.header})
        self.list[row_index + 1] = row
        self.endInsertRows()

    def insertRows(self, row, count, parent=QModelIndex()):
        self.beginInsertRows(parent, row, row + count - 1)
        for i in range(count):
            self.list.insert(row, {key: "" for key in self.header})
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row + count - 1)
        del self.list[row:row + count]
        self.endRemoveRows()
        return True

    def sort(self, ncol, order):
        if len(self.list) == 0:
            return
        self.emit(SIGNAL("layoutToBeChanged()"))
        self.list = natsorted(self.list, key=itemgetter(self.header[ncol]), reverse=(order == Qt.DescendingOrder))
        self.emit(SIGNAL("layoutChanged()"))

    def set_list(self, datalist, header=None):
        self.emit(SIGNAL("layoutToBeChanged()"))
        self.list = datalist
        if header is None:
            self.generate_headers()
        else:
            self.header = header
        self.emit(SIGNAL("layoutChanged()"))
