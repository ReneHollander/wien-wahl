"""
Autor: Rene Hollander, Paul Kalauner 5BHIT
"""
from PySide.QtCore import QAbstractTableModel, Qt


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

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None