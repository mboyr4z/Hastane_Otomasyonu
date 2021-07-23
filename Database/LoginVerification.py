import sqlite3 as sql

def f_Input_Control_and_Login_Verification(var):
    if(var.screen_login.line_username.text() == ""):
        print("username cant be null")
    elif var.screen_login.line_password.text() == "":
        print("password cant be null")
    else:
        if(var.screen_login.rdy_doctor.isChecked()):
            var.loginedJob = "doctor"
        elif(var.screen_login.rdy_patient.isChecked()):
            var.loginedJob = "patient"
        elif (var.screen_login.rdy_pharmacist.isChecked()):
            var.loginedJob = "pharmacist"
        else:
            var.loginedJob = "counselor"
        isSuccess = f_LoginVerification(var,"Database/database.db",var.screen_login.line_username.text(),var.screen_login.line_password.text(),var.loginedJob)
        if isSuccess:
            var.screen_login.setVisible(False)
            if var.loginedJob == "doctor":
                var.screen_doctor.show()
                var.screen_doctor.refresh()
            elif var.loginedJob == "patient":
                var.screen_patient.show()
                var.screen_patient.refresh()
            elif var.loginedJob == "pharmacist":
                var.screen_pharmacist.show()
                var.screen_pharmacist.refresh()
            else:
                var.screen_counselor.show()
                var.screen_counselor.refresh()

def f_LoginVerification(var,dbPath,username,password,tableName):
        try:
            db = sql.connect(dbPath)
            cursor = db.cursor()

            request = cursor.execute("SELECT * FROM {} where username = '{}' ".format(tableName,username)).fetchall()
            if(tableName == "doctor" and str(password) == str(request[0][5])):
                var.loginedID = request[0][0]
                return True
            elif(tableName == "patient" and str(password) == str(request[0][7])):
                var.loginedID = request[0][0]
                return True
            elif(tableName == "pharmacist" and str(password) == str(request[0][4])):
                var.loginedID = request[0][0]
                return True
            elif(tableName == "counselor" and str(password) == str(request[0][4])):
                var.loginedID = request[0][0]
                return True
            else:
                print("Username or password invalid")
                return False

            db.commit()
            db.close()

        except:
            print("Username or password invalid")
            return False