import sqlite3 as sql
from Hospital_Automation.Database.CheckTables import CheckTables

def addDoctortoDatabase(dbPath,name,surname,profession,username,password,imagePath):
    try:
        CheckTables(dbPath)
        vt = sql.connect(dbPath)
        imlec = vt.cursor()
        command = 'INSERT INTO doctor (name,surname,profession,username,password,imagePath) VALUES  ("{}","{}","{}","{}","{}","{}")'.format(name,surname,profession,username,password,imagePath)
        imlec.execute(command)
        vt.commit()
        vt.close()
        print("{} has been successfully added to doctors".format(name))
    except:
        print("An Error current Add Doctor")

def addPatienttoDatabase(dbPath,tc_id,name,surname,age,gender,username,password,imagePath):
    try:
        CheckTables(dbPath)
        vt = sql.connect(dbPath)

        imlec = vt.cursor()
        command = 'INSERT INTO patient (tc_id,name,surname,age,gender,username,password,imagePath) VALUES  ("{}","{}","{}",{},{},"{}","{}","{}")'.format(tc_id,name,surname,age,gender,username,password,imagePath)
        # age and gender is INTEGER
        imlec.execute(command)
        vt.commit()
        vt.close()
        print("{}  has been successfully added to Patients".format(name))
    except:
        print("An Error current Add Patient")


def addCounselortoDatabase(dbPath,name,surname,username,password,imagePath):
    try:
        CheckTables(dbPath)
        vt = sql.connect(dbPath)
        imlec = vt.cursor()
        command = 'INSERT INTO counselor (name,surname,username,password,imagePath) VALUES  ("{}","{}","{}","{}","{}")'.format(name,surname,username,password,imagePath)
        imlec.execute(command)
        vt.commit()
        vt.close()
        print("{}  has been successfully added to Conselors".format(name))
    except:
        print("An Error current Add Conselor")


def addPharmacisttoDatabase(dbPath,name,surname,username,password,imagePath):
    try:
        CheckTables(dbPath)
        vt = sql.connect(dbPath)
        imlec = vt.cursor()
        command = 'INSERT INTO pharmacist (name,surname,username,password,imagePath) VALUES  ("{}","{}","{}","{}","{}")'.format(name,surname,username,password,imagePath)
        imlec.execute(command)
        vt.commit()
        vt.close()
        print("{}  has been successfully added to Pharmacist".format(name))
    except:
        print("An Error current Add Pharmacist")
