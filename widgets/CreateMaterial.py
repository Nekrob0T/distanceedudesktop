# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/CreateMaterial.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class CreateMaterial(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 388)

        
        self.name = QtWidgets.QLineEdit(MainWindow)
        self.name.setGeometry(QtCore.QRect(170, 120, 291, 31))
        self.name.setStyleSheet("QLineEdit\n"
"{\n"
"border: 2px solid black;\n"
"border-radius: 15px;\n"
"}")
        self.name.setObjectName("name")
        self.name_label = QtWidgets.QLabel(MainWindow)
        self.name_label.setGeometry(QtCore.QRect(180, 100, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.description_label = QtWidgets.QLabel(MainWindow)
        self.description_label.setGeometry(QtCore.QRect(180, 170, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.description_label.setFont(font)
        self.description_label.setObjectName("description_label")
        self.description = QtWidgets.QLineEdit(MainWindow)
        self.description.setGeometry(QtCore.QRect(170, 190, 291, 31))
        self.description.setStyleSheet("QLineEdit\n"
"{\n"
"border: 2px solid black;\n"
"border-radius: 15px;\n"
"}")
        self.description.setObjectName("description")
        self.return_button = QtWidgets.QPushButton(MainWindow)
        self.return_button.setGeometry(QtCore.QRect(10, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")
        self.creatematerial_button = QtWidgets.QPushButton(MainWindow)
        self.creatematerial_button.setGeometry(QtCore.QRect(260, 250, 111, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.creatematerial_button.setFont(font)
        self.creatematerial_button.setStyleSheet("")
        self.creatematerial_button.setObjectName("creatematerial_button")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name_label.setText(_translate("MainWindow", "Назва"))
        self.description_label.setText(_translate("MainWindow", "Опис"))
        self.return_button.setText(_translate("MainWindow", "<"))
        self.creatematerial_button.setText(_translate("MainWindow", "Вкласти матеріал"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
