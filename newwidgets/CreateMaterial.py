from PyQt5 import QtCore, QtGui, QtWidgets


class CreateMaterial(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 388)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(170, 120, 291, 31))
        self.name.setStyleSheet("border: 2px solid black;\n"
                                "border-radius: 15px;\n"
                                "padding-left: 5px;")
        self.name.setObjectName("name")
        self.description = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(170, 190, 291, 81))
        self.description.setStyleSheet("border: 2px solid black;\n"
                                       "border-radius: 10px;\n"
                                       "padding-left: 5px;")
        self.description.setReadOnly(False)
        self.description.setObjectName("description")
        self.creatematerial_button = QtWidgets.QPushButton(self.centralwidget)
        self.creatematerial_button.setGeometry(QtCore.QRect(260, 290, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.creatematerial_button.setFont(font)
        self.creatematerial_button.setStyleSheet(
            "background-color: rgb(53, 132, 228);")
        self.creatematerial_button.setObjectName("creatematerial_button")
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
        self.name.setPlaceholderText(_translate("MainWindow", "Назва"))
        self.description.setPlaceholderText(_translate("MainWindow", "Опис"))
        self.return_button.setText(_translate("MainWindow", "<"))
        self.creatematerial_button.setText(
            _translate("MainWindow", "Вкласти матеріал"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CreateMaterial()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
