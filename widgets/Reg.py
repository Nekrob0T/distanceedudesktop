# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Register.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PyProgram(object):
    def setupUi(self, PyProgram):
        PyProgram.setObjectName("PyProgram")
        PyProgram.resize(640, 400)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        PyProgram.setFont(font)
        PyProgram.setStyleSheet("font: 8pt \"Comic Sans MS\";")
        self.login_label = QtWidgets.QLabel(PyProgram)
        self.login_label.setGeometry(QtCore.QRect(190, 20, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("font-size:10pt;")
        self.login_label.setObjectName("login_label")
        self.login = QtWidgets.QLineEdit(PyProgram)
        self.login.setGeometry(QtCore.QRect(190, 40, 251, 31))
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(PyProgram)
        self.password.setGeometry(QtCore.QRect(190, 160, 251, 31))
        self.password.setObjectName("password")
        self.password_label = QtWidgets.QLabel(PyProgram)
        self.password_label.setGeometry(QtCore.QRect(190, 140, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("font-size:10pt;")
        self.password_label.setObjectName("password_label")
        self.reg_button = QtWidgets.QPushButton(PyProgram)
        self.reg_button.setGeometry(QtCore.QRect(240, 310, 121, 41))
        self.reg_button.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.reg_button.setObjectName("reg_button")
        self.login_button_link = QtWidgets.QPushButton(PyProgram)
        self.login_button_link.setGeometry(QtCore.QRect(250, 360, 101, 23))
        self.login_button_link.setStyleSheet("")
        self.login_button_link.setObjectName("login_button_link")
        self.passwordr_label = QtWidgets.QLabel(PyProgram)
        self.passwordr_label.setGeometry(QtCore.QRect(190, 200, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.passwordr_label.setFont(font)
        self.passwordr_label.setStyleSheet("font-size:10pt;")
        self.passwordr_label.setObjectName("passwordr_label")
        self.passwordr = QtWidgets.QLineEdit(PyProgram)
        self.passwordr.setGeometry(QtCore.QRect(190, 220, 251, 31))
        self.passwordr.setObjectName("passwordr")
        self.email = QtWidgets.QLineEdit(PyProgram)
        self.email.setGeometry(QtCore.QRect(190, 100, 251, 31))
        self.email.setObjectName("email")
        self.email_label = QtWidgets.QLabel(PyProgram)
        self.email_label.setGeometry(QtCore.QRect(190, 80, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("font-size:10pt;")
        self.email_label.setObjectName("email_label")
        self.isteacher_checkbox = QtWidgets.QCheckBox(PyProgram)
        self.isteacher_checkbox.setGeometry(QtCore.QRect(230, 270, 121, 20))
        self.isteacher_checkbox.setObjectName("isteacher_checkbox")

        self.retranslateUi(PyProgram)
        QtCore.QMetaObject.connectSlotsByName(PyProgram)

    def retranslateUi(self, PyProgram):
        _translate = QtCore.QCoreApplication.translate
        PyProgram.setWindowTitle(_translate("PyProgram", "PyProgram"))
        self.login_label.setText(_translate("PyProgram", "Логін"))
        self.password_label.setText(_translate("PyProgram", "Пароль"))
        self.reg_button.setText(_translate("PyProgram", "Зареєструватися"))
        self.login_button_link.setText(_translate("PyProgram", "Увійти"))
        self.passwordr_label.setText(_translate("PyProgram", "Повторення паролю"))
        self.email_label.setText(_translate("PyProgram", "Email"))
        self.isteacher_checkbox.setText(_translate("PyProgram", "Я вчитель"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PyProgram = QtWidgets.QDialog()
    ui = Ui_PyProgram()
    ui.setupUi(PyProgram)
    PyProgram.show()
    sys.exit(app.exec_())
