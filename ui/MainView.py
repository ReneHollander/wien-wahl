# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/ui/Main.ui'
#
# Created: Tue Apr 19 11:16:33 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.contentTable = QtGui.QTableView(self.centralwidget)
        self.contentTable.setObjectName("contentTable")
        self.gridLayout.addWidget(self.contentTable, 0, 0, 1, 1)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuDatabase = QtGui.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(Main)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(Main)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtGui.QAction(Main)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionNew = QtGui.QAction(Main)
        self.actionNew.setObjectName("actionNew")
        self.actionCopy = QtGui.QAction(Main)
        self.actionCopy.setObjectName("actionCopy")
        self.actionControlQ = QtGui.QAction(Main)
        self.actionControlQ.setObjectName("actionControlQ")
        self.actionClose = QtGui.QAction(Main)
        self.actionClose.setObjectName("actionClose")
        self.actionPaste = QtGui.QAction(Main)
        self.actionPaste.setObjectName("actionPaste")
        self.actionUndo = QtGui.QAction(Main)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(Main)
        self.actionRedo.setObjectName("actionRedo")
        self.actionDuplicate_Row = QtGui.QAction(Main)
        self.actionDuplicate_Row.setObjectName("actionDuplicate_Row")
        self.actionCut = QtGui.QAction(Main)
        self.actionCut.setObjectName("actionCut")
        self.actionRemove_Row = QtGui.QAction(Main)
        self.actionRemove_Row.setObjectName("actionRemove_Row")
        self.actionInsert_Row = QtGui.QAction(Main)
        self.actionInsert_Row.setObjectName("actionInsert_Row")
        self.actionConnectDisconnect = QtGui.QAction(Main)
        self.actionConnectDisconnect.setObjectName("actionConnectDisconnect")
        self.actionLoad = QtGui.QAction(Main)
        self.actionLoad.setEnabled(False)
        self.actionLoad.setObjectName("actionLoad")
        self.actionWrite = QtGui.QAction(Main)
        self.actionWrite.setEnabled(False)
        self.actionWrite.setObjectName("actionWrite")
        self.actionCreate_Projection = QtGui.QAction(Main)
        self.actionCreate_Projection.setEnabled(False)
        self.actionCreate_Projection.setObjectName("actionCreate_Projection")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionInsert_Row)
        self.menuEdit.addAction(self.actionDuplicate_Row)
        self.menuEdit.addAction(self.actionRemove_Row)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuDatabase.addAction(self.actionConnectDisconnect)
        self.menuDatabase.addAction(self.actionLoad)
        self.menuDatabase.addAction(self.actionWrite)
        self.menuDatabase.addAction(self.actionCreate_Projection)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Main)
        QtCore.QObject.connect(self.actionControlQ, QtCore.SIGNAL("triggered()"), Main.close)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(QtGui.QApplication.translate("Main", "Main", None, QtGui.QApplication.UnicodeUTF8))
        self.contentTable.setToolTip(QtGui.QApplication.translate("Main", "Wahlergebnisse", None, QtGui.QApplication.UnicodeUTF8))
        self.contentTable.setStatusTip(QtGui.QApplication.translate("Main", "Wahlergebnisse", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setToolTip(QtGui.QApplication.translate("Main", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setStatusTip(QtGui.QApplication.translate("Main", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("Main", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setToolTip(QtGui.QApplication.translate("Main", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setStatusTip(QtGui.QApplication.translate("Main", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("Main", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setToolTip(QtGui.QApplication.translate("Main", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setStatusTip(QtGui.QApplication.translate("Main", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("Main", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDatabase.setToolTip(QtGui.QApplication.translate("Main", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDatabase.setStatusTip(QtGui.QApplication.translate("Main", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDatabase.setTitle(QtGui.QApplication.translate("Main", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("Main", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setStatusTip(QtGui.QApplication.translate("Main", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("Main", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setStatusTip(QtGui.QApplication.translate("Main", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("Main", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setStatusTip(QtGui.QApplication.translate("Main", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("Main", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setStatusTip(QtGui.QApplication.translate("Main", "New File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("Main", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setStatusTip(QtGui.QApplication.translate("Main", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionControlQ.setText(QtGui.QApplication.translate("Main", "ControlQ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionControlQ.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("Main", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setStatusTip(QtGui.QApplication.translate("Main", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("Main", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setStatusTip(QtGui.QApplication.translate("Main", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("Main", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setStatusTip(QtGui.QApplication.translate("Main", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("Main", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setStatusTip(QtGui.QApplication.translate("Main", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+Shift+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDuplicate_Row.setText(QtGui.QApplication.translate("Main", "Duplicate Row", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDuplicate_Row.setStatusTip(QtGui.QApplication.translate("Main", "Duplicate Row", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDuplicate_Row.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("Main", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setStatusTip(QtGui.QApplication.translate("Main", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+Y", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_Row.setText(QtGui.QApplication.translate("Main", "Remove Row", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_Row.setStatusTip(QtGui.QApplication.translate("Main", "Remove Row", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_Row.setShortcut(QtGui.QApplication.translate("Main", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsert_Row.setText(QtGui.QApplication.translate("Main", "Insert Row", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsert_Row.setStatusTip(QtGui.QApplication.translate("Main", "Insert Row", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsert_Row.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnectDisconnect.setText(QtGui.QApplication.translate("Main", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnectDisconnect.setStatusTip(QtGui.QApplication.translate("Main", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("Main", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setStatusTip(QtGui.QApplication.translate("Main", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWrite.setText(QtGui.QApplication.translate("Main", "Write", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWrite.setStatusTip(QtGui.QApplication.translate("Main", "Write", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate_Projection.setText(QtGui.QApplication.translate("Main", "Create Projection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate_Projection.setStatusTip(QtGui.QApplication.translate("Main", "Create Projection", None, QtGui.QApplication.UnicodeUTF8))

