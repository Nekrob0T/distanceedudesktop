# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newui/Material.ui'
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
        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(70, 70, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.description_label = QtWidgets.QLabel(Dialog)
        self.description_label.setGeometry(QtCore.QRect(70, 110, 491, 201))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.description_label.setFont(font)
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("description_label")
        self.date_label = QtWidgets.QLabel(Dialog)
        self.date_label.setGeometry(QtCore.QRect(70, 330, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.return_button = QtWidgets.QPushButton(Dialog)
        self.return_button.setGeometry(QtCore.QRect(10, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_label.setText(_translate("Dialog", "Закони Ньютона"))
        self.description_label.setText(_translate("Dialog", "Ознайомтесь з матеріалами та занотуйте основне gffjksdnsdfnsdkgbdkbfkasdnfmsanfm,dasnfm,nsadm,fbads,mbgasmdnbg.mdsbg.madsbg.adnbgmasbdg.adsbgasmdbngasm.bgasd"))
        self.date_label.setText(_translate("Dialog", "Віталій Кіндій | 18.03.2021"))
        self.return_button.setText(_translate("Dialog", "<"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())