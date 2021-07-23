

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql
import cv2

from Hospital_Automation.Database.DeleteAppointment import f_DeleteAppointment


class Ui_Pharmacist(QtWidgets.QWidget):
    def __init__(self,var):
        super().__init__()
        self.var = var
        self.resize(690, 281)
        self.setStyleSheet("QPushButton{border:1px solid;border-color:White;color:White;} QPushButton:hover{background:white;color:#1A1627;}")

        self.lbl_background = QtWidgets.QLabel(self)
        self.lbl_background.setGeometry(QtCore.QRect(-20, -20, 831, 301))
        self.lbl_background.setStyleSheet("background:#1A1627;")

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 511, 261))
        self.groupBox.setStyleSheet("color:White;")

        self.txt_allAppointment = QtWidgets.QTextBrowser(self)
        self.txt_allAppointment.setGeometry(QtCore.QRect(20, 28, 491, 231))

        self.lbl_Image = QtWidgets.QLabel(self)
        self.lbl_Image.setEnabled(True)
        self.lbl_Image.setGeometry(QtCore.QRect(530, 30, 151, 151))
        self.lbl_Image.setMinimumSize(QtCore.QSize(151, 141))
        self.lbl_Image.setStyleSheet("border:1px solid;border-color:white;")

        self.lbl_ID = QtWidgets.QLabel(self)
        self.lbl_ID.setGeometry(QtCore.QRect(530, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_ID.setFont(font)
        self.lbl_ID.setStyleSheet("color:White;")

        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setGeometry(QtCore.QRect(570, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_name.setFont(font)
        self.lbl_name.setStyleSheet("color:White;")
        self.lbl_name.setObjectName("lbl_name")
        self.line_appointmentID = QtWidgets.QLineEdit(self)
        self.line_appointmentID.setGeometry(QtCore.QRect(530, 200, 81, 31))

        self.btn_giveMedicine = QtWidgets.QPushButton(self)
        self.btn_giveMedicine.setGeometry(QtCore.QRect(530, 240, 81, 31))

        self.btn_giveMedicine.clicked.connect(self.giveMedicine)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def giveMedicine(self):
        try:
            appointmentID = int(self.line_appointmentID.text())
            f_DeleteAppointment(appointmentID, self)
            self.refresh()
        except:
            self.txt_allAppointment.append("Check ID")


    def refresh(self):

        try:

            vt = sql.connect("Database/database.db")
            cursor = vt.cursor()

            self.pharmacistInfo = cursor.execute("Select * FROM pharmacist where id = {}".format(self.var.loginedID)).fetchall()[0]
            self.lbl_ID.setText(str(self.var.loginedID))  # print ID
            self.lbl_name.setText(
                "{} {}".format(self.pharmacistInfo[1], self.pharmacistInfo[2]))  # print name and surname

            img = cv2.imread(self.pharmacistInfo[5])  # print image  1
            cv2.imwrite("Images/pathImage.jpg", cv2.resize(img, (151, 151)))  # 2
            self.lbl_Image.setStyleSheet("background:url(Images/pathImage.jpg)")  # 3
            allAppointments = cursor.execute("Select * from appointment where success == 1 ").fetchall()
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
        self.setWindowTitle(_translate("self", "Pharmacist"))
        self.groupBox.setTitle(_translate("self", "Reçeteler"))
        self.lbl_ID.setText(_translate("self", "ID"))
        self.lbl_name.setText(_translate("self", "Ad"))
        self.btn_giveMedicine.setText(_translate("self", "Give Med"))


