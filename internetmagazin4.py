from PyQt5.QtWidgets import QApplication
from mainWindow import mainWindow
import sys


app = QApplication(sys.argv)
mw=mainWindow()
mw.show()
sys.exit(app.exec_())

