# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Login.ui'
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
        self.login_label.setGeometry(QtCore.QRect(180, 70, 41, 21))
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
        self.login.setGeometry(QtCore.QRect(180, 90, 251, 31))
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(PyProgram)
        self.password.setGeometry(QtCore.QRect(180, 170, 251, 31))
        self.password.setObjectName("password")
        self.password_label = QtWidgets.QLabel(PyProgram)
        self.password_label.setGeometry(QtCore.QRect(180, 150, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("font-size:10pt;")
        self.password_label.setObjectName("password_label")
        self.login_button = QtWidgets.QPushButton(PyProgram)
        self.login_button.setGeometry(QtCore.QRect(240, 290, 121, 41))
        self.login_button.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.login_button.setObjectName("login_button")
        self.reg_button_link = QtWidgets.QPushButton(PyProgram)
        self.reg_button_link.setGeometry(QtCore.QRect(250, 350, 101, 23))
        self.reg_button_link.setStyleSheet("")
        self.reg_button_link.setObjectName("reg_button_link")
        self.frame = QtWidgets.QFrame(PyProgram)
        self.frame.setGeometry(QtCore.QRect(90, 60, 120, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.retranslateUi(PyProgram)
        QtCore.QMetaObject.connectSlotsByName(PyProgram)

    def retranslateUi(self, PyProgram):
        _translate = QtCore.QCoreApplication.translate
        PyProgram.setWindowTitle(_translate("PyProgram", "PyProgram"))
        self.login_label.setText(_translate("PyProgram", "Логін"))
        self.password_label.setText(_translate("PyProgram", "Пароль"))
        self.login_button.setText(_translate("PyProgram", "Увійти"))
        self.reg_button_link.setText(_translate("PyProgram", "Зареєструватися"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PyProgram = QtWidgets.QDialog()
    ui = Ui_PyProgram()
    ui.setupUi(PyProgram)
    PyProgram.show()
    sys.exit(app.exec_())