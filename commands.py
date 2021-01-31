import sqlite3
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as mb

ids = {}


def fulling(on, memid):
    ids[on] = memid


def result(g_id):
    if g_id == 0:
        adding()
    elif g_id == 1:
        finding()


def adding():

    name = ids["entry_name"].get()
    surname = ids["entry_surname"].get()
    patronymic = ids["entry_patronymic"].get()
    phone = ids["entry_phone"].get()
    email = ids["entry_e-mail"].get()
    note = ids["entry_note"].get()
    if name and phone:
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        cursor.execute("INSERT INTO 'book' VALUES (?, ?, ?, ?, ?, ?)", (
            name, surname, patronymic, phone, email, note))
        db.commit()
        db.close()

    for i in list(ids.keys()):
        ids[i].delete(0, END)


def finding():
    name = ids["entry_name"].get()
    surname = ids["entry_surname"].get()
    patronymic = ids["entry_patronymic"].get()
    phone = ids["entry_phone"].get()
    email = ids["entry_e-mail"].get()
    note = ids["entry_note"].get()
    checker = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: []
    }
    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    for i in cursor.execute("SELECT * FROM book"):
        points = 0
        if (name in i[0] and name != "") :
            points += 1
        elif (surname in i[1] and surname != ""):
            points += 1
        elif (patronymic in i[2] and patronymic != ""):
            points += 1
        elif (phone in i[3] and phone != ""):
            points += 1
        elif (email in i[4] and email != ""):
            points += 1
        elif (note in i[5] and note != "") :
            points += 1
        checker[points].append(
            f"{i[1]} {i[0]} {i[2]}\nPhone:  {i[3]}\nE-mail:  {i[4]}\nNote:  {i[5]}")

    ans = checker[6] + checker[5] + checker[4] + \
        checker[3] + checker[2] + checker[1]
    ans = ans[:3]
    answer_string = ""
    for i in ans:
        answer_string += i + "\n\n"
    if answer_string == "":
        answer_string = "Eeee tut pusto k sozhaleniyu" 
    mb.showinfo("Result", answer_string)
    db.close()
