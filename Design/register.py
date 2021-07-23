

from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import filedialog
from tkinter import *
import cv2

root = Tk()
root.withdraw()

class Ui_ScreenRegister(QtWidgets.QWidget):
    def __init__(self,var):
        super().__init__()

        self.var = var
        self.resize(499, 400)
        self.setStyleSheet("QLabel{color:white;}QPushButton{border:1px solid;border-color:White;color:White;} QPushButton:hover{background:white;color:#1A1627;}")

        self.lbl_background = QtWidgets.QLabel(self)
        self.lbl_background.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.lbl_background.setStyleSheet("background:#1A1627;\n""color:White;")

        self.line = QtWidgets.QLabel(self)
        self.line.setGeometry(QtCore.QRect(16,350,470,3))
        self.line.setStyleSheet("background:White;")


        self.lbl_mid_background = QtWidgets.QLabel(self)
        self.lbl_mid_background.setGeometry(QtCore.QRect(0, 28, 501, 321))
        self.lbl_mid_background.setStyleSheet("background:#1A1627;")


        self.btn_image = QtWidgets.QPushButton(self)
        self.btn_image.setGeometry(QtCore.QRect(330, 60, 151, 141))
        self.btn_image.setStyleSheet("border:1px solid;border-color:white;color:white;")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(60)
        self.btn_image.setFont(font)
        self.btn_image.setText("Resim Ekle")


        self.btn_register = QtWidgets.QPushButton(self)
        self.btn_register.setGeometry(QtCore.QRect(100, 360, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_register.setFont(font)
        self.btn_register.setText("Register")

        self.btn_backloginPage = QtWidgets.QPushButton(self)
        self.btn_backloginPage.setGeometry(QtCore.QRect(14, 360, 41, 31))
        self.btn_backloginPage.setText("Geri")

        self.btn_doctor = QtWidgets.QPushButton(self)
        self.btn_doctor.setGeometry(QtCore.QRect(-5, -5, 130, 35))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_doctor.setFont(font)
        self.btn_doctor.setStyleSheet("background:#1A1627;\n""color:#DCE45B;")
        self.btn_doctor.setText("Doctor")

        self.btn_patient = QtWidgets.QPushButton(self)
        self.btn_patient.setGeometry(QtCore.QRect(120, -5, 130, 35))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_patient.setFont(font)
        self.btn_patient.setStyleSheet("background:#1A1627;\n""color:White;")
        self.btn_patient.setText("Patient")

        self.btn_counselor = QtWidgets.QPushButton(self)
        self.btn_counselor.setGeometry(QtCore.QRect(245, -5, 132, 35))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_counselor.setFont(font)
        self.btn_counselor.setStyleSheet("background:#1A1627;\n""color:White;")
        self.btn_counselor.setText("Counselor")

        self.btn_pharmacist = QtWidgets.QPushButton(self)
        self.btn_pharmacist.setGeometry(QtCore.QRect(374, -5, 131, 35))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_pharmacist.setFont(font)
        self.btn_pharmacist.setStyleSheet("background:#1A1627;\n""color:White;")
        self.btn_pharmacist.setText("Pharmacist")




        # DOKTOR KISMI



        self.doctor_lbl_txt_name = QtWidgets.QLabel(self)
        self.doctor_lbl_txt_name.setGeometry(QtCore.QRect(40, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.doctor_lbl_txt_name.setFont(font)
        self.doctor_lbl_txt_name.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.doctor_lbl_txt_name.setText("Name : ")

        self.doctor_line_surname = QtWidgets.QLineEdit(self)
        self.doctor_line_surname.setGeometry(QtCore.QRect(100, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.doctor_line_surname.setFont(font)


        self.doctor_line_name = QtWidgets.QLineEdit(self)
        self.doctor_line_name.setGeometry(QtCore.QRect(100, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.doctor_line_name.setFont(font)


        self.doctor_lbl_txt_surname = QtWidgets.QLabel(self)
        self.doctor_lbl_txt_surname.setGeometry(QtCore.QRect(20, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.doctor_lbl_txt_surname.setFont(font)
        self.doctor_lbl_txt_surname.setAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.doctor_lbl_txt_surname.setText("Surname : ")

        self.doctor_lbl_txt_username = QtWidgets.QLabel(self)
        self.doctor_lbl_txt_username.setGeometry(QtCore.QRect(20, 180, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.doctor_lbl_txt_username.setFont(font)
        self.doctor_lbl_txt_username.setAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.doctor_lbl_txt_username.setText("Username : ")



        self.doctor_line_password = QtWidgets.QLineEdit(self)
        self.doctor_line_password.setGeometry(QtCore.QRect(100, 220, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.doctor_line_password.setFont(font)
        self.doctor_line_password.setObjectName("doctor_line_password")

        self.doctor_line_username = QtWidgets.QLineEdit(self)
        self.doctor_line_username.setGeometry(QtCore.QRect(100, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.doctor_line_username.setFont(font)

        self.doctor_lbl_txt_password = QtWidgets.QLabel(self)
        self.doctor_lbl_txt_password.setGeometry(QtCore.QRect(20, 220, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.doctor_lbl_txt_password.setFont(font)
        self.doctor_lbl_txt_password.setAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.doctor_lbl_txt_password.setText("Password : ")

        self.doctor_lbl_txt_profession = QtWidgets.QLabel(self)
        self.doctor_lbl_txt_profession.setGeometry(QtCore.QRect(10, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.doctor_lbl_txt_profession.setFont(font)
        self.doctor_lbl_txt_profession.setAlignment(
                QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.doctor_lbl_txt_profession.setText("Profession : ")

        self.doctor_combo_profession = QtWidgets.QComboBox(self)
        self.doctor_combo_profession.setGeometry(QtCore.QRect(100, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.doctor_combo_profession.setFont(font)
        self.doctor_combo_profession.setObjectName("doctor_combo_profession")
        self.doctor_combo_profession.addItem("")
        self.doctor_combo_profession.addItem("")
        self.doctor_combo_profession.addItem("")
        self.doctor_combo_profession.setItemText(0, "Dahiliye")
        self.doctor_combo_profession.setItemText(1, "Nöroloji")
        self.doctor_combo_profession.setItemText(2, "Diş")










        ################### PATİENT KISMI #####################




        self.patient_line_surname = QtWidgets.QLineEdit(self)
        self.patient_line_surname.setGeometry(QtCore.QRect(100, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.patient_line_surname.setFont(font)

        self.patient_line_name = QtWidgets.QLineEdit(self)
        self.patient_line_name.setGeometry(QtCore.QRect(100, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.patient_line_name.setFont(font)

        self.patient_line_password = QtWidgets.QLineEdit(self)
        self.patient_line_password.setGeometry(QtCore.QRect(100, 300, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.patient_line_password.setFont(font)

        self.patient_line_age = QtWidgets.QLineEdit(self)
        self.patient_line_age.setGeometry(QtCore.QRect(100, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.patient_line_age.setFont(font)

        self.patient_line_username = QtWidgets.QLineEdit(self)
        self.patient_line_username.setGeometry(QtCore.QRect(100, 260, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.patient_line_username.setFont(font)

        self.patient_line_gender = QtWidgets.QLineEdit(self)
        self.patient_line_gender.setGeometry(QtCore.QRect(100, 220, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.patient_line_gender.setFont(font)

        self.patient_line_tc = QtWidgets.QLineEdit(self)
        self.patient_line_tc.setGeometry(QtCore.QRect(100, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.patient_line_tc.setFont(font)





        self.patient_lbl_txt_name = QtWidgets.QLabel(self)
        self.patient_lbl_txt_name.setGeometry(QtCore.QRect(40, 100, 61, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.patient_lbl_txt_name.setFont(font)
        self.patient_lbl_txt_name.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.patient_lbl_txt_name.setText("Name : ")

        self.patient_lbl_txt_surname = QtWidgets.QLabel(self)
        self.patient_lbl_txt_surname.setGeometry(QtCore.QRect(20, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.patient_lbl_txt_surname.setFont(font)
        self.patient_lbl_txt_surname.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.patient_lbl_txt_surname.setText("Surname : ")

        self.patient_lbl_txt_gender = QtWidgets.QLabel(self)
        self.patient_lbl_txt_gender.setGeometry(QtCore.QRect(20, 220, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.patient_lbl_txt_gender.setFont(font)
        self.patient_lbl_txt_gender.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.patient_lbl_txt_gender.setText("Gender : ")



        self.patient_lbl_txt_username = QtWidgets.QLabel(self)
        self.patient_lbl_txt_username.setGeometry(QtCore.QRect(20, 260, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.patient_lbl_txt_username.setFont(font)
        self.patient_lbl_txt_username.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.patient_lbl_txt_username.setText("Username : ")

        self.patient_lbl_txt_age = QtWidgets.QLabel(self)
        self.patient_lbl_txt_age.setGeometry(QtCore.QRect(10, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.patient_lbl_txt_age.setFont(font)
        self.patient_lbl_txt_age.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.patient_lbl_txt_age.setText("Age : ")



        self.patient_lbl_txt_tc = QtWidgets.QLabel(self)
        self.patient_lbl_txt_tc.setGeometry(QtCore.QRect(40, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.patient_lbl_txt_tc.setFont(font)
        self.patient_lbl_txt_tc.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.patient_lbl_txt_tc.setText("TC : ")







        self.patient_lbl_txt_password = QtWidgets.QLabel(self)
        self.patient_lbl_txt_password.setGeometry(QtCore.QRect(20, 300, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.patient_lbl_txt_password.setFont(font)
        self.patient_lbl_txt_password.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.patient_lbl_txt_password.setText("Password : ")




        ################ COUNSELOR KISMI ##################33

        self.counselor_lbl_txt_name = QtWidgets.QLabel(self)
        self.counselor_lbl_txt_name.setGeometry(QtCore.QRect(40, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.counselor_lbl_txt_name.setFont(font)
        self.counselor_lbl_txt_name.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.counselor_lbl_txt_name.setText("Name : ")


        self.counselor_line_surname = QtWidgets.QLineEdit(self)
        self.counselor_line_surname.setGeometry(QtCore.QRect(100, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.counselor_line_surname.setFont(font)


        self.counselor_line_name = QtWidgets.QLineEdit(self)
        self.counselor_line_name.setGeometry(QtCore.QRect(100, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.counselor_line_name.setFont(font)


        self.counselor_lbl_txt_surname = QtWidgets.QLabel(self)
        self.counselor_lbl_txt_surname.setGeometry(QtCore.QRect(20, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.counselor_lbl_txt_surname.setFont(font)
        self.counselor_lbl_txt_surname.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.counselor_lbl_txt_surname.setText("Surname : ")

        self.counselor_line_username = QtWidgets.QLineEdit(self)
        self.counselor_line_username.setGeometry(QtCore.QRect(100, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.counselor_line_username.setFont(font)

        self.counselor_lbl_txt_username = QtWidgets.QLabel(self)
        self.counselor_lbl_txt_username.setGeometry(QtCore.QRect(20, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.counselor_lbl_txt_username.setFont(font)
        self.counselor_lbl_txt_username.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.counselor_lbl_txt_username.setText("Username : ")

        self.counselor_lbl_txt_password = QtWidgets.QLabel(self)
        self.counselor_lbl_txt_password.setGeometry(QtCore.QRect(20, 180, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.counselor_lbl_txt_password.setFont(font)
        self.counselor_lbl_txt_password.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.counselor_lbl_txt_password.setText("Password : ")

        self.counselor_line_password = QtWidgets.QLineEdit(self)
        self.counselor_line_password.setGeometry(QtCore.QRect(100, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.counselor_line_password.setFont(font)







        ################  PHARMACIST KISMI  ###################

        self.pharmacist_lbl_txt_name = QtWidgets.QLabel(self)
        self.pharmacist_lbl_txt_name.setGeometry(QtCore.QRect(40, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.pharmacist_lbl_txt_name.setFont(font)
        self.pharmacist_lbl_txt_name.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.pharmacist_lbl_txt_name.setText("Name : ")

        self.pharmacist_line_surname = QtWidgets.QLineEdit(self)
        self.pharmacist_line_surname.setGeometry(QtCore.QRect(100, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pharmacist_line_surname.setFont(font)


        self.pharmacist_line_name = QtWidgets.QLineEdit(self)
        self.pharmacist_line_name.setGeometry(QtCore.QRect(100, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pharmacist_line_name.setFont(font)
        self.pharmacist_line_name.setObjectName("pharmacist_line_name")

        self.pharmacist_lbl_txt_surname = QtWidgets.QLabel(self)
        self.pharmacist_lbl_txt_surname.setGeometry(QtCore.QRect(20, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.pharmacist_lbl_txt_surname.setFont(font)
        self.pharmacist_lbl_txt_surname.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.pharmacist_lbl_txt_surname.setText("Surname : ")

        self.pharmacist_line_username = QtWidgets.QLineEdit(self)
        self.pharmacist_line_username.setGeometry(QtCore.QRect(100, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pharmacist_line_username.setFont(font)


        self.pharmacist_lbl_txt_username = QtWidgets.QLabel(self)
        self.pharmacist_lbl_txt_username.setGeometry(QtCore.QRect(20, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.pharmacist_lbl_txt_username.setFont(font)
        self.pharmacist_lbl_txt_username.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.pharmacist_lbl_txt_username.setText("Username : ")

        self.pharmacist_lbl_txt_password = QtWidgets.QLabel(self)
        self.pharmacist_lbl_txt_password.setGeometry(QtCore.QRect(20, 180, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.pharmacist_lbl_txt_password.setFont(font)
        self.pharmacist_lbl_txt_password.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.pharmacist_lbl_txt_password.setText("Password : ")


        self.pharmacist_line_password = QtWidgets.QLineEdit(self)
        self.pharmacist_line_password.setGeometry(QtCore.QRect(100, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pharmacist_line_password.setFont(font)
        self.pharmacist_line_password.setObjectName("pharmacist_line_password")

        self.setWindowTitle("Register")

        self.btn_doctor.clicked.connect(self.f_doctor)
        self.btn_patient.clicked.connect(self.f_patient)
        self.btn_pharmacist.clicked.connect(self.f_pharmacist)
        self.btn_counselor.clicked.connect(self.f_counselor)

        self.btn_image.clicked.connect(self.f_selectImage)

        self.f_openClose_doctor(True)
        self.f_openClose_patient(False)
        self.f_openClose_counselor(False)
        self.f_openClose_pharmacist(False)



        QtCore.QMetaObject.connectSlotsByName(self)

    def f_selectImage(self):
        self.var.imagePath = filedialog.askopenfilename()
        if(self.var.imagePath.endswith(".jpg") or self.var.imagePath.endswith(".png") or self.var.imagePath.endswith(".jpeg")):
            img = cv2.imread(self.var.imagePath)
            img = cv2.resize(img,(151,141))
            cv2.imwrite("images/ownPhoto.jpg",img)
            self.btn_image.setText("")

            self.btn_image.setStyleSheet("background:url('Images/ownPhoto.jpg')")
        else:
            print(self.var.imagePath + " yanlış")

    def f_doctor(self):
        self.f_openClose_doctor(True)
        self.f_openClose_patient(False)
        self.f_openClose_counselor(False)
        self.f_openClose_pharmacist(False)
        self.var.selectedJob = "doctor"
    def f_patient(self):
        self.f_openClose_doctor(False)
        self.f_openClose_patient(True)
        self.f_openClose_counselor(False)
        self.f_openClose_pharmacist(False)
        self.var.selectedJob = "patient"
    def f_pharmacist(self):
        self.f_openClose_doctor(False)
        self.f_openClose_patient(False)
        self.f_openClose_counselor(False)
        self.f_openClose_pharmacist(True)
        self.var.selectedJob = "pharmacist"
    def f_counselor(self):
        self.f_openClose_doctor(False)
        self.f_openClose_patient(False)
        self.f_openClose_counselor(True)
        self.f_openClose_pharmacist(False)
        self.var.selectedJob = "counselor"

    def f_openClose_counselor(self, bool):
        self.counselor_lbl_txt_name.setVisible(bool)
        self.counselor_lbl_txt_surname.setVisible(bool)
        self.counselor_lbl_txt_username.setVisible(bool)
        self.counselor_lbl_txt_password.setVisible(bool)

        self.counselor_line_name.setVisible(bool)
        self.counselor_line_surname.setVisible(bool)
        self.counselor_line_username.setVisible(bool)
        self.counselor_line_password.setVisible(bool)

        if bool == True:
            self.btn_counselor.setStyleSheet("background:#1A1627;\n""color:#DCE45B;")
        else:
            self.btn_counselor.setStyleSheet("background:#3C2B76;\n""color:White;")
    def f_openClose_patient(self,bool):

        self.patient_lbl_txt_tc.setVisible(bool)
        self.patient_lbl_txt_name.setVisible(bool)
        self.patient_lbl_txt_surname.setVisible(bool)
        self.patient_lbl_txt_age.setVisible(bool)
        self.patient_lbl_txt_gender.setVisible(bool)
        self.patient_lbl_txt_username.setVisible(bool)
        self.patient_lbl_txt_password.setVisible(bool)


        self.patient_line_tc.setVisible(bool)
        self.patient_line_name.setVisible(bool)
        self.patient_line_surname.setVisible(bool)
        self.patient_line_age.setVisible(bool)
        self.patient_line_gender.setVisible(bool)
        self.patient_line_username.setVisible(bool)
        self.patient_line_password.setVisible(bool)



        if bool == True:
                self.btn_patient.setStyleSheet("background:#1A1627;\n""color:#DCE45B;")
                # BURAYA FOTO DEĞİŞTİRME GELECEK
        else:
                self.btn_patient.setStyleSheet("background:#3C2B76;\n""color:White;")
    def f_openClose_doctor(self,bool):

        self.doctor_lbl_txt_surname.setVisible(bool)
        self.doctor_lbl_txt_name.setVisible(bool)
        self.doctor_lbl_txt_profession.setVisible(bool)
        self.doctor_lbl_txt_username.setVisible(bool)
        self.doctor_lbl_txt_password.setVisible(bool)

        self.doctor_line_name.setVisible(bool)
        self.doctor_line_surname.setVisible(bool)
        self.doctor_line_username.setVisible(bool)
        self.doctor_line_password.setVisible(bool)

        self.doctor_combo_profession.setVisible(bool)


        if bool == True:
                self.btn_doctor.setStyleSheet("background:#1A1627;\n""color:#DCE45B;")
                # BURAYA FOTO DEĞİŞTİRME GELECEK
        else:
                self.btn_doctor.setStyleSheet("background:#3C2B76;\n""color:White;")
    def f_openClose_pharmacist(self, bool):

        self.pharmacist_lbl_txt_name.setVisible(bool)
        self.pharmacist_lbl_txt_surname.setVisible(bool)
        self.pharmacist_lbl_txt_username.setVisible(bool)
        self.pharmacist_lbl_txt_password.setVisible(bool)

        self.pharmacist_line_name.setVisible(bool)
        self.pharmacist_line_surname.setVisible(bool)
        self.pharmacist_line_username.setVisible(bool)
        self.pharmacist_line_password.setVisible(bool)

        if bool == True:
            self.btn_pharmacist.setStyleSheet("background:#1A1627;\n""color:#DCE45B;")
            # BURAYA FOTO DEĞİŞTİRME GELECEK
        else:
            self.btn_pharmacist.setStyleSheet("background:#3C2B76;\n""color:White;")




