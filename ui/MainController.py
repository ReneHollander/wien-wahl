"""
Autor: Rene Hollander 5BHIT
"""

from PySide.QtGui import *

from ui import MainView


class MainController(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.last_value = 0

        self.form = MainView.Ui_Main()
        self.form.setupUi(self)

        self.form.actionOpen.triggered.connect(self.onclick_open)
        self.form.actionSave.triggered.connect(self.onclick_save)
        self.form.actionSave_As.triggered.connect(self.onclick_saveas)
        self.form.actionNew.triggered.connect(self.onclick_new)
        self.form.actionCopy_CS.triggered.connect(self.onclick_copycs)

    def onclick_open(self):
        pass

    def onclick_save(self):
        pass

    def onclick_saveas(self):
        pass

    def onclick_new(self):
        pass

    def onclick_copycs(self):
        pass
