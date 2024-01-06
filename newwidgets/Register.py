from PyQt5 import QtCore, QtGui, QtWidgets


class Register(QtWidgets.QWidget):
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
        self.login = QtWidgets.QLineEdit(MainWindow)
        self.login.setGeometry(QtCore.QRect(190, 40, 251, 31))
        self.login.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                 "border-radius:15px;\n"
                                 "padding-left: 5px;")
        self.login.setObjectName("login")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(190, 100, 251, 31))
        self.email.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                 "border-radius:15px;\n"
                                 "padding-left: 5px;")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(190, 160, 251, 31))
        self.password.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                    "border-radius:15px;\n"
                                    "padding-left: 5px;")
        self.password.setObjectName("password")
        self.passwordr = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordr.setGeometry(QtCore.QRect(190, 220, 251, 31))
        self.passwordr.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                     "border-radius:15px;\n"
                                     "padding-left: 5px;")
        self.passwordr.setObjectName("passwordr")
        self.isteacher_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.isteacher_checkbox.setGeometry(QtCore.QRect(260, 270, 91, 20))
        self.isteacher_checkbox.setObjectName("isteacher_checkbox")
        self.reg_button = QtWidgets.QPushButton(self.centralwidget)
        self.reg_button.setGeometry(QtCore.QRect(240, 310, 121, 41))
        self.reg_button.setStyleSheet("background-color: rgb(103, 226, 60);\n"
                                      "border: 0.5px solid rgb(61, 56, 70);\n"
                                      "border-radius:10px;\n")
        self.reg_button.setObjectName("reg_button")
        self.login_button_link = QtWidgets.QPushButton(self.centralwidget)
        self.login_button_link.setGeometry(QtCore.QRect(250, 360, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.login_button_link.setFont(font)
        self.login_button_link.setStyleSheet("font-color: rgb(0,0,0);\n"
                                             "background-color: rgb(28, 113, 216);\n"
                                             "border: 0.5px solid rgb(61, 56, 70);\n"
                                             "border-radius:10px;\n")
        self.login_button_link.setObjectName("login_button_link")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login.setPlaceholderText(_translate("MainWindow", "Логін"))
        self.email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.password.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.passwordr.setPlaceholderText(
            _translate("MainWindow", "Повторення паролю"))
        self.isteacher_checkbox.setText(_translate("MainWindow", "Я вчитель"))
        self.reg_button.setText(_translate("MainWindow", "Зареєструватися"))
        self.login_button_link.setText(_translate("MainWindow", "Увійти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Register()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
