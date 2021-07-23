
import sqlite3 as sql
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2

class Ui_Doctor(QtWidgets.QWidget):
    def __init__(self,var):
        super().__init__()
        self.var = var
        self.resize(777, 479)

        self.setStyleSheet("QPushButton{border:1px solid;border-color:White;color:White;} QPushButton:hover{background:white;color:#1A1627;}")

        self.lbl_background = QtWidgets.QLabel(self)
        self.lbl_background.setGeometry(QtCore.QRect(0, -10, 771, 571))
        self.lbl_background.setStyleSheet("background:#1A1627;")

        self.lbl_Image = QtWidgets.QLabel(self)
        self.lbl_Image.setEnabled(True)
        self.lbl_Image.setGeometry(QtCore.QRect(580, 30, 151, 151))
        self.lbl_Image.setMinimumSize(QtCore.QSize(151, 141))
        self.lbl_Image.setStyleSheet("border:1px solid;border-color:White;")

        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setGeometry(QtCore.QRect(620, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_name.setFont(font)
        self.lbl_name.setStyleSheet("color:White;")

        self.lbl_ID = QtWidgets.QLabel(self)
        self.lbl_ID.setGeometry(QtCore.QRect(580, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_ID.setFont(font)
        self.lbl_ID.setStyleSheet("color:White;")

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 511, 261))
        self.groupBox.setStyleSheet("color:White;")

        self.txt_allAppointment = QtWidgets.QTextBrowser(self)
        self.txt_allAppointment.setGeometry(QtCore.QRect(20, 38, 491, 231))

        self.line_mid_a = QtWidgets.QFrame(self)
        self.line_mid_a.setGeometry(QtCore.QRect(10, 300, 701, 20))
        self.line_mid_a.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_mid_a.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_mid_b = QtWidgets.QFrame(self)
        self.line_mid_b.setGeometry(QtCore.QRect(30, 290, 701, 20))
        self.line_mid_b.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_mid_b.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_patientID = QtWidgets.QLineEdit(self)
        self.line_patientID.setGeometry(QtCore.QRect(350, 340, 81, 31))
        self.line_patientID.setText("")

        self.btn_success = QtWidgets.QPushButton(self)
        self.btn_success.setGeometry(QtCore.QRect(350, 380, 81, 31))

        self.txt_recete = QtWidgets.QTextEdit(self)
        self.txt_recete.setGeometry(QtCore.QRect(20, 340, 321, 121))

        self.lbl_txt_recete = QtWidgets.QLabel(self)
        self.lbl_txt_recete.setGeometry(QtCore.QRect(20, 320, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_txt_recete.setFont(font)
        self.lbl_txt_recete.setStyleSheet("color:White;")

        self.txt_output = QtWidgets.QTextEdit(self)
        self.txt_output.setGeometry(QtCore.QRect(450, 340, 291, 121))

        self.lbl_txt_output = QtWidgets.QLabel(self)
        self.lbl_txt_output.setGeometry(QtCore.QRect(450, 320, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_txt_output.setFont(font)
        self.lbl_txt_output.setStyleSheet("color:White;")
        
        self.btn_success.clicked.connect(self.success)
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def success(self):
        try:
            vt = sql.connect("Database/database.db")
            cursor = vt.cursor()
            patientID = int(self.line_patientID.text())
            print(patientID)
            if self.txt_recete.toPlainText() != "":
                result = cursor.execute("update appointment set success = 1 where id = {}".format(patientID)).rowcount
                if(result == 1):
                    self.txt_output.append("patient discharged successfully")
                else:
                    self.txt_output.append("Please check ID")

            else:
                self.txt_output.append("Please Write Recipe")
            vt.commit()
            vt.close()
            self.refresh()
        except:
            self.txt_output.append("Error during success check ID. \n Maybe ur ID not Integer")

    def refresh(self):

        try:

            vt = sql.connect("Database/database.db")
            cursor = vt.cursor()


            self.doctorInfo = cursor.execute("Select * FROM doctor where id = {}".format(self.var.loginedID)).fetchall()[0]

            self.lbl_ID.setText(str(self.var.loginedID))  # print ID

            self.lbl_name.setText(
                "{} {}".format(self.doctorInfo[1], self.doctorInfo[2]))  # print name and surname


            img = cv2.imread(self.doctorInfo[6])  # print image  1
            cv2.imwrite("Images/pathImage.jpg", cv2.resize(img, (151, 151)))  # 2
            self.lbl_Image.setStyleSheet("background:url(Images/pathImage.jpg)")  # 3

            allAppointments = cursor.execute("Select * from appointment where confirm = 1 AND doctor_id = {} and success == 0 ".format(self.lbl_ID.text())).fetchall()
            self.txt_allAppointment.clear()



            self.txt_allAppointment.append("    id             p_id                  d_id                      profession                               day ")
            # Show all appointments info

            txt = ""
            for appointment in allAppointments:
                txt += "   " + str(appointment[0])

                for j in range(18 - len(str(appointment[0]))):
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

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Doctor"))
        self.lbl_name.setText(_translate("self", "Ad"))
        self.lbl_ID.setText(_translate("self", "ID"))
        self.groupBox.setTitle(_translate("self", "Hastalar"))
        self.btn_success.setText(_translate("self", "Success"))
        self.lbl_txt_recete.setText(_translate("self", "Reçete"))
        self.lbl_txt_output.setText(_translate("self", "Output"))



