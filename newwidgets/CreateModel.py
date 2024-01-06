from PyQt5 import QtCore, QtGui, QtWidgets


class CreateModel(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(170, 130, 291, 31))
        self.name.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                "border-radius:15px;\n"
                                "padding-left: 5px;\n"
                                "")
        self.name.setObjectName("name")
        self.link = QtWidgets.QLineEdit(self.centralwidget)
        self.link.setGeometry(QtCore.QRect(170, 200, 291, 31))
        self.link.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                "border-radius:15px;\n"
                                "padding-left: 5px;")
        self.link.setObjectName("link")
        self.createmodel_button = QtWidgets.QPushButton(self.centralwidget)
        self.createmodel_button.setGeometry(QtCore.QRect(260, 250, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.createmodel_button.setFont(font)
        self.createmodel_button.setStyleSheet(
            "background-color: rgb(53, 132, 228);")
        self.createmodel_button.setObjectName("createmodel_button")
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
        self.return_button.setText(_translate("MainWindow", "<"))
        self.createmodel_button.setText(
            _translate("MainWindow", "Додати модель"))
        self.name.setPlaceholderText(_translate("MainWindow", "Назва"))
        self.link.setPlaceholderText(_translate("MainWindow", "Посилання"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CreateModel()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
