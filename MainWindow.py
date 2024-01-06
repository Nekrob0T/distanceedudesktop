import sys
import os
import string
import random
import hashlib
import easygui
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from mysql.connector import connect, Error


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.user = ()
        self.loginWindow = Login()
        self.regWindow = Register()
        self.materialsWindow = Materials()
        self.materialWindow = Material()
        self.creatematerialWindow = CreateMaterial()
        self.modelsWindow = Models()
        self.modelWindow = Model()
        self.createmodelWindow = CreateModel()
        self.ohmmodelWindow = Ohmmodel()
        self.profileWindow = Profile()
        self.settingsWindow = Settings()

        self.startUILogin()

    def startUIRegister(self):
        self.regWindow.setupUi(self)
        self.regWindow.login_button_link.clicked.connect(self.startUILogin)
        self.show()

    def startUILogin(self, exit=False):
        if exit:
            self.user = ()
        self.loginWindow.setupUi(self)
        self.loginWindow.reg_button_link.clicked.connect(self.startUIRegister)
        self.show()

    def startUIMaterials(self):
        self.materialsWindow.setupUi(self)
        self.materialsWindow.models_button.clicked.connect(self.startUIModels)
        self.materialsWindow.profile_button.clicked.connect(
            self.startUIProfile)

        if ui.user[2]:
            self.materialsWindow.addmaterial_button.clicked.connect(
                self.startUICreateMaterial)

        self.show()

    def startUIMaterial(self, id):
        self.materialWindow.setupUi(self, id)
        self.materialWindow.return_button.clicked.connect(
            self.startUIMaterials)
        self.show()

    def startUICreateMaterial(self):
        self.creatematerialWindow.setupUi(self)
        self.creatematerialWindow.return_button.clicked.connect(
            self.startUIMaterials)
        self.show()

    def startUIModels(self):
        self.modelsWindow.setupUi(self)
        self.modelsWindow.materials_button.clicked.connect(
            self.startUIMaterials)
        self.modelsWindow.profile_button.clicked.connect(
            self.startUIProfile)

        if ui.user[2]:
            self.modelsWindow.addmodel_button.clicked.connect(
                self.startUICreateModel)

        self.show()

    def startUIModel(self, id):
        if int(id) == 1:
            self.ohmmodelWindow.setupUi(self)
            self.ohmmodelWindow.return_button.clicked.connect(
                self.startUIModels)
            self.show()
        else:
            self.modelWindow.setupUi(self, id)
            self.modelWindow.return_button.clicked.connect(
                self.startUIModels)
            self.show()

    def startUICreateModel(self):
        self.createmodelWindow.setupUi(self)
        self.createmodelWindow.return_button.clicked.connect(
            self.startUIModels)

    def startUIProfile(self):
        self.profileWindow.setupUi(self)
        self.profileWindow.models_button.clicked.connect(self.startUIModels)
        self.profileWindow.materials_button.clicked.connect(
            self.startUIMaterials)
        self.profileWindow.settings_button.clicked.connect(
            self.startUISettings)
        self.profileWindow.exit_button.clicked.connect(
            lambda: self.startUILogin(True))
        self.show()

    def startUISettings(self):
        self.settingsWindow.setupUi(self)
        self.settingsWindow.return_button.clicked.connect(
            self.startUIProfile)
        self.show()


class Login(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("font: 8pt \"Comic Sans MS\";")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(180, 100, 251, 31))
        self.login.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                 "border-radius:15px;\n"
                                 "padding-left: 5px;\n"
                                 "")
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(180, 180, 251, 31))
        self.password.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                    "border-radius:15px;\n"
                                    "padding-left: 5px;")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(240, 290, 121, 41))
        self.login_button.setStyleSheet("background-color: rgb(103, 226, 60);\n"
                                        "border: 0.5px solid rgb(61, 56, 70);\n"
                                        "border-radius:10px;\n"
                                        "")
        self.login_button.setObjectName("login_button")
        self.login_button.clicked.connect(self.checkForm)
        self.reg_button_link = QtWidgets.QPushButton(self.centralwidget)
        self.reg_button_link.setGeometry(QtCore.QRect(250, 350, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.reg_button_link.setFont(font)
        self.reg_button_link.setStyleSheet("color: rgb(0,0,0);\n"
                                           "background-color: rgb(28, 113, 216);\n"
                                           "border: 0.5px solid rgb(61, 56, 70);\n"
                                           "border-radius:10px;\n"
                                           "")
        self.reg_button_link.setObjectName("reg_button_link")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login.setPlaceholderText(_translate("MainWindow", "Логін"))
        self.login_button.setText(_translate("MainWindow", "Увійти"))
        self.reg_button_link.setText(
            _translate("MainWindow", "Зареєструватися"))
        self.password.setPlaceholderText(_translate("MainWindow", "Пароль"))

    def checkForm(self):
        if self.login.text() == "" or self.password.text() == "":
            QtWidgets.QMessageBox.about(
                self, "Помилка", "Не всі поля заповнені")
        else:
            self.loginF()

    def loginF(self):
        try:
            with connect(
                host="localhost",
                user="root",
                password="",
                database="pyfuture",
            ) as connection:
                get_value_table_query = "SELECT * FROM users WHERE login = '{login}'".format(
                    login=self.login.text())
                with connection.cursor(buffered=True) as cursor:
                    cursor.execute(get_value_table_query)
                    temp = cursor.fetchone()
                    if temp == None:
                        QtWidgets.QMessageBox.about(
                            self, "Помилка", "Користувача з таким логіном не знайдено")
                    elif hashlib.md5(self.password.text().encode('utf8')).hexdigest() != temp[6]:
                        QtWidgets.QMessageBox.about(
                            self, "Помилка", "Неправильний пароль")
                    else:
                        ui.user = temp
                        ui.startUIMaterials()

        except Error as e:
            print(e)


class Register(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("font: 8pt \"Comic Sans MS\";")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(190, 40, 251, 31))
        self.login.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                 "border-radius:15px;\n"
                                 "padding-left: 5px;")
        self.login.setObjectName("login")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(190, 100, 251, 31))
        self.email.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                 "border-radius:15px;\n"
                                 "padding-left: 5px;")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(190, 160, 251, 31))
        self.password.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                    "border-radius:15px;\n"
                                    "padding-left: 5px;")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordr = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordr.setGeometry(QtCore.QRect(190, 220, 251, 31))
        self.passwordr.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                     "border-radius:15px;\n"
                                     "padding-left: 5px;")
        self.passwordr.setObjectName("passwordr")
        self.passwordr.setEchoMode(QtWidgets.QLineEdit.Password)
        self.isteacher_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.isteacher_checkbox.setGeometry(QtCore.QRect(260, 270, 91, 20))
        self.isteacher_checkbox.setObjectName("isteacher_checkbox")
        self.reg_button = QtWidgets.QPushButton(self.centralwidget)
        self.reg_button.setGeometry(QtCore.QRect(240, 310, 121, 41))
        self.reg_button.setStyleSheet("background-color: rgb(103, 226, 60);\n"
                                      "border: 0.5px solid rgb(61, 56, 70);\n"
                                      "border-radius:10px;\n")
        self.reg_button.setObjectName("reg_button")
        self.reg_button.clicked.connect(self.checkForm)
        self.login_button_link = QtWidgets.QPushButton(self.centralwidget)
        self.login_button_link.setGeometry(QtCore.QRect(250, 360, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.login_button_link.setFont(font)
        self.login_button_link.setStyleSheet("color: rgb(0,0,0);\n"
                                             "background-color: rgb(28, 113, 216);\n"
                                             "border: 0.5px solid rgb(61, 56, 70);\n"
                                             "border-radius:10px;\n")
        self.login_button_link.setObjectName("login_button_link")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_button_link.setText(_translate("MainWindow", "Увійти"))
        self.login.setPlaceholderText(_translate("MainWindow", "Логін"))
        self.email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.password.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.passwordr.setPlaceholderText(
            _translate("MainWindow", "Повторення паролю"))
        self.reg_button.setText(_translate("MainWindow", "Зареєструватися"))
        self.isteacher_checkbox.setText(_translate("MainWindow", "Я вчитель"))

    def checkForm(self):
        if self.login.text() == "" or self.email.text() == "" or self.password.text() == "":
            QtWidgets.QMessageBox.about(
                self, "Помилка", "Не всі поля заповнені")
        elif self.password.text() != self.passwordr.text():
            QtWidgets.QMessageBox.about(
                self, "Помилка", "Паролі не співпадають")
        else:
            self.register()

    def register(self):
        try:
            with connect(
                host="localhost",
                user="root",
                password="",
                database="pyfuture",
            ) as connection:
                insert_value_table_query = ""
                password = self.password.text()
                hashed_password = hashlib.md5(
                    password.encode('utf8')).hexdigest()

                if self.isteacher_checkbox.isChecked():
                    letters = string.ascii_lowercase
                    link = ''.join(random.choice(letters) for i in range(10))
                    insert_value_table_query = """
                        INSERT INTO users (login, teacher, teacherlink, otherid, email, password, avatar, name, surname, pobat)
                        VALUES ('{login}', '{teacher}', '{link}', '', '{email}', '{password}', 'avatar.jpg',
                                "Ім'я", "Прізвище", "По-батькові")
                    """.format(login=self.login.text(), teacher=1, link=link, email=self.email.text(), password=hashed_password)
                else:
                    insert_value_table_query = """
                        INSERT INTO users (login, teacher, teacherlink, otherid, email, password, avatar, name, surname, pobat)
                        VALUES ('{login}', '{teacher}', '', '', '{email}', '{password}', 'avatar.jpg',
                                "Ім'я", "Прізвище", "По-батькові")
                    """.format(login=self.login.text(), teacher=0, email=self.email.text(), password=hashed_password)

                with connection.cursor() as cursor:
                    cursor.execute(insert_value_table_query)
                    get_value_table_query = "SELECT * FROM users WHERE login = '{login}'".format(
                        login=self.login.text())
                    print(self.login.text())
                    connection.commit()
                    cursor.execute(get_value_table_query)
                    ui.user = cursor.fetchone()
                    ui.startUIMaterials()

        except Error as e:
            print(e)


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

        if ui.user[2]:
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
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(26, 73, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.header.setFont(font)
        self.header.setStyleSheet("font-size: 16px")
        self.header.setObjectName("header")
        self.scrollArea.raise_()
        self.line.raise_()
        self.models_button.raise_()
        self.profile_button.raise_()
        self.materials_label.raise_()

        if ui.user[2]:
            self.addmaterial_button.raise_()

        self.header.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.loadMaterials()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.line.setText(_translate(
            "MainWindow", "____________________________________________________________________________________________________"))
        self.models_button.setText(_translate("MainWindow", "Моделі"))
        self.profile_button.setText(_translate("MainWindow", "Профіль"))
        self.materials_label.setText(_translate("MainWindow", "  Матеріали"))

        if ui.user[2]:
            self.addmaterial_button.setText(
                _translate("MainWindow", "Додати матеріал"))

        self.header.setText(_translate("MainWindow", "Матеріали"))

    def loadMaterials(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            with connect(
                host="localhost",
                user="root",
                password="",
                database="pyfuture",
            ) as connection:
                get_materials_table_query = ""

                # check if the user is a teacher
                if ui.user[2]:
                    get_materials_table_query = "SELECT * FROM materials WHERE teacherid = '{id}'".format(
                        id=ui.user[0])
                else:
                    tempStr = ui.user[4]
                    get_materials_table_query = "SELECT * FROM materials WHERE teacherid IN ({tin})".format(
                        tin=tempStr[:len(tempStr)-2])

                with connection.cursor() as cursor:
                    cursor.execute(get_materials_table_query)
                    temp = cursor.fetchall()

                    for row in temp:
                        self.groupBox = QtWidgets.QPushButton(
                            self.scrollAreaWidgetContents)
                        self.groupBox.setMinimumSize(QtCore.QSize(0, 70))
                        self.groupBox.setMaximumSize(
                            QtCore.QSize(16777215, 70))
                        self.groupBox.setStyleSheet(
                            "background-color: rgb(255, 255, 255);")
                        self.groupBox.setObjectName("groupBox_" + str(row[0]))
                        self.groupBox.clicked.connect(self.load)
                        self.name_label = QtWidgets.QLabel(self.groupBox)
                        self.name_label.setGeometry(
                            QtCore.QRect(10, 10, 350, 40))
                        self.name_label.setObjectName("name_label")
                        self.date_label = QtWidgets.QLabel(self.groupBox)
                        self.date_label.setGeometry(
                            QtCore.QRect(480, 50, 81, 16))
                        self.date_label.setObjectName("date_label")
                        self.author_label = QtWidgets.QLabel(self.groupBox)
                        self.author_label.setGeometry(
                            QtCore.QRect(10, 50, 150, 13))
                        self.author_label.setObjectName("author_label")
                        self.date_label.raise_()
                        self.name_label.raise_()
                        self.author_label.raise_()
                        self.name_label.setText(
                            _translate("MainWindow", row[2]))
                        self.date_label.setText(
                            _translate("MainWindow", row[5]))
                        self.author_label.setText(
                            _translate("MainWindow", row[4]))
                        self.verticalLayout.addWidget(self.groupBox)

        except Error as e:
            print(e)

    def load(self):
        temp = self.sender().objectName()
        ui.startUIMaterial(temp[temp.index("_")+1:])


class Material(QtWidgets.QWidget):
    def setupUi(self, MainWindow, id):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 400)

        self.id = id
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(70, 70, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.description_label = QtWidgets.QLabel(self.centralwidget)
        self.description_label.setGeometry(QtCore.QRect(70, 120, 491, 201))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.description_label.setFont(font)
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("description_label")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(70, 330, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(10, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.loadMaterial()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.return_button.setText(_translate("MainWindow", "<"))

    def loadMaterial(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            with connect(
                host="localhost",
                user="root",
                password="",
                database="pyfuture",
            ) as connection:
                get_material_table_query = "SELECT * FROM materials WHERE id = '{id}'".format(
                    id=self.id)

                with connection.cursor(buffered=True) as cursor:
                    cursor.execute(get_material_table_query)
                    temp = cursor.fetchone()

                    self.title_label.setText(_translate(
                        "MainWindow", str(temp[2])))
                    self.description_label.setText(_translate(
                        "MainWindow", str(temp[3])))
                    self.date_label.setText(_translate(
                        "MainWindow", str(temp[4]) + " | " + str(temp[5])))

        except Error as e:
            print(e)


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
        self.creatematerial_button.clicked.connect(self.checkForm)
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

    def checkForm(self, MainWindow):
        if self.name.text() == "" or self.description.toPlainText() == "":
            QtWidgets.QMessageBox.about(
                self, "Помилка", "Не всі поля заповнені")
        else:
            self.create()

    def create(self):
        try:
            with connect(
                host="localhost",
                user="root",
                password="",
                database="pyfuture",
            ) as connection:
                insert_material_table_query = """
                    INSERT INTO materials (teacherid, title, description, author, date)
                    VALUES ('{teacherid}', '{title}',
                            '{description}', "{author}", '{date}')
                """.format(teacherid=ui.user[0], title=self.name.text(), description=self.description.toPlainText(), author=str(ui.user[8] + " " + ui.user[9]), date=date.today().strftime("%d.%m.%Y"))
                with connection.cursor() as cursor:
                    cursor.execute(insert_material_table_query)
                    connection.commit()
                    ui.startUIMaterials()

        except Error as e:
            print(e)


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
        self.header.setStyleSheet("font-size: 16px")
        self.header.setFont(font)
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
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        if ui.user[2]:
            self.addmodel_button = QtWidgets.QPushButton(self.centralwidget)
            self.addmodel_button.setGeometry(QtCore.QRect(510, 60, 111, 31))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.addmodel_button.setFont(font)
            self.addmodel_button.setStyleSheet(
                "background-color: rgb(53, 132, 228);")
            self.addmodel_button.setObjectName("addmodel_button")

        MainWindow.setCentralWidget(self.centralwidget)

        self.loadMaterials()

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

        if ui.user[2]:
            self.addmodel_button.setText(
                _translate("MainWindow", "Додати модель"))

    def loadMaterials(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            with connect(
                host="localhost",
                user="root",
                password="",
                database="pyfuture",
            ) as connection:
                get_experiments_table_query = "SELECT * FROM experiments"

                with connection.cursor() as cursor:
                    cursor.execute(get_experiments_table_query)
                    temp = cursor.fetchall()

                    for row in temp:
                        self.groupBox = QtWidgets.QPushButton(
                            self.scrollAreaWidgetContents)
                        self.groupBox.setMinimumSize(QtCore.QSize(0, 70))
                        self.groupBox.setMaximumSize(
                            QtCore.QSize(16777215, 70))
                        self.groupBox.setStyleSheet(
                            "background-color: rgb(255, 255, 255);")
                        self.groupBox.setObjectName("model_" + str(row[0]))
                        self.groupBox.clicked.connect(self.load)
                        self.name_label = QtWidgets.QLabel(self.groupBox)
                        self.name_label.setGeometry(
                            QtCore.QRect(10, 10, 561, 51))
                        self.name_label.setStyleSheet("font-size: 16px")
                        self.name_label.setObjectName("name_label")
                        self.name_label.setText(
                            _translate("MainWindow", row[1]))
                        self.verticalLayout.addWidget(self.groupBox)

        except Error as e:
            print(e)

    def load(self):
        temp = self.sender().objectName()
        ui.startUIModel(temp[temp.index("_")+1:])


class Model(QtWidgets.QWidget):
    def setupUi(self, MainWindow, id):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 400)

        self.link = ""
        try:
            with connect(
                host="localhost",
                user="root",
                password="",
                database="pyfuture",
            ) as connection:
                get_experiment_table_query = "SELECT * FROM experiments WHERE id = '{id}'".format(
                    id=id)

                with connection.cursor(buffered=True) as cursor:
                    cursor.execute(get_experiment_table_query)
                    temp = cursor.fetchone()
                    self.link = temp[2]

        except Error as e:
            print(e)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(20, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")
        self.textBrowser = QtWebEngineWidgets.QWebEngineView(
            self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 60, 601, 321))
        self.textBrowser.load(QtCore.QUrl(self.link))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.return_button.setText(_translate("MainWindow", "<"))


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
        self.createmodel_button.clicked.connect(self.checkForm)
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

    def checkForm(self):
        if self.name.text() == "" or self.link.text() == "":
            QtWidgets.QMessageBox.about(
                self, "Помилка", "Не всі поля заповнені")
        else:
            self.createModel()

    def createModel(self):
        try:
            with connect(
                host="localhost",
                user="root",
                password="",
                database="pyfuture",
            ) as connection:
                add_model_table_query = "INSERT INTO experiments (title, link) VALUES ('{name}', '{link}')".format(
                    name=self.name.text(), link=self.link.text())
                with connection.cursor() as cursor:
                    cursor.execute(add_model_table_query)
                    connection.commit()
                    ui.startUIModels()

        except Error as e:
            print(e)


class Profile(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.line = QtWidgets.QLabel(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 50, 611, 16))
        self.line.setObjectName("line")
        self.materials_button = QtWidgets.QPushButton(self.centralwidget)
        self.materials_button.setGeometry(QtCore.QRect(20, 30, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.materials_button.setFont(font)
        self.materials_button.setStyleSheet(
            "background-color: rgb(53, 132, 228);")
        self.materials_button.setObjectName("materials_button")
        self.models_button = QtWidgets.QPushButton(self.centralwidget)
        self.models_button.setGeometry(QtCore.QRect(100, 30, 75, 23))
        self.models_button.setStyleSheet(
            "background-color: rgb(53, 132, 228);")
        self.models_button.setObjectName("models_button")
        self.profile_label = QtWidgets.QLabel(self.centralwidget)
        self.profile_label.setGeometry(QtCore.QRect(187, 31, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.profile_label.setFont(font)
        self.profile_label.setStyleSheet(
            "background-color: rgb(154, 153, 150);")
        self.profile_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.profile_label.setObjectName("profile_label")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(550, 70, 71, 31))
        self.exit_button.setStyleSheet("background-color: rgb(224, 27, 36);")
        self.exit_button.setObjectName("exit_button")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(130, 85, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(440, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.settings_button.setFont(font)
        self.settings_button.setStyleSheet(
            "background-color: rgb(53, 132, 228);")
        self.settings_button.setObjectName("settings_button")
        self.icon = QtWidgets.QLabel(self.centralwidget)
        self.icon.setGeometry(QtCore.QRect(20, 80, 91, 91))
        self.icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.icon.setText("")
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")

        if ui.user[2]:
            self.teacherlink_label = QtWidgets.QLabel(self.centralwidget)
            self.teacherlink_label.setGeometry(QtCore.QRect(130, 112, 351, 16))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.teacherlink_label.setFont(font)
            self.teacherlink_label.setObjectName("teacherlink_label")
        else:
            self.userlink_label = QtWidgets.QLabel(self.centralwidget)
            self.userlink_label.setGeometry(QtCore.QRect(130, 112, 171, 16))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.userlink_label.setFont(font)
            self.userlink_label.setObjectName("userlink_label")
            self.userlink = QtWidgets.QLineEdit(self.centralwidget)
            self.userlink.setGeometry(QtCore.QRect(300, 112, 151, 20))
            self.userlink.setObjectName("userlink")
            self.userlink_button = QtWidgets.QPushButton(self.centralwidget)
            self.userlink_button.setGeometry(QtCore.QRect(460, 112, 81, 21))
            font = QtGui.QFont()
            font.setPointSize(9)
            self.userlink_button.setFont(font)
            self.userlink_button.setStyleSheet(
                "background-color: rgb(103, 226, 60);")
            self.userlink_button.setObjectName("userlink_button")
            self.userlink_button.clicked.connect(
                lambda: self.addTeacher(self.userlink.text()))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.line.setText(_translate(
            "MainWindow", "____________________________________________________________________________________________________"))
        self.models_button.setText(_translate("MainWindow", "Моделі"))
        self.icon.setStyleSheet("border-radius:45px;\n"
                                "background:rgb(255,255,255,0%);\n"
                                "border: 2px solid black;\n"
                                "border-image: url(img/user/" +
                                str(ui.user[7])+") 0 stretch stretch;\n"
                                "background-attachment: fixed;\n"
                                "")
        self.materials_button.setText(_translate("MainWindow", "Матеріали"))
        self.profile_label.setText(_translate("MainWindow", "   Профіль"))
        self.settings_button.setText(_translate("MainWindow", "Налаштування"))
        self.exit_button.setText(_translate("MainWindow", "Вийти"))
        self.name_label.setText(_translate(
            "MainWindow", str(ui.user[9] + " " + ui.user[8] + " " + ui.user[10])))
        if ui.user[2]:
            self.teacherlink_label.setText(_translate(
                "MainWindow", "Ваше посилання для приєднання: " + str(ui.user[3])))
        else:
            self.userlink_label.setText(_translate(
                "MainWindow", "Уведіть посилання вчителя: "))
            self.userlink_button.setText(
                _translate("MainWindow", "Підтвердити"))

    def addTeacher(self, link):
        try:
            with connect(
                host="localhost",
                user="root",
                password="",
                database="pyfuture",
            ) as connection:
                find_teacher_table_query = "SELECT * FROM users WHERE teacherlink = '{teacherlink}'".format(
                    teacherlink=link)
                with connection.cursor(buffered=True) as cursor:
                    cursor.execute(find_teacher_table_query)
                    connection.commit()
                    temp = cursor.fetchone()

                    if temp == None:
                        QtWidgets.QMessageBox.about(
                            self, "Помилка", "Учителя з таким кодом не знайдено")
                    else:
                        tempStr = str(ui.user[4]) + str(temp[0]) + ", "
                        update_otherid_table_query = "UPDATE users SET otherid = '{otherid}' WHERE id = '{userid}'".format(
                            otherid=tempStr, userid=ui.user[0])
                        cursor.execute(update_otherid_table_query)
                        connection.commit()
                        get_value_table_query = "SELECT * FROM users WHERE id = '{id}'".format(
                            id=ui.user[0])
                        cursor.execute(get_value_table_query)
                        connection.commit()
                        ui.user = cursor.fetchone()
        except Error as e:
            print(e)


class Settings(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 360)

        self.file = ""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.icon_button = QtWidgets.QPushButton(self.centralwidget)
        self.icon_button.setGeometry(QtCore.QRect(270, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.icon_button.setFont(font)
        self.icon_button.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.icon_button.setObjectName("icon_button")
        self.icon_button.clicked.connect(self.openFile)
        self.surname = QtWidgets.QLineEdit(self.centralwidget)
        self.surname.setGeometry(QtCore.QRect(140, 130, 171, 31))
        self.surname.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                   "border-radius:15px;\n"
                                   "padding-left: 5px;\n"
                                   "")
        self.surname.setObjectName("surname")
        self.surname.setText(ui.user[9])
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(330, 130, 171, 31))
        self.name.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                "border-radius:15px;\n"
                                "padding-left: 5px;")
        self.name.setObjectName("name")
        self.name.setText(ui.user[8])
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(330, 210, 171, 31))
        self.email.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                 "border-radius:15px;\n"
                                 "padding-left: 5px;")
        self.email.setObjectName("email")
        self.email.setText(ui.user[5])
        self.pobat = QtWidgets.QLineEdit(self.centralwidget)
        self.pobat.setGeometry(QtCore.QRect(140, 210, 171, 31))
        self.pobat.setStyleSheet("border: 2px solid rgb(61, 56, 70);\n"
                                 "border-radius:15px;\n"
                                 "padding-left: 5px;")
        self.pobat.setObjectName("pobat")
        self.pobat.setText(ui.user[10])
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(270, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("background-color: rgb(103, 226, 60);")
        self.save_button.setObjectName("save_button")
        self.save_button.clicked.connect(self.checkForm)
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
        self.icon_button.setText(_translate("MainWindow", "Аватар"))
        self.save_button.setText(_translate("MainWindow", "Зберегти"))
        self.return_button.setText(_translate("MainWindow", "<"))
        self.surname.setPlaceholderText(_translate("MainWindow", "Прізвище"))
        self.name.setPlaceholderText(_translate("MainWindow", "Ім\'я"))
        self.email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.pobat.setPlaceholderText(_translate("MainWindow", "По-батькові"))

    def checkForm(self):
        if self.surname.text() == "" or self.name.text() == "" or self.pobat.text() == "" or self.email.text() == "":
            QtWidgets.QMessageBox.about(
                self, "Помилка", "Не всі поля заповнені")
        else:
            self.updateSettings()

    def openFile(self):
        self.file = easygui.fileopenbox(filetypes=["*.png", "*.jpg", "*.jpeg"])

    def updateSettings(self):
        try:
            with connect(
                host="localhost",
                user="root",
                password="",
                database="pyfuture",
            ) as connection:
                if self.file != "":
                    ind = self.file[::-1].index("\\")
                    fileName = self.file[len(str(self.file))-ind:]
                    update_user_table_query = "UPDATE users SET name = '{name}', surname = '{surname}', pobat = '{pobat}', email = '{email}', avatar = '{avatar}'  WHERE id = '{userid}'".format(
                        name=self.name.text(), surname=self.surname.text(), pobat=self.pobat.text(), email=self.email.text(), avatar=fileName, userid=ui.user[0])
                    os.replace(self.file,
                               "./img/user/"+fileName)
                else:
                    update_user_table_query = "UPDATE users SET name = '{name}', surname = '{surname}', pobat = '{pobat}', email = '{email}'  WHERE id = '{userid}'".format(
                        name=self.name.text(), surname=self.surname.text(), pobat=self.pobat.text(), email=self.email.text(), userid=ui.user[0])

                with connection.cursor(buffered=True) as cursor:
                    cursor.execute(update_user_table_query)
                    connection.commit()
                    get_value_table_query = "SELECT * FROM users WHERE id = '{id}'".format(
                        id=ui.user[0])
                    cursor.execute(get_value_table_query)
                    connection.commit()
                    ui.user = cursor.fetchone()
                    ui.startUIProfile()
        except Error as e:
            print(e)


class Ohmmodel(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: #fff;")
        self.obvodka_textbrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.obvodka_textbrowser.setGeometry(QtCore.QRect(180, 90, 281, 111))
        self.obvodka_textbrowser.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                               "border: 2px solid black;\n"
                                               "border-radius: 15px;\n")
        self.obvodka_textbrowser.setObjectName("obvodka_textbrowser")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(210, 160, 221, 91))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.cylindr_label = QtWidgets.QLabel(self.groupBox)
        self.cylindr_label.setGeometry(QtCore.QRect(0, 0, 221, 91))
        self.cylindr_label.setToolTipDuration(0)
        self.cylindr_label.setStyleSheet("")
        self.cylindr_label.setText("")
        self.cylindr_label.setPixmap(
            QtGui.QPixmap("./img/exp/cylinder.png"))
        self.cylindr_label.setScaledContents(True)
        self.cylindr_label.setObjectName("cylindr_label")

        self.amper_label = QtWidgets.QLabel(self.centralwidget)
        self.amper_label.setGeometry(QtCore.QRect(290, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.amper_label.setFont(font)
        self.amper_label.setObjectName("amper_label")
        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(20, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")
        self.obvodkares_textbrowser = QtWidgets.QTextBrowser(
            self.centralwidget)
        self.obvodkares_textbrowser.setGeometry(QtCore.QRect(50, 260, 141, 91))
        self.obvodkares_textbrowser.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                                  "border: 1px solid black;\n"
                                                  "border-radius: 15px;\n")
        self.obvodkares_textbrowser.setObjectName("obvodkares_textbrowser")
        self.res_label = QtWidgets.QLabel(self.centralwidget)
        self.res_label.setGeometry(QtCore.QRect(110, 270, 47, 13))
        self.res_label.setObjectName("res_label")
        self.vimirres_label = QtWidgets.QLabel(self.centralwidget)
        self.vimirres_label.setGeometry(QtCore.QRect(70, 290, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vimirres_label.setFont(font)
        self.vimirres_label.setObjectName("vimirres_label")
        self.oneres_label = QtWidgets.QLabel(self.centralwidget)
        self.oneres_label.setGeometry(QtCore.QRect(70, 330, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.oneres_label.setFont(font)
        self.oneres_label.setObjectName("oneres_label")
        self.stores_label = QtWidgets.QLabel(self.centralwidget)
        self.stores_label.setGeometry(QtCore.QRect(150, 330, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stores_label.setFont(font)
        self.stores_label.setObjectName("stores_label")
        self.tenvolt_label = QtWidgets.QLabel(self.centralwidget)
        self.tenvolt_label.setGeometry(QtCore.QRect(490, 330, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tenvolt_label.setFont(font)
        self.tenvolt_label.setObjectName("tenvolt_label")
        self.obvodkavolt_textbrowser = QtWidgets.QTextBrowser(
            self.centralwidget)
        self.obvodkavolt_textbrowser.setGeometry(
            QtCore.QRect(470, 260, 141, 91))
        self.obvodkavolt_textbrowser.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                                   "border: 1px solid black;\n"
                                                   "border-radius: 15px;\n")
        self.obvodkavolt_textbrowser.setObjectName("obvodkavolt_textbrowser")
        self.vimirvolt_label = QtWidgets.QLabel(self.centralwidget)
        self.vimirvolt_label.setGeometry(QtCore.QRect(490, 290, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vimirvolt_label.setFont(font)
        self.vimirvolt_label.setObjectName("vimirvolt_label")
        self.volt_label = QtWidgets.QLabel(self.centralwidget)
        self.volt_label.setGeometry(QtCore.QRect(520, 270, 51, 16))
        self.volt_label.setObjectName("volt_label")
        self.tisyachavolt_label = QtWidgets.QLabel(self.centralwidget)
        self.tisyachavolt_label.setGeometry(QtCore.QRect(570, 330, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tisyachavolt_label.setFont(font)
        self.tisyachavolt_label.setObjectName("tisyachavolt_label")
        self.res_slider = QtWidgets.QSlider(self.centralwidget)
        self.res_slider.setGeometry(QtCore.QRect(60, 310, 121, 22))
        self.res_slider.setMinimum(1)
        self.res_slider.setMaximum(100)
        self.res_slider.setValue(50)
        self.res_slider.setOrientation(QtCore.Qt.Horizontal)
        self.res_slider.setInvertedAppearance(False)
        self.res_slider.setInvertedControls(False)
        self.res_slider.setObjectName("res_slider")
        self.res_slider.valueChanged.connect(self.resValueChanged)
        self.res_slider.sliderReleased.connect(self.generatePoints)
        self.volt_slider = QtWidgets.QSlider(self.centralwidget)
        self.volt_slider.setGeometry(QtCore.QRect(480, 310, 121, 22))
        self.volt_slider.setMinimum(10)
        self.volt_slider.setMaximum(1000)
        self.volt_slider.setValue(500)
        self.volt_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volt_slider.setInvertedAppearance(False)
        self.volt_slider.setInvertedControls(False)
        self.volt_slider.setObjectName("volt_slider")
        self.volt_slider.valueChanged.connect(self.voltValueChanged)
        MainWindow.setCentralWidget(self.centralwidget)

        self.voltValueChanged()
        self.resValueChanged()
        self.generatePoints()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.amper_label.setText(_translate("MainWindow", "I = 10 A"))
        self.return_button.setText(_translate("MainWindow", "<"))
        self.res_label.setText(_translate("MainWindow", "Опір"))
        self.vimirres_label.setText(_translate("MainWindow", "50"))
        self.oneres_label.setText(_translate("MainWindow", "1"))
        self.stores_label.setText(_translate("MainWindow", "100"))
        self.tenvolt_label.setText(_translate("MainWindow", "10"))
        self.vimirvolt_label.setText(_translate(
            "MainWindow", str(self.volt_slider.value())))
        self.volt_label.setText(_translate("MainWindow", "Вольтаж"))
        self.tisyachavolt_label.setText(_translate("MainWindow", "1000"))

    def voltValueChanged(self):
        _translate = QtCore.QCoreApplication.translate
        self.vimirvolt_label.setText(_translate(
            "MainWindow", str(self.volt_slider.value())))
        amper = round(self.volt_slider.value() / self.res_slider.value(), 2)
        self.amper_label.setText(_translate(
            "MainWindow", "I = " + str(amper) + " A"))

    def resValueChanged(self):
        _translate = QtCore.QCoreApplication.translate
        self.vimirres_label.setText(_translate(
            "MainWindow", str(self.res_slider.value())))
        amper = round(self.volt_slider.value() / self.res_slider.value(), 2)
        self.amper_label.setText(_translate(
            "MainWindow", "I = " + str(amper) + " A"))

    def generatePoints(self):
        times = self.res_slider.value() * 8
        for point in self.groupBox.findChildren(QtWidgets.QLabel):
            if point.objectName() != "cylindr_label":
                point.deleteLater()

        for i in range(0, times):
            self.point = QtWidgets.QLabel(self.groupBox)
            self.point.setGeometry(QtCore.QRect(random.randrange(
                20, 195), random.randrange(10, 80), 2, 2))
            # self.point.setGeometry(QtCore.QRect(0, 0, 30, 30))
            self.point.setStyleSheet("background-color: #000")
            self.point.setText("")
            self.point.setObjectName("point_" + str(i))
            self.point.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())
