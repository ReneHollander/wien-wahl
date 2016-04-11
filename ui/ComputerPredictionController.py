"""
Autor: Rene Hollander 5BHIT
"""

from PySide.QtGui import *

from ui.MatplotlibWidget import MatplotlibWidget


class ComputerPredictionController(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.plot = MatplotlibWidget()
        layout.addWidget(self.plot)

        self.setWindowTitle("Predictions")
        self.resize(800, 600)
        self.setModal(True)
        self.exec_()