"""
Autor: Rene Hollander 5BHIT
"""
import csv
import sys

from PySide.QtGui import *

import os
from data.database import WienWahlDatabase
from data.dbconfig import DBConfig
from ui import MainView
from ui.ComputerPredictionController import ComputerPredictionController
from ui.MainModel import MainModel
from ui.command import EditCommand, DuplicateRowCommand, RemoveRowsCommand
from ui.itemdelegate import ItemDelegate


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
                self.wienwahldb = WienWahlDatabase(connectionstring=DBConfig.connection_string, electiondate="2015-10-11")
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

    def on_insert(self):
        pass

    def on_load(self):
        data = self.wienwahldb.load()
        self.model.contentTableModel.set_list(data)
        QMessageBox.information(self, "Loaded from database", "Successfully loaded all entries from the database")

    def on_write(self):
        self.wienwahldb.write(self.model.contentTableModel.list)
        QMessageBox.information(self, "Written to database", "Successfully wrote all entries to the database")

    def on_create_projection(self):
        cpc = ComputerPredictionController()
        cpc.show()

    def on_open(self):
        try:
            fileName = QFileDialog.getOpenFileName(self, self.tr("Open CSV File"), os.getcwd(), self.tr("CSV Files (*.csv *.tsv)"))[0]
            if fileName is not None and fileName is not "":
                self.model.fileName = fileName
                self.model.contentTableModel.open(self.model.fileName)
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
        pass

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
        command.newValue(str(clipboard.text()))

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

    def on_duplicate(self):
        if len(self.view.tableView.selectionModel().selectedIndexes()) == 0:
            QMessageBox.critical(self, "Error", "You must select the first column of the row you want to duplicate")
            return

        start, amount = self.get_selection()
        self.undoStack.beginMacro("Duplicate Row")
        self.undoStack.push(DuplicateRowCommand(self.model.contentTableModel, start))
        self.undoStack.endMacro()
        self.set_undo_redo_text()
        self.form.contentTable.reset()

    def on_cut(self):
        self.copy()
        index = self.form.contentTable.selectionModel().selectedIndexes()[0]
        command = EditCommand(self.model.contentTableModel, index)
        command.newValue("")
        self.undoStack.beginMacro("Cut")
        self.undoStack.push(command)
        self.undoStack.endMacro()
        self.set_undo_redo_text()
        self.form.contentTable.reset()

    def on_remove(self):
        if len(self.model.contentTableModel.list) == 0:
            QMessageBox.critical(self, "Error", "Removing rows from an empty table is not possible.")
            return
        start, amount = self.get_selection()
        if start != len(self.model.contentTableModel.list):
            self.undoStack.beginMacro("Remove Row(s)")
            self.undoStack.push(RemoveRowsCommand(self.model.contentTableModel, start, amount))
            self.undoStack.endMacro()
            self.set_undo_redo_text()
        else:
            QMessageBox.critical(self, "Error", "You need to choose the rows you want to remove by selecting the cells in the first column")
