# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GUImain(object):
    def setupUi(self, GUImain):
        GUImain.setObjectName("GUImain")
        GUImain.resize(401, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(GUImain)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 401, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.startClicker = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.startClicker.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.startClicker.setObjectName("startClicker")
        self.horizontalLayout.addWidget(self.startClicker)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.stopClicker = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stopClicker.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.stopClicker.setObjectName("stopClicker")
        self.horizontalLayout.addWidget(self.stopClicker)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.startListener = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.startListener.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.startListener.setObjectName("startListener")
        self.horizontalLayout_2.addWidget(self.startListener)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.stopListener = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stopListener.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.stopListener.setObjectName("stopListener")
        self.horizontalLayout_2.addWidget(self.stopListener)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)

        self.retranslateUi(GUImain)
        QtCore.QMetaObject.connectSlotsByName(GUImain)

    def retranslateUi(self, GUImain):
        _translate = QtCore.QCoreApplication.translate
        GUImain.setWindowTitle(_translate("GUImain", "Dialog"))
        self.startClicker.setText(_translate("GUImain", "Start Clicker"))
        self.stopClicker.setText(_translate("GUImain", "Stop Clicker"))
        self.startListener.setText(_translate("GUImain", "Start Listener"))
        self.stopListener.setText(_translate("GUImain", "Stop Listener"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    GUImain = QtWidgets.QDialog()
#    ui = Ui_GUImain()
#    ui.setupUi(GUImain)
#    GUImain.show()
#    sys.exit(app.exec_())