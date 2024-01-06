import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget


class Ui_PyProgram(object):
    def setupUi(self, PyProgram):
        PyProgram.setObjectName("PyProgram")
        PyProgram.resize(640, 380)
        self.line = QtWidgets.QLabel(PyProgram)
        self.line.setGeometry(QtCore.QRect(20, 50, 611, 16))
        self.line.setObjectName("line")
        self.models_button = QtWidgets.QPushButton(PyProgram)
        self.models_button.setEnabled(True)
        self.models_button.setGeometry(QtCore.QRect(90, 30, 75, 23))
        self.models_button.setObjectName("models_button")
        self.profile_button = QtWidgets.QPushButton(PyProgram)
        self.profile_button.setGeometry(QtCore.QRect(170, 30, 75, 23))
        self.profile_button.setObjectName("profile_button")
        self.materials_label = QtWidgets.QLabel(PyProgram)
        self.materials_label.setGeometry(QtCore.QRect(20, 30, 61, 21))
        self.materials_label.setStyleSheet(
            "background-color: rgb(177, 177, 177);")
        self.materials_label.setObjectName("materials_label")
        self.addmaterial_button = QtWidgets.QPushButton(PyProgram)
        self.addmaterial_button.setGeometry(QtCore.QRect(510, 70, 111, 31))
        self.addmaterial_button.setObjectName("addmaterial_button")
        self.material_border = QtWidgets.QPlainTextEdit(PyProgram)
        self.material_border.setGeometry(QtCore.QRect(20, 80, 391, 61))
        self.material_border.setObjectName("material_border")
        self.name_label = QtWidgets.QLabel(PyProgram)
        self.name_label.setGeometry(QtCore.QRect(30, 90, 47, 13))
        self.name_label.setObjectName("name_label")
        self.author_label = QtWidgets.QLabel(PyProgram)
        self.author_label.setGeometry(QtCore.QRect(30, 120, 47, 13))
        self.author_label.setObjectName("author_label")
        self.date_label = QtWidgets.QLabel(PyProgram)
        self.date_label.setGeometry(QtCore.QRect(320, 120, 81, 16))
        self.date_label.setObjectName("date_label")
        self.checkBox = QtWidgets.QCheckBox(PyProgram)
        self.checkBox.setGeometry(QtCore.QRect(150, 190, 191, 121))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(PyProgram)
        QtCore.QMetaObject.connectSlotsByName(PyProgram)

    def retranslateUi(self, PyProgram):
        _translate = QtCore.QCoreApplication.translate
        PyProgram.setWindowTitle(_translate("PyProgram", "Dialog"))
        self.line.setText(_translate(
            "PyProgram", "____________________________________________________________________________________________________"))
        self.models_button.setText(_translate("PyProgram", "Моделі"))
        self.profile_button.setText(_translate("PyProgram", "Профіль"))
        self.materials_label.setText(_translate("PyProgram", "  Матеріали"))
        self.addmaterial_button.setText(
            _translate("PyProgram", "Додати матеріал"))
        self.name_label.setText(_translate("PyProgram", "Назва"))
        self.author_label.setText(_translate("PyProgram", "Автор"))
        self.date_label.setText(_translate("PyProgram", "Дата додання"))


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.uiWindow = Ui_PyProgram()
        self.startUIWindow()

    def startUIWindow(self):
        self.uiWindow.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
