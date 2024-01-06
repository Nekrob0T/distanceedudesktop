from PyQt5 import QtCore, QtGui, QtWidgets


class Settings(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 360)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.icon_button = QtWidgets.QPushButton(self.centralwidget)
        self.icon_button.setGeometry(QtCore.QRect(270, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.icon_button.setFont(font)
        self.icon_button.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.icon_button.setObjectName("icon_button")
        self.surname = QtWidgets.QLineEdit(self.centralwidget)
        self.surname.setGeometry(QtCore.QRect(140, 130, 171, 31))
        self.surname.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                   "border-radius:15px;\n"
                                   "padding-left: 5px;\n"
                                   "")
        self.surname.setObjectName("surname")
        self.name = QtWidgets.QLineEdit(MainWindow)
        self.name.setGeometry(QtCore.QRect(330, 130, 171, 31))
        self.name.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                "border-radius:15px;\n"
                                "padding-left: 5px;")
        self.name.setObjectName("name")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(330, 210, 171, 31))
        self.email.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                 "border-radius:15px;\n"
                                 "padding-left: 5px;")
        self.email.setObjectName("email")
        self.pobat = QtWidgets.QLineEdit(self.centralwidget)
        self.pobat.setGeometry(QtCore.QRect(140, 210, 171, 31))
        self.pobat.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                 "border-radius:15px;\n"
                                 "padding-left: 5px;")
        self.pobat.setObjectName("pobat")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(270, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("background-color: rgb(103, 226, 60);")
        self.save_button.setObjectName("save_button")
        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(10, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.icon_button.setText(_translate("MainWindow", "Аватар"))
        self.save_button.setText(_translate("MainWindow", "Зберегти"))
        self.return_button.setText(_translate("MainWindow", "<"))
        self.surname.setPlaceholderText(_translate("MainWindow", "Прізвище"))
        self.name.setPlaceholderText(_translate("MainWindow", "Ім\'я"))
        self.email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.pobat.setPlaceholderText(_translate("MainWindow", "По-батькові"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Settings()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
