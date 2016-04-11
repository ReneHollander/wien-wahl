"""
Autor: Rene Hollander 5BHIT
"""
import csv

from PySide.QtGui import *

import os
from ui import MainView
from ui.ContentTableModel import ContentTableModel
from ui.MainModel import MainModel


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

        self.model = MainModel()
        self.contentTableModel = ContentTableModel(self, self.model.items)
        self.form.contentTable.setModel(self.contentTableModel)

    def onclick_open(self):
        try:
            self.fileName = QFileDialog.getOpenFileName(self, self.tr("Open CSV File"), os.getcwd(), self.tr("CSV Files (*.csv *.tsv)"))[0]
            self.model.read(self.fileName)
            self.contentTableModel.generate_headers()
            self.contentTableModel.reset()
        except FileNotFoundError:
            QMessageBox.critical(self, "Read Error", "Error reading CSV File:\nFile \"" + self.fileName + "\" not found!", QMessageBox.Close)
        except csv.Error:
            QMessageBox.critical(self, "Read Error", "Error reading CSV File:\n File is not an valid CSV File!", QMessageBox.Close)
        except:
            QMessageBox.critical(self, "Read Error", "Error reading CSV File:\nAn unknown Error occured!", QMessageBox.Close)
            raise

    def onclick_save(self):
        pass

    def onclick_saveas(self):
        pass

    def onclick_new(self):
        pass

    def onclick_copycs(self):
        pass
