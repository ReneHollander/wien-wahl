"""
Autor: Rene Hollander 5BHIT
"""
import csv
import sys

from PySide.QtGui import *

import os
from data.database import WienWahlDatabase, default_header
from data.dbconfig import DBConfig
from ui import MainView
from ui.MainModel import MainModel
from ui.command import EditCommand, DuplicateRowCommand, RemoveRowCommand, InsertRowCommand
from ui.itemdelegate import ItemDelegate
import numpy
from matplotlib import pyplot as plt


class MainController(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.last_value = 0

        self.undoStack = QUndoStack()

        self.form = MainView.Ui_Main()
        self.form.setupUi(self)

        self.form.actionOpen.triggered.connect(self.on_open)
        self.form.actionSave.triggered.connect(self.on_save)
        self.form.actionSave_As.triggered.connect(self.on_saveas)
        self.form.actionNew.triggered.connect(self.on_new)
        self.form.actionCopy.triggered.connect(self.on_copy)
        self.form.actionPaste.triggered.connect(self.on_paste)
        self.form.actionUndo.triggered.connect(self.on_undo)
        self.form.actionRedo.triggered.connect(self.on_redo)
        self.form.actionCut.triggered.connect(self.on_cut)
        self.form.actionDuplicate_Row.triggered.connect(self.on_duplicate)
        self.form.actionRemove_Row.triggered.connect(self.on_remove)
        self.form.actionInsert_Row.triggered.connect(self.on_insert)
        self.form.actionConnectDisconnect.triggered.connect(self.on_connectdisconnect)
        self.form.actionLoad.triggered.connect(self.on_load)
        self.form.actionWrite.triggered.connect(self.on_write)
        self.form.actionCreate_Projection.triggered.connect(self.on_create_projection)

        self.model = MainModel(self)
        self.form.contentTable.setModel(self.model.contentTableModel)
        self.form.contentTable.setItemDelegate(ItemDelegate(self.undoStack, self.set_undo_redo_text))

        self.wienwahldb = None

    def set_undo_redo_text(self):
        undo = "Undo"
        redo = "Redo"
        undo_text = self.undoStack.undoText()
        redo_text = self.undoStack.redoText()
        if undo_text:
            undo += " \"" + undo_text + "\""
        if redo_text:
            redo += " \"" + redo_text + "\""
        self.form.actionUndo.setText(undo)
        self.form.actionRedo.setText(redo)

    def on_connectdisconnect(self):
        if self.wienwahldb is None:
            try:
                connection_string, ok = QInputDialog.getText(self, "Connection String", "Please enter the Database Connection String", QLineEdit.Normal, DBConfig.connection_string)
                if ok:
                    election_date, ok = QInputDialog.getText(self, "Election Date", "Please enter the Election Date", QLineEdit.Normal, "2015-10-11")
                    if ok:
                        self.wienwahldb = WienWahlDatabase(connectionstring=connection_string, electiondate=election_date)
                        QMessageBox.information(self, "Connected to database", "Successfully connected to database")
                        self.form.actionConnectDisconnect.setText("Disconnect")
                        self.form.actionConnectDisconnect.setToolTip("Disconnect")
                        self.form.actionConnectDisconnect.setStatusTip("Disconnect")
                        self.form.actionConnectDisconnect.setIconText("Disconnect")
                        self.form.actionLoad.setEnabled(True)
                        self.form.actionWrite.setEnabled(True)
                        self.form.actionCreate_Projection.setEnabled(True)
            except:
                QMessageBox.critical(self, "Connect Error", "Error connecting to Database:\n" + sys.exc_info()[0], QMessageBox.Close)
                raise
        else:
            self.form.actionConnectDisconnect.setText("Connect")
            self.form.actionConnectDisconnect.setToolTip("Connect")
            self.form.actionConnectDisconnect.setStatusTip("Connect")
            self.form.actionConnectDisconnect.setIconText("Connect")
            self.form.actionLoad.setEnabled(False)
            self.form.actionWrite.setEnabled(False)
            self.form.actionCreate_Projection.setEnabled(False)
            self.wienwahldb.close()
            self.wienwahldb = None
            QMessageBox.information(self, "Disconnected from database", "Successfully disconnected from database")

    def on_load(self):
        header, data = self.wienwahldb.load()
        self.model.contentTableModel.set_list(data, header=header)
        QMessageBox.information(self, "Loaded from database", "Successfully loaded all entries from the database")

    def on_write(self):
        self.wienwahldb.write(self.model.contentTableModel.list)
        QMessageBox.information(self, "Written to database", "Successfully wrote all entries to the database")

    def on_create_projection(self):
        projection_data = self.wienwahldb.create_projection()
        print("Hochrechnung:")
        for key, value in projection_data.items():
            print(key + ": " + str(value))
        print("\n")
        ind = numpy.arange(len(projection_data))
        width = 0.5
        plt.bar(ind, list(projection_data.values()), width, color='r')
        plt.ylabel('%')
        plt.xlabel('Parteien')
        plt.title('Wien Wahl Hochrechnung')
        plt.xticks(ind + width / 2, list(projection_data.keys()))
        plt.yticks(numpy.arange(0, 61, 5))
        plt.show()

    def on_open(self):
        try:
            fileName = QFileDialog.getOpenFileName(self, self.tr("Open CSV File"), os.getcwd(), self.tr("CSV Files (*.csv *.tsv)"))[0]
            if fileName is not None and fileName is not "":
                append_or_override = False
                if self.model.fileName is not None:
                    append_or_override = self.show_append_override_dialog()
                self.model.fileName = fileName
                self.model.contentTableModel.open(self.model.fileName, clear=append_or_override)
                self.undoStack.clear()
                self.set_undo_redo_text()
        except FileNotFoundError:
            QMessageBox.critical(self, "Read Error", "Error reading CSV File:\nFile \"" + self.fileName + "\" not found!", QMessageBox.Close)
        except csv.Error:
            QMessageBox.critical(self, "Read Error", "Error reading CSV File:\n File is not an valid CSV File!", QMessageBox.Close)
        except:
            QMessageBox.critical(self, "Read Error", "Error reading CSV File:\nAn unknown Error occured!", QMessageBox.Close)
            raise

    def on_save(self):
        if self.model.fileName is not None and self.model.fileName is not "":
            self.model.contentTableModel.save(self.model.fileName)
        else:
            fileName = QFileDialog.getSaveFileName(self, caption="Save CSV File", dir=os.getcwd(), filter="CSV Files (*.csv *.tsv)")[0]
            if fileName is not None and fileName is not "":
                self.model.contentTableModel.save(fileName)

    def on_saveas(self):
        fileName = QFileDialog.getSaveFileName(self, caption="Save CSV File", dir=os.getcwd(), filter="CSV Files (*.csv *.tsv)")[0]
        if fileName is not None and fileName is not "":
            self.model.contentTableModel.save(fileName)

    def on_new(self):
        text, ok = QInputDialog.getText(self, "Parties", "Enter the parties here, separated with ';'", QLineEdit.Normal, "SPOE;FPOE;OEVP;GRUE;NEOS;WWW;ANDAS;GFW;SLP;WIFF;M;FREIE")
        if ok:
            headers = default_header + text.split(";")
            self.model.fileName = None
            self.model.contentTableModel.set_list([], header=headers)
            self.undoStack.clear()
            self.set_undo_redo_text()

    def on_copy(self):
        if len(self.form.contentTable.selectionModel().selectedIndexes()) == 0:
            return

        clipboard = QApplication.clipboard()
        selected_index = self.form.contentTable.selectionModel().selectedIndexes()[0]
        selected_text = str(self.model.contentTableModel.data(selected_index))
        clipboard.setText(selected_text)

    def on_paste(self):
        if len(self.form.contentTable.selectionModel().selectedIndexes()) == 0:
            return

        clipboard = QApplication.clipboard()
        index = self.form.contentTable.selectionModel().selectedIndexes()[0]
        command = EditCommand(self.model.contentTableModel, index)
        command.newValue = str(clipboard.text())

        self.undoStack.beginMacro("Paste")
        self.undoStack.push(command)
        self.undoStack.endMacro()
        self.set_undo_redo_text()
        self.form.contentTable.reset()

    def on_undo(self):
        self.undoStack.undo()
        self.set_undo_redo_text()
        self.form.contentTable.reset()

    def on_redo(self):
        self.undoStack.redo()
        self.set_undo_redo_text()
        self.form.contentTable.reset()

    def on_duplicate(self):
        if self.get_selected_cell() is not None:
            index = self.form.contentTable.model().index(self.get_selected_cell()[1], self.get_selected_cell()[0])
            self.undoStack.beginMacro("Duplicate Row")
            self.undoStack.push(DuplicateRowCommand(self.model.contentTableModel, self.get_selected_cell()))
            self.undoStack.endMacro()
            self.set_undo_redo_text()
            self.form.contentTable.reset()
            self.form.contentTable.selectionModel().select(index, QItemSelectionModel.Select)

    def on_insert(self):
        if self.get_selected_row() is not None:
            self.undoStack.beginMacro("Add Row")
            self.undoStack.push(InsertRowCommand(self.model.contentTableModel, self.get_selected_row() + 1))
            self.undoStack.endMacro()
            self.set_undo_redo_text()
        else:
            self.undoStack.beginMacro("Add Row")
            self.undoStack.push(InsertRowCommand(self.model.contentTableModel, 0))
            self.undoStack.endMacro()
            self.set_undo_redo_text()

    def on_cut(self):
        self.on_copy()
        index = self.form.contentTable.selectionModel().selectedIndexes()[0]
        command = EditCommand(self.model.contentTableModel, index)
        command.newValue = ""
        self.undoStack.beginMacro("Cut")
        self.undoStack.push(command)
        self.undoStack.endMacro()
        self.set_undo_redo_text()
        self.form.contentTable.reset()

    def on_remove(self):
        if self.get_selected_row() is not None:
            index = self.form.contentTable.model().index(self.get_selected_cell()[1], self.get_selected_cell()[0])
            self.undoStack.beginMacro("Remove Row")
            self.undoStack.push(RemoveRowCommand(self.model.contentTableModel, self.get_selected_row()))
            self.undoStack.endMacro()
            self.set_undo_redo_text()
            self.form.contentTable.selectionModel().select(index, QItemSelectionModel.Select)

    def show_append_override_dialog(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Append or Override")
        msgBox.setText("Append or override the current entries?")
        msgBox.addButton("Append", QMessageBox.YesRole)
        msgBox.addButton("Override", QMessageBox.NoRole)
        return msgBox.exec_()

    def get_zero_column_selected_indexes(self):
        selected_indexes = self.form.contentTable.selectedIndexes()
        if not selected_indexes:
            return
        return [index for index in selected_indexes if not index.column()]

    def get_selection(self):
        zero_column_selected_indexes = self.get_zero_column_selected_indexes()
        if not zero_column_selected_indexes:
            return self.model.contentTableModel.rowCount(self), 1
        first_zero_column_selected_index = zero_column_selected_indexes[0]
        zero_column_selected_indexes = self.get_zero_column_selected_indexes()

        if not first_zero_column_selected_index or not first_zero_column_selected_index.isValid():
            return False
        startingrow = first_zero_column_selected_index.row()

        return startingrow, len(zero_column_selected_indexes)

    def get_selected_cells(self):
        selected = []
        for selected_index in self.form.contentTable.selectedIndexes():
            selected.append((selected_index.column(), selected_index.row()))
        return selected

    def get_selected_cell(self):
        selected = self.get_selected_cells()
        if len(selected) == 1:
            return selected[0]
        return None

    def get_selected_rows(self):
        rows = []
        for index in self.get_selected_cells():
            rows.append(index[1])
        return rows

    def get_selected_row(self):
        rows = self.get_selected_rows()
        if len(rows) == 1:
            return rows[0]
