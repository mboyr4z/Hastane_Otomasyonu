

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScreenLogin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(340, 283)
        self.setStyleSheet("QLabel{color:white;}QRadioButton{color:White;}QPushButton{border:1px solid;border-color:White;color:White;} QPushButton:hover{background:white;color:#1A1627;}")

        self.lbl_background = QtWidgets.QLabel(self)
        self.lbl_background.setGeometry(QtCore.QRect(-10, -10, 391, 361))
        self.lbl_background.setStyleSheet("background:#1A1627;")

        self.line_password = QtWidgets.QLineEdit(self)
        self.line_password.setGeometry(QtCore.QRect(90, 80, 221, 31))

        self.lbl_txt_or = QtWidgets.QLabel(self)
        self.lbl_txt_or.setGeometry(QtCore.QRect(190, 240, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_txt_or.setFont(font)

        self.rdy_doctor = QtWidgets.QRadioButton(self)
        self.rdy_doctor.setGeometry(QtCore.QRect(230, 130, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.rdy_doctor.setFont(font)
        self.rdy_doctor.setChecked(True)

        self.line_username = QtWidgets.QLineEdit(self)
        self.line_username.setGeometry(QtCore.QRect(90, 40, 221, 31))

        self.btn_register = QtWidgets.QPushButton(self)
        self.btn_register.setGeometry(QtCore.QRect(220, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_register.setFont(font)

        self.setWindowTitle("Login")

        self.lbl_jobImage = QtWidgets.QLabel(self)
        self.lbl_jobImage.setGeometry(QtCore.QRect(90, 120, 121, 101))
        self.lbl_jobImage.setStyleSheet("border:1px solid;\n")
        self.lbl_jobImage.setText("")

        self.lbl_txt_username = QtWidgets.QLabel(self)
        self.lbl_txt_username.setGeometry(QtCore.QRect(10, 40, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.lbl_txt_username.setFont(font)

        self.rdy_patient = QtWidgets.QRadioButton(self)
        self.rdy_patient.setGeometry(QtCore.QRect(230, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.rdy_patient.setFont(font)

        self.btn_login = QtWidgets.QPushButton(self)
        self.btn_login.setGeometry(QtCore.QRect(90, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)

        self.rdy_counselor = QtWidgets.QRadioButton(self)
        self.rdy_counselor.setGeometry(QtCore.QRect(230, 170, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.rdy_counselor.setFont(font)

        self.rdy_pharmacist = QtWidgets.QRadioButton(self)
        self.rdy_pharmacist.setGeometry(QtCore.QRect(230, 190, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.rdy_pharmacist.setFont(font)

        self.lbl_txt_password = QtWidgets.QLabel(self)
        self.lbl_txt_password.setGeometry(QtCore.QRect(10, 80, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.lbl_txt_password.setFont(font)


        self.lbl_text_loginPage = QtWidgets.QLabel(self)
        self.lbl_text_loginPage.setGeometry(QtCore.QRect(100, 10, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_text_loginPage.setFont(font)
        self.lbl_text_loginPage.setAlignment(QtCore.Qt.AlignCenter)

        self.rdy_doctor.toggled.connect(self.radioController)
        self.rdy_patient.toggled.connect(self.radioController)
        self.rdy_pharmacist.toggled.connect(self.radioController)
        self.rdy_counselor.toggled.connect(self.radioController)
        self.radioController()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def radioController(self):
        if self.rdy_doctor.isChecked():
            self.jobImagePath = "Design/images/doctor.jpg"
        elif self.rdy_patient.isChecked():
            self.jobImagePath = "Design/images/patient.jpg"
        elif self.rdy_counselor.isChecked():
            self.jobImagePath = "Design/images/counselor.jpg"
        else:
            self.jobImagePath = "Design/images/pharmacist.jpg"

        self.query = "background-image:url('"+self.jobImagePath+"');background-repeat:no-repeat;"
        self.lbl_jobImage.setStyleSheet(self.query)



    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Login"))
        self.lbl_txt_or.setText(_translate("self", "or"))
        self.rdy_doctor.setText(_translate("self", "Doctor"))
        self.btn_register.setText(_translate("self", "Register"))
        self.lbl_txt_username.setText(_translate("self", "Username :"))
        self.rdy_patient.setText(_translate("self", "Patient"))
        self.btn_login.setText(_translate("self", "Login"))
        self.rdy_counselor.setText(_translate("self", "Counselor"))
        self.rdy_pharmacist.setText(_translate("self", "Pharmacist"))
        self.lbl_txt_password.setText(_translate("self", "Password : "))
        self.lbl_text_loginPage.setText(_translate("self", "LOGIN PAGE"))


