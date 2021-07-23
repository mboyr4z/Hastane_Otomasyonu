
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QIcon

from Hospital_Automation.Design.counselor_page import Ui_Counselor
from Hospital_Automation.Design.doctor_page import Ui_Doctor
from Hospital_Automation.Design.functions.clicked_Events import clickedEvents
from Hospital_Automation.Design.login import Ui_ScreenLogin
from Hospital_Automation.Design.patient_page import Ui_Patient
from Hospital_Automation.Design.pharmacist_page import Ui_Pharmacist
from Hospital_Automation.Design.register import Ui_ScreenRegister
from Hospital_Automation.Functions.register_functions import register_functions
from Hospital_Automation.Variables.variables import variables
from Hospital_Automation.Database.LoginVerification import f_Input_Control_and_Login_Verification

def f_define_All_Objects(var):
    var.screen_login = Ui_ScreenLogin()
    var.screen_register = Ui_ScreenRegister(var)

    var.screen_login.show()


    var.clickedEvents = clickedEvents(var)
    var.register_functions = register_functions(var)

    var.screen_patient = Ui_Patient(var)
    var.screen_counselor = Ui_Counselor(var)
    var.screen_doctor = Ui_Doctor(var)
    var.screen_pharmacist = Ui_Pharmacist(var)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    q_pixmap = QPixmap('Images/hospital_1.png')
    q_icon = QIcon(q_pixmap)
    app.setWindowIcon(q_icon)


    var = variables()
    f_define_All_Objects(var)

    #CLICKED EVENTS
    var.screen_register.btn_backloginPage.clicked.connect(var.clickedEvents.f_RegisterToLogin)      # kayıttan logine
    var.screen_login.btn_register.clicked.connect(var.clickedEvents.f_LoginToRegister)              #loginden kayıta
    var.screen_register.btn_register.clicked.connect(var.register_functions.f_register)
    var.screen_login.btn_login.clicked.connect(lambda : f_Input_Control_and_Login_Verification(var))





    sys.exit(app.exec_())
