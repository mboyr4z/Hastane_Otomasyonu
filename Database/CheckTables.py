import sqlite3 as sql

def CheckTables(dbPath):
    vt = sql.connect(dbPath)
    imlec = vt.cursor()

    exist_doctor =      'CREATE TABLE IF NOT EXISTS "doctor" ("id"	INTEGER NOT NULL UNIQUE,"name"	TEXT,"surname"	TEXT,"profession"	TEXT,"username"	TEXT,"password"	TEXT,"imagePath"	TEXT,PRIMARY KEY("id" AUTOINCREMENT))'

    exist_patient =     'CREATE TABLE IF NOT EXISTS "patient" ("id"	INTEGER NOT NULL UNIQUE,"tc_id"	TEXT UNIQUE,"name"	TEXT,"surname"	TEXT,"age"	INTEGER,"gender"	INTEGER,"username"	TEXT,"password"	TEXT,"imagePath"	TEXT,PRIMARY KEY("id" AUTOINCREMENT))'

    exist_counselor =   'CREATE TABLE IF NOT EXISTS "counselor" ("id"	INTEGER NOT NULL UNIQUE,"name"	TEXT,"surname"	TEXT,"username"	TEXT,"password"	TEXT,"imagePath"	TEXT,PRIMARY KEY("id" AUTOINCREMENT))'

    exist_pharmacist =  'CREATE TABLE IF NOT EXISTS "pharmacist" ("id"	INTEGER NOT NULL UNIQUE,"name"	TEXT,"surname"	TEXT,"username"	TEXT,"password"	TEXT,"imagePath"	TEXT,PRIMARY KEY("id" AUTOINCREMENT))'

    exist_recipe =      'CREATE TABLE IF NOT EXISTS "recipe" ("id"	INTEGER NOT NULL UNIQUE,"patient_id"	INTEGER,"doctor_id"	INTEGER,"content"	TEXT,PRIMARY KEY("id" AUTOINCREMENT))'

    exist_appointment = 'CREATE TABLE IF NOT EXISTS "appointment" ("id"	INTEGER NOT NULL UNIQUE,"patient_id"	INTEGER,"doctor_id"	INTEGER,"profession"	TEXT,"day"	TEXT,"confirm"	INTEGER,"success"	INTEGER,PRIMARY KEY("id" AUTOINCREMENT))'

    imlec.execute(exist_doctor)
    imlec.execute(exist_patient)
    imlec.execute(exist_counselor)
    imlec.execute(exist_pharmacist)
    imlec.execute(exist_recipe)
    imlec.execute(exist_appointment)

    vt.commit()
    vt.close()