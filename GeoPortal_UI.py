import os
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from multiprocessing import Pool
import printing1, printing2, printing3

processes = []


class Ui_MainWindow(object):
    def check_options(self):
        scripts = []
        # if self.metersCheckBox.isChecked():
        #     scripts.append("")

        if self.pinCheckBox.isChecked():
            scripts.append(printing1)
        if self.qarsCheckBox.isChecked():
            scripts.append(printing2)
        if self.poiCheckBox.isChecked():
            scripts.append(printing3)
        # if self.kmlOption.isChecked():
        #     scripts.append("polygonsToKML.py")
        return scripts

    def call_mains(self, script):
        script.main1()

    def call_functions(self):
        scripts = self.check_options()
        print(scripts)
        with Pool(processes=len(scripts)) as pool:
            pool.imap_unordered(self.call_mains, scripts)
            print("End of pool")
        print("Processes have ended.")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(437, 308)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pngegg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.executeScripts = QtWidgets.QPushButton(self.centralwidget)
        self.executeScripts.setGeometry(QtCore.QRect(150, 200, 121, 41))

        self.executeScripts.setFont(font)
        self.executeScripts.setObjectName("executeScripts")  # This is the button
        # self.executeScripts.clicked
        self.executeScripts.clicked.connect(self.call_functions)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 201, 111))

        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.metersCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.metersCheckBox.setGeometry(QtCore.QRect(10, 80, 111, 18))

        self.metersCheckBox.setFont(font)
        self.metersCheckBox.setObjectName("metersCheckBox")
        self.poiCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.poiCheckBox.setGeometry(QtCore.QRect(10, 60, 67, 18))

        self.poiCheckBox.setFont(font)
        self.poiCheckBox.setObjectName("poiCheckBox")
        self.pinCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.pinCheckBox.setGeometry(QtCore.QRect(10, 20, 131, 21))

        self.pinCheckBox.setFont(font)
        self.pinCheckBox.setObjectName("pinCheckBox")
        self.qarsCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.qarsCheckBox.setGeometry(QtCore.QRect(10, 40, 181, 21))

        self.qarsCheckBox.setFont(font)
        self.qarsCheckBox.setObjectName("qarsCheckBox")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 150, 451, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(240, 30, 171, 51))

        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.kmlOption = QtWidgets.QCheckBox(self.groupBox_2)
        self.kmlOption.setGeometry(QtCore.QRect(10, 20, 131, 21))

        self.kmlOption.setFont(font)
        self.kmlOption.setObjectName("kmlOption")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GeoPortal Services"))
        self.executeScripts.setText(_translate("MainWindow", "Extract"))
        self.groupBox.setTitle(_translate("MainWindow", "Scripts"))
        self.metersCheckBox.setText(_translate("MainWindow", "Meters (KIDs)"))
        self.poiCheckBox.setText(_translate("MainWindow", "POI"))
        self.pinCheckBox.setText(_translate("MainWindow", "Cadastre (PINs)"))
        self.qarsCheckBox.setText(_translate("MainWindow", "QARS (ZSB - Blueplates)"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Options"))
        self.kmlOption.setText(_translate("MainWindow", "Export PINs to KML"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
