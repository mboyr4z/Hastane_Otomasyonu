
import sqlite3 as sql
def f_AddAppointment(patient_id,doctor_id,profession,day,confirm,success,ui):
    try:
        print(patient_id,doctor_id,profession,day,confirm,success,ui)
        db = sql.connect("Database/database.db")
        cursor = db.cursor()
        print(patient_id, doctor_id, profession, day, confirm, success, ui)
        try:
            maxID = cursor.execute("SELECT id FROM appointment WHERE id=(SELECT max(id) FROM appointment)").fetchall()[0][0]
            print(patient_id, doctor_id, profession, day, confirm, success, ui)
            ui.txt_output.append("Added Appo. ")
        except:
            maxID = 0
        cursor.execute('INSERT INTO appointment (id,patient_id,doctor_id,profession,day,confirm,success) VALUES ({},{},{},"{}","{}",{},{})'.format(maxID+1,patient_id,doctor_id,profession,day,confirm,success))
        print(patient_id, doctor_id, profession, day, confirm, success, ui)
        db.commit()
        db.close()

    except:
        ui.txt_output.append("Err DB. Add")