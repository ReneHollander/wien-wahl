"""
Autor: Rene Hollander, Paul Kalauner 5BHIT
"""
from PySide.QtCore import QAbstractTableModel, Qt

from PySide import QtCore
from data.wienwahlcsv import WienWahlReader, WienWahlWriter


class ContentTableModel(QAbstractTableModel):
    def __init__(self, parent, list, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.list = list
        self.header = []
        self.generate_headers()

    def generate_headers(self):
        if len(self.list) > 0:
            for key in self.list[0]:
                self.header.append(key)

    def rowCount(self, parent):
        return len(self.list)

    def columnCount(self, parent):
        return len(self.header)

    def data(self, index, role):
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

    def open(self, path):
        with open(path) as file:
            reader = WienWahlReader(file)
            self.list.clear()
            reader.collect(self.list)
        self.generate_headers()
        self.reset()

    def save(self, path):
        with open(path, "w") as file:
            writer = WienWahlWriter(file)
            writer.writeAll(self.list)
