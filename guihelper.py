from _thread import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import click
from sqlalchemy import null
from PyQt5 import QtWidgets
import sys
import client
import gui
from listener import Listen
from clicker import Click

clickedCollection = "1"

class guiMenu(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = gui.windowMenu()
        self.ui.setupUi(self)
        self.ui.enterListener.clicked.connect(self.enterListener)
        self.ui.enterClicker.clicked.connect(self.enterClicker)
        
    @pyqtSlot()
    def enterListener(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        print('entering Listener')

    @pyqtSlot()
    def enterClicker(self):
        widget.setCurrentIndex(widget.currentIndex()+2)
        print('entering Clicker')

class guiListener(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = gui.windowListener()
        self.ui.setupUi(self)
        self.ui.startListener.clicked.connect(self.on_buttonStartListener)
        self.ui.stopListener.clicked.connect(self.on_buttonStopListener)
        self.ui.returnListener.clicked.connect(self.returnListener)
        
    @pyqtSlot()
    def on_buttonStartListener(self):
        Listen.startKeyboardListener()

    @pyqtSlot()
    def on_buttonStopListener(self):
        Listen.stopKeyboardListener()

    @pyqtSlot()
    def returnListener(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        print('returning')

class guiClicker(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = gui.windowClicker()
        self.ui.setupUi(self)
        self.ui.startClicker.clicked.connect(self.on_buttonStartClicker)
        self.ui.stopClicker.clicked.connect(self.on_buttonStopClicker)
        self.ui.refreshList.clicked.connect(self.updateCollectionsList)
        self.ui.dropRecord.clicked.connect(self.dropRecord)
        self.ui.collectionsList.clicked.connect(self.updateClickedConnection)
        self.ui.returnClicker.clicked.connect(self.returnClicker)

    @pyqtSlot()
    def on_buttonStartClicker(self):
        client.database()
        Click.startClicker(clickedCollection)

    @pyqtSlot()
    def on_buttonStopClicker(self):
        Click.stopClicker()

    @pyqtSlot()
    def updateCollectionsList(self):
        #try:
        collections = client.database.update_collections()
        self.ui.collectionsList.clear()
        self.ui.collectionsList.addItems(collections)
        #except:
        #    print("Error updating collections list.")     
        
    @pyqtSlot()
    def dropRecord(self):
        try:
            client.database.drop(clickedCollection)
            self.updateCollectionsList()
        except:
            print("Error connecting to the database.")        

    @pyqtSlot()
    def updateClickedConnection(self):
        try:
            global clickedCollection
            clickedCollection = str(self.ui.collectionsList.currentItem().text())
            print("updated clicked to "+str(clickedCollection))
        except:
            print("Error connecting to the database.")

    @pyqtSlot()
    def returnClicker(self):
        widget.setCurrentIndex(widget.currentIndex()-2)
        print('returning')

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = QtWidgets.QStackedWidget()    
    winMenu = guiMenu()
    winListener = guiListener()
    winClicker = guiClicker()
    widget.addWidget(winMenu)
    widget.addWidget(winListener)
    widget.addWidget(winClicker)
    widget.show()
    sys.exit(app.exec_())
