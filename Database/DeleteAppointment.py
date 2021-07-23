
import sqlite3 as sql
def f_DeleteAppointment(ID,ui):
    try:

        vt = sql.connect("Database/database.db")
        cursor = vt.cursor()

        cursor.execute("DELETE from appointment where id = {}".format(ID))
        try:
            ui.txt_output.append("Deleted {}".format(ID))
        except:
            pass
        vt.commit()
        vt.close()
    except:
        try:
            ui.txt_output.append("Err. Delete.")
        except:
            pass
