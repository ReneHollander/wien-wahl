import sys

from PySide.QtGui import QApplication

from ui.MainWindowController import MainWindowController

app = QApplication(sys.argv)
c = MainWindowController()
c.show()
sys.exit(app.exec_())
