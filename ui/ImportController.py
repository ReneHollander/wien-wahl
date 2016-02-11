"""
Autor: Rene Hollander 5BHIT
"""
import csv

from PySide.QtGui import *

import os
from ui import ImportView
from ui.ContentTableModel import ContentTableModel
from ui.ImportModel import ImportModel


class ImportController(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.last_value = 0

        self.form = ImportView.Ui_Import()
        self.form.setupUi(self)

        self.model = ImportModel()
        self.table_model = ContentTableModel(self, self.model.items)
        self.form.contentTable.setModel(self.table_model)
        self.form.readButton.clicked.connect(self.onclick_read)
        self.form.fileExplorerButton.clicked.connect(self.onclick_fileexplorer)

    def onclick_read(self):
        try:
            self.model.read(self.form.pathEdit.text())
            self.table_model.generate_headers()
            self.table_model.reset()
        except FileNotFoundError:
            QMessageBox.critical(self, "Read Error", "Error reading CSV File:\nFile \"" + self.form.pathEdit.text() + "\" not found!", QMessageBox.Close)
        except csv.Error:
            QMessageBox.critical(self, "Read Error", "Error reading CSV File:\n File is not an valid CSV File!", QMessageBox.Close)
        except:
            QMessageBox.critical(self, "Read Error", "Error reading CSV File:\nAn unknown Error occured!", QMessageBox.Close)
            raise

    def onclick_fileexplorer(self):
        fileName = QFileDialog.getOpenFileName(self, self.tr("Open CSV File"), os.getcwd(), self.tr("CSV Files (*.csv *.tsv)"))
        self.form.pathEdit.setText(fileName[0])
