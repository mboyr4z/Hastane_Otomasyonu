from Hospital_Automation.Database.AddHuman import addDoctortoDatabase,addPatienttoDatabase,addPharmacisttoDatabase,addCounselortoDatabase

class register_functions():

    def __init__(self,var):
        self.var = var
        self.errorCount = 0

    def f_register(self):           ## kayıt ol kısmımız
        self.f_check_All_Input_and_Register()        #kaydolmadan önce input kontrollerim

    def f_check_All_Input_and_Register(self):
        self.errorCount = 0
        if self.var.selectedJob == "doctor":        # doktor için olan input kontrollerim

            if(self.var.screen_register.doctor_line_name.text() == ""):
                print("name cant be null")

            elif(self.var.screen_register.doctor_line_surname.text() == ""):
                print("surname cant be null")

            elif(self.var.screen_register.doctor_line_username.text() == ""):
                print("username cant be null")

            elif(self.var.screen_register.doctor_line_password.text() == ""):
                print("password cant be null")
            elif self.var.imagePath == "":
                print("image Path catn be null. Please select Image!!.")
            else:
                self.doctor_name =     self.var.screen_register.doctor_line_name.text()
                self.doctor_surname =  self.var.screen_register.doctor_line_surname.text()
                self.doctor_username = self.var.screen_register.doctor_line_username.text()
                self.doctor_password = self.var.screen_register.doctor_line_password.text()
                self.doctor_profession = self.var.screen_register.doctor_combo_profession.currentText()

                addDoctortoDatabase("Database/database.db",self.doctor_name,self.doctor_surname,self.doctor_profession,self.doctor_username,self.doctor_password,self.var.imagePath)


        elif self.var.selectedJob == "patient":         #hasta için input kontrollerim
            self.errorCount = 0
            if (self.var.screen_register.patient_line_name.text() == ""):
                print("name cant be null")
                self.errorCount+=1
            elif (self.var.screen_register.patient_line_surname.text() == ""):
                print("surname cant be null")
                self.errorCount += 1
            elif (self.var.screen_register.patient_line_username.text() == ""):
                print("username cant be null")
                self.errorCount += 1
            elif (self.var.screen_register.patient_line_password.text() == ""):
                print("password cant be null")
                self.errorCount += 1

            try:
                a = int(self.var.screen_register.patient_line_tc.text())
            except :
                print("TC only can be number")
                self.errorCount += 1

            try:
                a = int(self.var.screen_register.patient_line_age.text())
            except:
                print("Age can be only number")
                self.errorCount += 1

            try:
                a = int(self.var.screen_register.patient_line_gender.text())
            except:
                print("Gender can be only number ('0' girl and '1' man)")
                self.errorCount += 1

            if self.errorCount == 0:
                tc_id = self.var.screen_register.patient_line_tc.text()
                name = self.var.screen_register.patient_line_name.text()
                surname = self.var.screen_register.patient_line_surname.text()
                age = int(self.var.screen_register.patient_line_age.text())
                gender = int(self.var.screen_register.patient_line_gender.text())
                username = self.var.screen_register.patient_line_username.text()
                password = self.var.screen_register.patient_line_password.text()
                addPatienttoDatabase("Database/database.db",tc_id,name,surname,age,gender,username,password,self.var.imagePath)
            else:
                print("Fix All errors then try again!")



        elif self.var.selectedJob == "counselor":
            print("Counselordayız")
            if (self.var.screen_register.counselor_line_name.text() == ""):
                print("name cant be null")
            elif (self.var.screen_register.counselor_line_surname.text() == ""):
                print("surname cant be null")
            elif (self.var.screen_register.counselor_line_username.text() == ""):
                print("username cant be null")
            elif (self.var.screen_register.counselor_line_password.text() == ""):
                print("password cant be null")
            else:
                name = self.var.screen_register.counselor_line_name.text()
                surname = self.var.screen_register.counselor_line_surname.text()
                username = self.var.screen_register.counselor_line_username.text()
                password = self.var.screen_register.counselor_line_password.text()
                imagePath = self.var.imagePath
                addCounselortoDatabase("Database/database.db",name,surname,username,password,imagePath)


        else:
            if (self.var.screen_register.pharmacist_line_name.text() == ""):
                print("name cant be null")
            elif (self.var.screen_register.pharmacist_line_surname.text() == ""):
                print("surname cant be null")
            elif (self.var.screen_register.pharmacist_line_username.text() == ""):
                print("username cant be null")
            elif (self.var.screen_register.pharmacist_line_password.text() == ""):
                print("password cant be null")
            else:
                name = self.var.screen_register.pharmacist_line_name.text()
                surname = self.var.screen_register.pharmacist_line_surname.text()
                username = self.var.screen_register.pharmacist_line_username.text()
                password = self.var.screen_register.pharmacist_line_password.text()
                addPharmacisttoDatabase("Database/database.db",name,surname,username,password,self.var.imagePath)




