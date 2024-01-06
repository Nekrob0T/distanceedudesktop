from PyQt5 import QtCore, QtGui, QtWidgets


class Login(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("font: 8pt \"Comic Sans MS\";")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(180, 100, 251, 31))
        self.login.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                 "border-radius:15px;\n"
                                 "padding-left: 5px;\n"
                                 "")
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(180, 180, 251, 31))
        self.password.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                    "border-radius:15px;\n"
                                    "padding-left: 5px;")
        self.password.setObjectName("password")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(240, 290, 121, 41))
        self.login_button.setStyleSheet("background-color: rgb(103, 226, 60);\n"
                                        "border: 0.5px solid rgb(61, 56, 70);\n"
                                        "border-radius:10px;\n"
                                        "")
        self.login_button.setObjectName("login_button")
        self.reg_button_link = QtWidgets.QPushButton(self.centralwidget)
        self.reg_button_link.setGeometry(QtCore.QRect(250, 350, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.reg_button_link.setFont(font)
        self.reg_button_link.setStyleSheet("color: rgb(0,0,0);\n"
                                           "background-color: rgb(28, 113, 216);\n"
                                           "border: 0.5px solid rgb(61, 56, 70);\n"
                                           "border-radius:10px;\n"
                                           "")
        self.reg_button_link.setObjectName("reg_button_link")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login.setPlaceholderText(_translate("MainWindow", "Логін"))
        self.login_button.setText(_translate("MainWindow", "Увійти"))
        self.reg_button_link.setText(
            _translate("MainWindow", "Зареєструватися"))
        self.password.setPlaceholderText(_translate("MainWindow", "Пароль"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
