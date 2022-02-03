import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os
import datetime


#db creat
conn = sqlite3.connect("database.db")
curs = conn.cursor()


#table creat
try:
    curs.execute("CREATE TABLE employee (name TEXT , education TEXT)")
except sqlite3.OperationalError as e:
    pass
try:
    curs.execute("CREATE TABLE cars (brand TEXT , platenumber TEXT , vintage INTEGER)")
except sqlite3.OperationalError as e:
    pass
try:
    curs.execute("CREATE TABLE inout (be DATE , ki DATE)")
except sqlite3.OperationalError as e:
    pass


#curs.execute("INSERT INTO employee VALUES ('jozsi','nemcigany')")


curs = conn.close()


root = tk.Tk()
root.geometry("1920x1080")


inp = ""
inp2 = ""
clicked = False
time = datetime.date.today()




def printInput():
    inp = e.get(1.0, "end-1c")
    inp2 = f.get(1.0, "end-1c")
    lbl.config(text="Provided Input: "+inp + " " + inp2)
    conn = sqlite3.connect("database.db")
    curs = conn.cursor()
    curs.execute("INSERT INTO employee VALUES ('Jozsi','nemcigany')")

lbl = tk.Label(root, text="")
e = tk.Text(root, height=5, width=20)
f = tk.Text(root, height=5, width=20)




e.pack()
f.pack()
button = tk.Button(root, text="OK", width=200, command=printInput)
button.pack()


#lbl = tk.Label(root, text="")
lbl.pack()
conn.close()


root.mainloop()

