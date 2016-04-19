from PySide.QtGui import QUndoCommand


class EditCommand(QUndoCommand):
    def __init__(self, model, index):
        QUndoCommand.__init__(self)
        self.newValue = None
        self.model = model
        self.index = index
        self.oldValue = None

    def redo(self):
        self.oldValue = self.model.data(self.index)
        self.model.setData(self.index, self.newValue)

    def undo(self):
        self.newValue = self.model.data(self.index)
        self.model.setData(self.index, self.oldValue)

    def setText(self, *args, **kwargs):
        super().setText(*args, **kwargs)


class InsertRowCommand(QUndoCommand):
    def __init__(self, model, row):
        QUndoCommand.__init__(self)
        self.model = model
        self.row = row

    def redo(self):
        self.model.insertRow(self.row)

    def undo(self):
        self.model.removeRow(self.row)


class RemoveRowCommand(QUndoCommand):
    def __init__(self, model, row):
        QUndoCommand.__init__(self)
        self.model = model
        self.row = row
        self.oldList = None
        self.oldHeader = None

    def redo(self):
        self.oldHeader = list(self.model.header)
        self.oldList = list(self.model.list)
        self.model.removeRow(self.row)

    def undo(self):
        self.model.set_list(self.oldList, self.oldHeader)


class DuplicateRowCommand(QUndoCommand):
    def __init__(self, model, index):
        QUndoCommand.__init__(self)
        self.model = model
        self.index = index

    def redo(self):
        self.model.duplicateRow(self.index[1])

    def undo(self):
        self.model.removeRow(self.index[1])
