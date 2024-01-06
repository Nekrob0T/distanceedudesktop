# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 380)
        self.line = QtWidgets.QLabel(Dialog)
        self.line.setGeometry(QtCore.QRect(20, 50, 611, 16))
        self.line.setObjectName("line")
        self.models_button = QtWidgets.QPushButton(Dialog)
        self.models_button.setGeometry(QtCore.QRect(90, 30, 75, 23))
        self.models_button.setObjectName("models_button")
        self.materials_button = QtWidgets.QPushButton(Dialog)
        self.materials_button.setGeometry(QtCore.QRect(20, 30, 61, 23))
        self.materials_button.setObjectName("materials_button")
        self.profile_label = QtWidgets.QLabel(Dialog)
        self.profile_label.setGeometry(QtCore.QRect(170, 30, 61, 21))
        self.profile_label.setStyleSheet(
            "background-color: rgb(177, 177, 177);")
        self.profile_label.setObjectName("profile_label")
        self.exit_button = QtWidgets.QPushButton(Dialog)
        self.exit_button.setGeometry(QtCore.QRect(550, 70, 71, 31))
        self.exit_button.setObjectName("exit_button")
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setGeometry(QtCore.QRect(130, 80, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.teacherlink_label = QtWidgets.QLabel(Dialog)
        self.teacherlink_label.setGeometry(QtCore.QRect(130, 110, 351, 16))
        self.teacherlink_label.setObjectName("teacherlink_label")
        self.userlink_label = QtWidgets.QLabel(Dialog)
        self.userlink_label.setGeometry(QtCore.QRect(130, 130, 161, 16))
        self.userlink_label.setObjectName("userlink_label")
        self.userlink = QtWidgets.QLineEdit(Dialog)
        self.userlink.setGeometry(QtCore.QRect(280, 130, 151, 20))
        self.userlink.setObjectName("userlink")
        self.settings_button = QtWidgets.QPushButton(Dialog)
        self.settings_button.setGeometry(QtCore.QRect(440, 70, 101, 31))
        self.settings_button.setObjectName("settings_button")
        self.userlink_button = QtWidgets.QPushButton(Dialog)
        self.userlink_button.setGeometry(QtCore.QRect(440, 130, 81, 21))
        self.userlink_button.setObjectName("userlink_button")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 80, 91, 91))
        self.label.setStyleSheet("border-radius:45px;\n"
                                 "background:rgb(255,255,255,0%);\n"
                                 "border: 2px solid black;\n"
                                 "border-image: url(img/user/black.jpg) 0 stretch stretch;\n"
                                 "background-attachment: fixed;\n"
                                 "")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap("./img/user/avatar.jpg"))
        # self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.line.setText(_translate(
            "Dialog", "____________________________________________________________________________________________________"))
        self.models_button.setText(_translate("Dialog", "Моделі"))
        self.materials_button.setText(_translate("Dialog", "Матеріали"))
        self.profile_label.setText(_translate("Dialog", "   Профіль"))
        self.exit_button.setText(_translate("Dialog", "Вийти"))
        self.name_label.setText(_translate(
            "Dialog", "Прізвище Ім\'я по-Батькові"))
        self.teacherlink_label.setText(_translate(
            "Dialog", "Ваше посилання для приєднання: "))
        self.userlink_label.setText(_translate(
            "Dialog", "Уведіть посилання вчителя: "))
        self.settings_button.setText(_translate("Dialog", "Налаштування"))
        self.userlink_button.setText(_translate("Dialog", "Підтвердити"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())