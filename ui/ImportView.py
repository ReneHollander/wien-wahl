# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/ui/Import.ui'
#
# Created: Thu Feb 11 12:23:37 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Import(object):
    def setupUi(self, Import):
        Import.setObjectName("Import")
        Import.resize(800, 600)
        self.centralWidget = QtGui.QWidget(Import)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.contentTable = QtGui.QTableView(self.centralWidget)
        self.contentTable.setObjectName("contentTable")
        self.verticalLayout.addWidget(self.contentTable)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.readButton = QtGui.QPushButton(self.centralWidget)
        self.readButton.setObjectName("readButton")
        self.horizontalLayout.addWidget(self.readButton)
        self.pathEdit = QtGui.QLineEdit(self.centralWidget)
        self.pathEdit.setObjectName("pathEdit")
        self.horizontalLayout.addWidget(self.pathEdit)
        self.fileExplorerButton = QtGui.QPushButton(self.centralWidget)
        self.fileExplorerButton.setObjectName("fileExplorerButton")
        self.horizontalLayout.addWidget(self.fileExplorerButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Import.setCentralWidget(self.centralWidget)

        self.retranslateUi(Import)
        QtCore.QMetaObject.connectSlotsByName(Import)

    def retranslateUi(self, Import):
        Import.setWindowTitle(QtGui.QApplication.translate("Import", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.readButton.setText(QtGui.QApplication.translate("Import", "Read", None, QtGui.QApplication.UnicodeUTF8))
        self.fileExplorerButton.setText(QtGui.QApplication.translate("Import", "...", None, QtGui.QApplication.UnicodeUTF8))

