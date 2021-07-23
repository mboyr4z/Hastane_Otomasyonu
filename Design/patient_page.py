import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql

from Hospital_Automation.Database.AddAppointment import f_AddAppointment
from Hospital_Automation.Database.DeleteAppointment import f_DeleteAppointment


class Ui_Patient(QtWidgets.QWidget):
    def __init__(self,var):
        super().__init__()
        self.var = var
        self.resize(437, 420)

        self.setStyleSheet("QPushButton{border:1px solid;border-color:White;color:White;} QPushButton:hover{background:white;color:#1A1627;}")

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        
        self.lbl_background = QtWidgets.QLabel(self)
        self.lbl_background.setGeometry(QtCore.QRect(0, 0, 441, 431))
        self.lbl_background.setStyleSheet("background:#1A1627;\n""color:White;")

        self.lbl_ID = QtWidgets.QLabel(self)
        self.lbl_ID.setGeometry(QtCore.QRect(270, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_ID.setFont(font)
        self.lbl_ID.setStyleSheet("color:White;")
        
        self.lbl_txt_profession = QtWidgets.QLabel(self)
        self.lbl_txt_profession.setGeometry(QtCore.QRect(20, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_txt_profession.setFont(font)
        self.lbl_txt_profession.setStyleSheet("color:White;")
        self.lbl_txt_profession.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.lbl_txt_doctor = QtWidgets.QLabel(self)
        self.lbl_txt_doctor.setGeometry(QtCore.QRect(30, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_txt_doctor.setFont(font)
        self.lbl_txt_doctor.setStyleSheet("color:White;")

        self.lbl_txt_day = QtWidgets.QLabel(self)
        self.lbl_txt_day.setGeometry(QtCore.QRect(30, 110, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_txt_day.setFont(font)
        self.lbl_txt_day.setStyleSheet("color:White;")
        self.lbl_txt_day.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.btn_addAppointment = QtWidgets.QPushButton(self)
        self.btn_addAppointment.setGeometry(QtCore.QRect(110, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(10)
        self.btn_addAppointment.setFont(font)

        self.line_ID = QtWidgets.QLineEdit(self)
        self.line_ID.setGeometry(QtCore.QRect(330, 210, 81, 31))
        self.line_ID.setObjectName("line_ID")
        self.btn_delete = QtWidgets.QPushButton(self)
        self.btn_delete.setGeometry(QtCore.QRect(330, 250, 81, 31))
 
        self.txt_allAppointment = QtWidgets.QTextBrowser(self)
        self.txt_allAppointment.setGeometry(QtCore.QRect(30, 210, 291, 201))

        self.txt_output= QtWidgets.QTextBrowser(self)
        self.txt_output.setGeometry(QtCore.QRect(330, 290, 81, 121))

        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setGeometry(QtCore.QRect(310, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_name.setFont(font)
        self.lbl_name.setStyleSheet("color:White;")

        self.combo_profession = QtWidgets.QComboBox(self)
        self.combo_profession.setGeometry(QtCore.QRect(110, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.combo_profession.setFont(font)

        self.combo_profession.addItem("")
        self.combo_profession.addItem("")
        self.combo_profession.addItem("")
        self.line_mid = QtWidgets.QFrame(self)
        self.line_mid.setGeometry(QtCore.QRect(20, 180, 401, 21))
        self.line_mid.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_mid.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.date_day = QtWidgets.QDateEdit(self)
        self.date_day.setGeometry(QtCore.QRect(110, 110, 151, 31))

        self.lbl_Image = QtWidgets.QLabel(self)
        self.lbl_Image.setEnabled(True)
        self.lbl_Image.setGeometry(QtCore.QRect(270, 30, 151, 151))
        self.lbl_Image.setMinimumSize(QtCore.QSize(151, 141))
        self.lbl_Image.setStyleSheet("border:1px solid;")



  
        self.combo_doctor = QtWidgets.QComboBox(self)
        self.combo_doctor.setGeometry(QtCore.QRect(110, 70, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.combo_doctor.setFont(font)

        self.combo_profession.currentTextChanged.connect(self.changeDoctorByProfession)
        self.btn_addAppointment.clicked.connect(self.controlAndAddAppointment)

        self.btn_delete.setEnabled(False)
        self.line_ID.textChanged.connect(self.idControll_and_SetButtonActive)
        self.btn_delete.clicked.connect(self.delete)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def idControll_and_SetButtonActive(self):
        if self.line_ID.text() == "":
            self.btn_delete.setEnabled(False)
        else:
            self.btn_delete.setEnabled(True)

    def delete(self):

        try:
            self.id = []
            self.id.append(int(self.line_ID.text()))
            self.id = tuple(self.id)


        except:
            self.txt_output.append("ID not INT")

        try:

            vt = sql.connect("Database/database.db")
            cursor = vt.cursor()

            allID = cursor.execute("select id from appointment").fetchall()
            if self.id in allID:
                f_DeleteAppointment(self.id[0],self)
            else:
                self.txt_output.append("ID Not Fo.")



            vt.commit()
            vt.close()
            self.refresh()

        except:
            self.txt_output.append("Err cont. ID")

    def refresh(self):
        self.lbl_ID.setText(str(self.var.loginedID))
        try:
            vt = sql.connect("Database/database.db")
            cursor = vt.cursor()

            patientInfo = cursor.execute("Select * FROM patient where id = {}".format(self.var.loginedID)).fetchall()

            #print image
            img = cv2.imread(patientInfo[0][8])
            cv2.imwrite("Images/Patient.jpg",cv2.resize(img,(151,151)))
            self.lbl_Image.setStyleSheet('background:url("Images/patient.jpg");')

            # print name and surname
            self.lbl_name.setText("{} {}".format(patientInfo[0][2],patientInfo[0][3]))

            allAppointments = cursor.execute("Select * from appointment where patient_id = {}".format(self.var.loginedID)).fetchall()

            self.txt_allAppointment.clear()


            self.txt_allAppointment.append("id    p_id    d_id          profession                      day ")

            # Show all appointments info

            txt = ""
            for appointment in allAppointments:
                txt += str(appointment[0])

                for j in range( 8 - len(str(appointment[0]))):
                    txt += " "

                txt += str(appointment[1]) + " "

                for j in range(10 - len(str(appointment[1]))):
                    txt += " "

                txt += str(appointment[2]) + " "
                for j in range(16 - len(str(appointment[2]))):
                    txt += " "

                txt += str(appointment[3]) + " "
                for j in range(22 - len(str(appointment[3]))):

                    txt += " "

                txt += str(appointment[4]) + " "
                txt+= "\n"

            self.txt_allAppointment.append(txt)



            vt.commit()
            vt.close()
        except:
            self.txt_output.append("Err Refresh")




    def controlAndAddAppointment(self):
        if(self.combo_doctor.currentText() == ""):
            self.txt_output.append("Doc Empty")

        elif self.combo_profession.currentText() == "":
            self.txt_output.append("Pro Empty")
        elif self.date_day.date() == "null":
            self.txt_output.append("Date Empty")
        else:
            ID = self.lbl_ID.text()
            doctor_name = self.combo_doctor.currentText().split(" ")[0]
            try:
                db = sql.connect("Database/database.db")
                cursor = db.cursor()
                self.doctor_ID = cursor.execute("SELECT id from doctor where name = '{}'".format(doctor_name)).fetchall()[0][0]
                print(self.doctor_ID)
                db.commit()
                db.close()
            except:
                self.txt_output.append("Err query/DB")

            profession = self.combo_profession.currentText()

            day = str(self.date_day.date().getDate())

            f_AddAppointment(ID,self.doctor_ID,profession,day,0,0,self)

            self.refresh()



    def changeDoctorByProfession(self):
        self.combo_doctor.clear()
        profession = self.combo_profession.currentText()
        try:
            vt = sql.connect("Database/database.db")
            cursor = vt.cursor()
            doctors = cursor.execute(
                "Select name,surname FROM doctor where profession = '{}'".format(profession)).fetchall()
            count = 0
            for doctor in doctors:
                self.combo_doctor.addItem("")
                self.combo_doctor.setItemText(count,doctor[0] + " " + doctor[1])
                count+=1



            vt.commit()
            vt.close()
        except:
            self.txt_output("Err cha.DR")






    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("Patient")
        self.lbl_ID.setText(_translate("Patient", "ID"))
        self.lbl_txt_profession.setText(_translate("Patient", "Profession : "))
        self.lbl_txt_doctor.setText(_translate("Patient", "Doctor : "))
        self.lbl_txt_day.setText(_translate("Patient", "Day : "))
        self.btn_addAppointment.setText(_translate("Patient", "Add Appointment"))
        self.line_ID.setText(_translate("Patient", "ID :"))
        self.btn_delete.setText(_translate("Patient", "Delete"))
        self.lbl_name.setText(_translate("Patient", "Ad"))
        self.combo_profession.setItemText(0, _translate("Patient", "Dahiliye"))
        self.combo_profession.setItemText(1, _translate("Patient", "Nöroloji"))
        self.combo_profession.setItemText(2, _translate("Patient", "Diş"))



