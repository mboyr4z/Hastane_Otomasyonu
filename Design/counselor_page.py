import sqlite3 as sql

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from Hospital_Automation.Database.AddAppointment import f_AddAppointment
from Hospital_Automation.Database.DeleteAppointment import f_DeleteAppointment

class Ui_Counselor(QtWidgets.QWidget):
    def __init__(self, var):
        super().__init__()
        self.var = var
        self.resize(758, 518)

        self.setStyleSheet("QPushButton{border:1px solid;border-color:White;color:White;} QPushButton:hover{background:white;color:#1A1627;}")

        self.lbl_background = QtWidgets.QLabel(self)
        self.lbl_background.setGeometry(QtCore.QRect(-10, -50, 771, 571))
        self.lbl_background.setStyleSheet("background:#1A1627;")

        self.txt_allAppointment = QtWidgets.QTextBrowser(self)
        self.txt_allAppointment.setGeometry(QtCore.QRect(20, 300, 421, 201))

        self.combo_profession = QtWidgets.QComboBox(self)
        self.combo_profession.setGeometry(QtCore.QRect(120, 60, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.combo_profession.setFont(font)
        self.combo_profession.addItem("")
        self.combo_profession.addItem("")
        self.combo_profession.addItem("")

        self.combo_doctor = QtWidgets.QComboBox(self)
        self.combo_doctor.setGeometry(QtCore.QRect(120, 100, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.combo_doctor.setFont(font)

        self.date_day = QtWidgets.QDateEdit(self)
        self.date_day.setGeometry(QtCore.QRect(120, 140, 151, 31))

        self.btn_delete = QtWidgets.QPushButton(self)
        self.btn_delete.setGeometry(QtCore.QRect(450, 340, 81, 31))

        self.btn_addAppointment = QtWidgets.QPushButton(self)
        self.btn_addAppointment.setGeometry(QtCore.QRect(120, 180, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(10)
        self.btn_addAppointment.setFont(font)

        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setGeometry(QtCore.QRect(380, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_name.setFont(font)
        self.lbl_name.setStyleSheet("color:White;")

        self.line_mid_a = QtWidgets.QFrame(self)
        self.line_mid_a.setGeometry(QtCore.QRect(20, 280, 511, 20))
        self.line_mid_a.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_mid_a.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.lbl_Image = QtWidgets.QLabel(self)
        self.lbl_Image.setEnabled(True)
        self.lbl_Image.setGeometry(QtCore.QRect(340, 30, 151, 151))
        self.lbl_Image.setMinimumSize(QtCore.QSize(151, 141))
        self.lbl_Image.setStyleSheet("border:1px solid;\nborder-color:white;")


        self.lbl_ID = QtWidgets.QLabel(self)
        self.lbl_ID.setGeometry(QtCore.QRect(340, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_ID.setFont(font)
        self.lbl_ID.setStyleSheet("color:White;")

        self.txt_doctor = QtWidgets.QLabel(self)
        self.txt_doctor.setGeometry(QtCore.QRect(40, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_doctor.setFont(font)
        self.txt_doctor.setStyleSheet("color:White;")
        self.txt_doctor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.line_deleteID = QtWidgets.QLineEdit(self)
        self.line_deleteID.setGeometry(QtCore.QRect(450, 300, 81, 31))
        
        self.txt_day = QtWidgets.QLabel(self)
        self.txt_day.setGeometry(QtCore.QRect(40, 140, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_day.setFont(font)
        self.txt_day.setStyleSheet("color:White;")
        self.txt_day.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.txt_output = QtWidgets.QTextBrowser(self)
        self.txt_output.setGeometry(QtCore.QRect(560, 70, 191, 431))

        self.line_confirmID = QtWidgets.QLineEdit(self)
        self.line_confirmID.setGeometry(QtCore.QRect(560, 10, 101, 31))
        
        self.btn_confirm = QtWidgets.QPushButton(self)
        self.btn_confirm.setGeometry(QtCore.QRect(670, 10, 81, 31))

        self.lbl_txt_info = QtWidgets.QLabel(self)
        self.lbl_txt_info.setGeometry(QtCore.QRect(560, 40, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_txt_info.setFont(font)
        self.lbl_txt_info.setStyleSheet("color:White;")
        self.lbl_txt_info.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.line_patientID = QtWidgets.QLineEdit(self)
        self.line_patientID.setGeometry(QtCore.QRect(120, 20, 151, 31))
        self.txt_profession = QtWidgets.QLabel(self)
        self.txt_profession.setGeometry(QtCore.QRect(30, 60, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_profession.setFont(font)
        self.txt_profession.setStyleSheet("color:White;")
        self.txt_profession.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.txt_patientID = QtWidgets.QLabel(self)
        self.txt_patientID.setGeometry(QtCore.QRect(30, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_patientID.setFont(font)
        self.txt_patientID.setStyleSheet("color:White;")
        self.txt_patientID.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
   
        self.line_mid_b = QtWidgets.QFrame(self)
        self.line_mid_b.setGeometry(QtCore.QRect(20, 270, 511, 20))
        self.line_mid_b.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_mid_b.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_mid_c = QtWidgets.QFrame(self)
        self.line_mid_c.setGeometry(QtCore.QRect(510, 10, 20, 261))
        self.line_mid_c.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_mid_c.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.line_mid_d = QtWidgets.QFrame(self)
        self.line_mid_d.setGeometry(QtCore.QRect(520, 10, 20, 261))
        self.line_mid_d.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_mid_d.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.combo_profession.currentTextChanged.connect(self.changeDoctorByProfession)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_addAppointment.clicked.connect(self.controlAndAddAppointment)
        self.btn_confirm.clicked.connect(self.confirm)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def confirm(self):
        try:
            confirmID = int(self.line_confirmID.text())
            try:
                db = sql.connect("Database/database.db")
                cursor = db.cursor()
                result = cursor.execute("update appointment set confirm = 1 where id = {}".format(confirmID))
                if(result.rowcount == 0):
                    self.txt_output.append("Check ID")
                else:
                    self.txt_output.append("Confirm Succesfully")
                db.commit()
                db.close()
                self.refresh()

            except:
                self.txt_output.append("Database Error")
        except:
            self.txt_output.append("Confirm ID must be Integer")



    def controlAndAddAppointment(self):
        if self.line_patientID.text() == "":
            self.txt_output.append("Patient ID null")
        elif self.combo_doctor.currentText() == "":
            self.txt_output.append("Doctor Null")
        elif self.combo_profession.currentText() == "":
            self.txt_output.append("Profession null")
        elif self.date_day.date().getDate() == "":
            self.txt_output.append("Date null")
        else:
            doctor_name = self.combo_doctor.currentText().split(" ")[0]

            try:
                ID = int(self.line_patientID.text())
                db = sql.connect("Database/database.db")
                cursor = db.cursor()
                self.doctor_ID = cursor.execute("SELECT id from doctor where name = '{}'".format(doctor_name)).fetchall()[0][0]
                db.commit()
                db.close()
            except:
                self.txt_output.append("Err query/DB")

            profession = self.combo_profession.currentText()
            day = str(self.date_day.date().getDate())
            f_AddAppointment(int(self.line_patientID.text()),self.doctor_ID,profession,day,0,0,self)
            self.refresh()


    def delete(self):

        try:
            self.id = []
            self.id.append(int(self.line_deleteID.text()))
            self.id = tuple(self.id)


        except:
            self.txt_output.append("ID not INT")

        try:

            vt = sql.connect("Database/database.db")
            cursor = vt.cursor()

            allID = cursor.execute("select id from appointment").fetchall()

            if self.id in allID:
                f_DeleteAppointment(self.id[0], self)
         
            else:
                self.txt_output.append("ID Not Fo.")


            vt.commit()
            vt.close()
            self.refresh()

        except:
            self.txt_output.append("Error ")
    
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

    def refresh(self):

        try:
            vt = sql.connect("Database/database.db")
            cursor = vt.cursor()

            self.counselorInfo = cursor.execute("Select * FROM counselor where id = {}".format(self.var.loginedID)).fetchall()[0]
            self.lbl_ID.setText(str(self.var.loginedID))          # print ID
            self.lbl_name.setText("{} {}".format(self.counselorInfo[1],self.counselorInfo[2])) #print name and surname



            img = cv2.imread(self.counselorInfo[5])             # print image  1
            cv2.imwrite("Images/pathImage.jpg", cv2.resize(img, (151, 151)))      #2
            self.lbl_Image.setStyleSheet("background:url(Images/pathImage.jpg)")#3


            allAppointments = cursor.execute("Select * from appointment where confirm = 0 ").fetchall()
            self.txt_allAppointment.clear()
            self.txt_allAppointment.append("    id             p_id                  d_id                      profession                               day ")

            # Show all appointments info

            txt = ""
            for appointment in allAppointments:
                txt += "   " + str(appointment[0])

                for j in range(18- len(str(appointment[0]))):
                    txt += " "

                txt += str(appointment[1]) + " "

                for j in range(21 - len(str(appointment[1]))):
                    txt += " "

                txt += str(appointment[2]) + " "
                for j in range(26 - len(str(appointment[2]))):
                    txt += " "

                txt += str(appointment[3]) + " "
                for j in range(34 - len(str(appointment[3]))):
                    txt += " "

                txt += str(appointment[4]) + " "
                txt += "\n"

            self.txt_allAppointment.append(txt)

            vt.commit()
            vt.close()
        except:
            self.txt_output.append("Err Refresh")

    def retranslateUi(self, Counselor):
        _translate = QtCore.QCoreApplication.translate
        Counselor.setWindowTitle(_translate("Counselor", "Counselor"))
        self.combo_profession.setItemText(0, _translate("Counselor", "Dahiliye"))
        self.combo_profession.setItemText(1, _translate("Counselor", "Nöroloji"))
        self.combo_profession.setItemText(2, _translate("Counselor", "Diş"))
        self.btn_delete.setText(_translate("Counselor", "Delete"))
        self.btn_addAppointment.setText(_translate("Counselor", "Add Appointment"))
        self.lbl_name.setText(_translate("Counselor", "Ad"))
        self.lbl_ID.setText(_translate("Counselor", "ID"))
        self.txt_doctor.setText(_translate("Counselor", "Doctor : "))
        self.txt_day.setText(_translate("Counselor", "Day : "))
        self.btn_confirm.setText(_translate("Counselor", "Confirm"))
        self.lbl_txt_info.setText(_translate("Counselor", "INFO"))
        self.txt_profession.setText(_translate("Counselor", "Profession : "))
        self.txt_patientID.setText("Patient ID : ")


