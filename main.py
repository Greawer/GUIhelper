from _thread import *
import gui_main
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = gui_main.mainWindow()
    widget.show()
    sys.exit(app.exec_())