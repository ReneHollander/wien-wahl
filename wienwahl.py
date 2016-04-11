import sys

from PySide.QtGui import QApplication

from ui.MainController import MainController

app = QApplication(sys.argv)
c = MainController()
c.show()
sys.exit(app.exec_())
