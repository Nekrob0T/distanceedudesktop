from PyQt5 import QtCore, QtGui, QtWidgets


class Models(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.line = QtWidgets.QLabel(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 40, 611, 16))
        self.line.setObjectName("line")
        self.models_label = QtWidgets.QLabel(self.centralwidget)
        self.models_label.setGeometry(QtCore.QRect(100, 20, 71, 21))
        self.models_label.setStyleSheet(
            "background-color: rgb(154, 153, 150);")
        self.models_label.setAlignment(QtCore.Qt.AlignCenter)
        self.models_label.setObjectName("models_label")
        self.profile_button = QtWidgets.QPushButton(self.centralwidget)
        self.profile_button.setGeometry(QtCore.QRect(180, 20, 75, 23))
        self.profile_button.setStyleSheet(
            "background-color: rgb(53, 132, 228);")
        self.profile_button.setObjectName("profile_button")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(20, 60, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.header.setFont(font)
        self.header.setStyleSheet("font-size: 16px")
        self.header.setObjectName("header")
        self.materials_button = QtWidgets.QPushButton(self.centralwidget)
        self.materials_button.setEnabled(True)
        self.materials_button.setGeometry(QtCore.QRect(20, 20, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.materials_button.setFont(font)
        self.materials_button.setStyleSheet(
            "background-color: rgb(53, 132, 228);")
        self.materials_button.setObjectName("materials_button")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 100, 601, 291))
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 599, 289))
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 70))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 70))
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.name_label = QtWidgets.QLabel(self.groupBox)
        self.name_label.setGeometry(QtCore.QRect(10, 10, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.groupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.addmodel_button = QtWidgets.QPushButton(self.centralwidget)
        self.addmodel_button.setGeometry(QtCore.QRect(510, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addmodel_button.setFont(font)
        self.addmodel_button.setStyleSheet(
            "background-color: rgb(53, 132, 228);")
        self.addmodel_button.setObjectName("addmodel_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.line.setText(_translate(
            "MainWindow", "____________________________________________________________________________________________________"))
        self.models_label.setText(_translate("MainWindow", "Моделі"))
        self.profile_button.setText(_translate("MainWindow", "Профіль"))
        self.header.setText(_translate("MainWindow", "Моделі"))
        self.materials_button.setText(_translate("MainWindow", "Матеріали"))
        self.name_label.setText(_translate("MainWindow", "Закон Ома"))
        self.addmodel_button.setText(_translate("MainWindow", "Додати модель"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Models()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
