from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ohmmodel(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 380)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.obvodka_textbrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.obvodka_textbrowser.setGeometry(QtCore.QRect(180, 90, 281, 111))
        self.obvodka_textbrowser.setStyleSheet("QTextBrowser\n"
                                               "{\n"
                                               "background-color: rgba(255, 255, 255, 0);\n"
                                               "border: 2px solid black;\n"
                                               "border-radius: 15px;\n"
                                               "}")
        self.obvodka_textbrowser.setObjectName("obvodka_textbrowser")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(210, 160, 221, 91))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.cylindr_label = QtWidgets.QLabel(self.centralwidget)
        self.cylindr_label.setGeometry(QtCore.QRect(210, 160, 221, 91))
        self.cylindr_label.setToolTipDuration(0)
        self.cylindr_label.setStyleSheet("")
        self.cylindr_label.setText("")
        self.cylindr_label.setPixmap(
            QtGui.QPixmap("./img/exp/cylinder.png"))
        self.cylindr_label.setScaledContents(True)
        self.cylindr_label.setObjectName("cylindr_label")
        self.groupBox.raise_()

        self.amper_label = QtWidgets.QLabel(self.centralwidget)
        self.amper_label.setGeometry(QtCore.QRect(290, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.amper_label.setFont(font)
        self.amper_label.setObjectName("amper_label")
        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(20, 20, 31, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")
        self.obvodkares_textbrowser = QtWidgets.QTextBrowser(
            self.centralwidget)
        self.obvodkares_textbrowser.setGeometry(QtCore.QRect(50, 260, 141, 91))
        self.obvodkares_textbrowser.setStyleSheet("QTextBrowser\n"
                                                  "{\n"
                                                  "background-color: rgba(255, 255, 255, 0);\n"
                                                  "border: 1px solid black;\n"
                                                  "border-radius: 15px;\n"
                                                  "}")
        self.obvodkares_textbrowser.setObjectName("obvodkares_textbrowser")
        self.res_label = QtWidgets.QLabel(self.centralwidget)
        self.res_label.setGeometry(QtCore.QRect(110, 270, 47, 13))
        self.res_label.setObjectName("res_label")
        self.vimirres_label = QtWidgets.QLabel(self.centralwidget)
        self.vimirres_label.setGeometry(QtCore.QRect(70, 290, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vimirres_label.setFont(font)
        self.vimirres_label.setObjectName("vimirres_label")
        self.oneres_label = QtWidgets.QLabel(self.centralwidget)
        self.oneres_label.setGeometry(QtCore.QRect(70, 330, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.oneres_label.setFont(font)
        self.oneres_label.setObjectName("oneres_label")
        self.stores_label = QtWidgets.QLabel(self.centralwidget)
        self.stores_label.setGeometry(QtCore.QRect(150, 330, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stores_label.setFont(font)
        self.stores_label.setObjectName("stores_label")
        self.tenvolt_label = QtWidgets.QLabel(self.centralwidget)
        self.tenvolt_label.setGeometry(QtCore.QRect(490, 330, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tenvolt_label.setFont(font)
        self.tenvolt_label.setObjectName("tenvolt_label")
        self.obvodkavolt_textbrowser = QtWidgets.QTextBrowser(
            self.centralwidget)
        self.obvodkavolt_textbrowser.setGeometry(
            QtCore.QRect(470, 260, 141, 91))
        self.obvodkavolt_textbrowser.setStyleSheet("QTextBrowser\n"
                                                   "{\n"
                                                   "background-color: rgba(255, 255, 255, 0);\n"
                                                   "border: 1px solid black;\n"
                                                   "border-radius: 15px;\n"
                                                   "}")
        self.obvodkavolt_textbrowser.setObjectName("obvodkavolt_textbrowser")
        self.vimirvolt_label = QtWidgets.QLabel(self.centralwidget)
        self.vimirvolt_label.setGeometry(QtCore.QRect(490, 290, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vimirvolt_label.setFont(font)
        self.vimirvolt_label.setObjectName("vimirvolt_label")
        self.volt_label = QtWidgets.QLabel(self.centralwidget)
        self.volt_label.setGeometry(QtCore.QRect(520, 270, 51, 16))
        self.volt_label.setObjectName("volt_label")
        self.tisyachavolt_label = QtWidgets.QLabel(self.centralwidget)
        self.tisyachavolt_label.setGeometry(QtCore.QRect(570, 330, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tisyachavolt_label.setFont(font)
        self.tisyachavolt_label.setObjectName("tisyachavolt_label")
        self.res_slider = QtWidgets.QSlider(self.centralwidget)
        self.res_slider.setGeometry(QtCore.QRect(60, 310, 121, 22))
        self.res_slider.setMinimum(1)
        self.res_slider.setMaximum(100)
        self.res_slider.setValue(50)
        self.res_slider.setOrientation(QtCore.Qt.Horizontal)
        self.res_slider.setInvertedAppearance(False)
        self.res_slider.setInvertedControls(False)
        self.res_slider.setObjectName("res_slider")
        self.res_slider.valueChanged.connect(self.resValueChanged)
        self.res_slider.sliderReleased.connect(self.generatePoints)
        self.volt_slider = QtWidgets.QSlider(self.centralwidget)
        self.volt_slider.setGeometry(QtCore.QRect(480, 310, 121, 22))
        self.volt_slider.setMinimum(10)
        self.volt_slider.setMaximum(1000)
        self.volt_slider.setValue(500)
        self.volt_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volt_slider.setInvertedAppearance(False)
        self.volt_slider.setInvertedControls(False)
        self.volt_slider.setObjectName("volt_slider")
        self.volt_slider.valueChanged.connect(self.voltValueChanged)
        MainWindow.setCentralWidget(self.centralwidget)

        self.voltValueChanged()
        self.resValueChanged()
        self.generatePoints()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.amper_label.setText(_translate("MainWindow", "I = 9.90 A"))
        self.return_button.setText(_translate("MainWindow", "<"))
        self.res_label.setText(_translate("MainWindow", "Опір"))
        self.vimirres_label.setText(_translate("MainWindow", "50"))
        self.oneres_label.setText(_translate("MainWindow", "1"))
        self.stores_label.setText(_translate("MainWindow", "100"))
        self.tenvolt_label.setText(_translate("MainWindow", "10"))
        self.vimirvolt_label.setText(_translate(
            "MainWindow", str(self.volt_slider.value())))
        self.volt_label.setText(_translate("MainWindow", "Вольтаж"))
        self.tisyachavolt_label.setText(_translate("MainWindow", "1000"))

    def voltValueChanged(self):
        _translate = QtCore.QCoreApplication.translate
        self.vimirvolt_label.setText(_translate(
            "MainWindow", str(self.volt_slider.value())))
        amper = round(self.volt_slider.value() / self.res_slider.value(), 2)
        self.amper_label.setText(_translate(
            "MainWindow", "I = " + str(amper) + " A"))

    def resValueChanged(self):
        _translate = QtCore.QCoreApplication.translate
        self.vimirres_label.setText(_translate(
            "MainWindow", str(self.res_slider.value())))
        amper = round(self.volt_slider.value() / self.res_slider.value(), 2)
        self.amper_label.setText(_translate(
            "MainWindow", "I = " + str(amper) + " A"))

    def generatePoints(self):
        times = self.res_slider.value() * 8
        for point in self.groupBox.findChildren(QtWidgets.QLabel):
            point.deleteLater()

        for i in range(0, times):
            self.point = QtWidgets.QLabel(self.groupBox)
            self.point.setGeometry(QtCore.QRect(random.randrange(
                20, 195), random.randrange(10, 80), 2, 2))
            # self.point.setGeometry(QtCore.QRect(0, 0, 30, 30))
            self.point.setStyleSheet("background-color: #000")
            self.point.setText("")
            self.point.setObjectName("point_" + str(i))
            self.point.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ohmmodel()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
