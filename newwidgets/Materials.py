from PyQt5 import QtCore, QtGui, QtWidgets


class Materials(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 400)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.line = QtWidgets.QLabel(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 50, 611, 16))
        self.line.setObjectName("line")
        self.models_button = QtWidgets.QPushButton(self.centralwidget)
        self.models_button.setEnabled(True)
        self.models_button.setGeometry(QtCore.QRect(100, 30, 75, 23))
        self.models_button.setStyleSheet(
            "background-color: rgb(53, 132, 228);")
        self.models_button.setObjectName("models_button")
        self.profile_button = QtWidgets.QPushButton(self.centralwidget)
        self.profile_button.setGeometry(QtCore.QRect(180, 30, 75, 23))
        self.profile_button.setStyleSheet(
            "background-color: rgb(53, 132, 228);")
        self.profile_button.setObjectName("profile_button")
        self.materials_label = QtWidgets.QLabel(self.centralwidget)
        self.materials_label.setGeometry(QtCore.QRect(20, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.materials_label.setFont(font)
        self.materials_label.setStyleSheet(
            "background-color: rgb(154, 153, 150);")
        self.materials_label.setObjectName("materials_label")
        self.addmaterial_button = QtWidgets.QPushButton(self.centralwidget)
        self.addmaterial_button.setGeometry(QtCore.QRect(510, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addmaterial_button.setFont(font)
        self.addmaterial_button.setStyleSheet(
            "background-color: rgb(53, 132, 228);")
        self.addmaterial_button.setObjectName("addmaterial_button")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 110, 601, 271))
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 599, 269))
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
        self.name_label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.name_label.setObjectName("name_label")
        self.date_label = QtWidgets.QLabel(self.groupBox)
        self.date_label.setGeometry(QtCore.QRect(480, 50, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.author_label = QtWidgets.QLabel(self.groupBox)
        self.author_label.setGeometry(QtCore.QRect(10, 50, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.author_label.setFont(font)
        self.author_label.setObjectName("author_label")
        self.date_label.raise_()
        self.name_label.raise_()
        self.author_label.raise_()
        self.verticalLayout.addWidget(self.groupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(26, 73, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.header.setFont(font)
        self.header.setObjectName("header")
        self.scrollArea.raise_()
        self.line.raise_()
        self.models_button.raise_()
        self.profile_button.raise_()
        self.materials_label.raise_()
        self.addmaterial_button.raise_()
        self.header.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.line.setText(_translate(
            "MainWindow", "____________________________________________________________________________________________________"))
        self.models_button.setText(_translate("MainWindow", "Моделі"))
        self.profile_button.setText(_translate("MainWindow", "Профіль"))
        self.materials_label.setText(_translate("MainWindow", " Матеріали"))
        self.addmaterial_button.setText(
            _translate("MainWindow", "Додати матеріал"))
        self.name_label.setText(_translate("MainWindow", "Назва"))
        self.date_label.setText(_translate("MainWindow", "Дата додання"))
        self.author_label.setText(_translate("MainWindow", "Автор 1"))
        self.header.setText(_translate("MainWindow", "Матеріали"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Materials()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())