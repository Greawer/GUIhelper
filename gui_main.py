from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout
from listener import Listen
from clicker import Click, inputs
from gui import Ui_GUImain
from client import database
import client

clickedCollection = ""

class mainWindow(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_GUImain()
        self.ui.setupUi(self)
        self.ui.startClicker.clicked.connect(self.on_buttonStartClicker)
        self.ui.stopClicker.clicked.connect(self.on_buttonStopClicker)
        self.ui.startListener.clicked.connect(self.on_buttonStartListener)
        self.ui.stopListener.clicked.connect(self.on_buttonStopListener)
        self.ui.refreshList.clicked.connect(self.updateCollectionsList)
        self.ui.dropRecord.clicked.connect(self.dropRecord)
        self.ui.collectionsList.clicked.connect(self.updateClickledConnection)
        
    @pyqtSlot()
    def on_buttonStartListener(self):
        Listen.startKeyboardListener()

    @pyqtSlot()
    def on_buttonStopListener(self):
        Listen.stopKeyboardListener()

    @pyqtSlot()
    def on_buttonStartClicker(self):
        client.database()
        Click.startClicker()

    @pyqtSlot()
    def on_buttonStopClicker(self):
        Click.stopClicker()

    @pyqtSlot()
    def updateCollectionsList(self):
        collections = database.update_collections()
        self.ui.collectionsList.clear()
        self.ui.collectionsList.addItems(collections)
        
    @pyqtSlot()
    def dropRecord(self):
        client.database.drop(clickedCollection)
        self.updateCollectionsList()

    @pyqtSlot()
    def updateClickledConnection(self):
        global clickedCollection
        clickedCollection = str(self.ui.collectionsList.currentItem().text())