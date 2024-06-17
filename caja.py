import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import mysql.connector
conexion = mysql.connector.connect(user='sam1', password='1234', host='localhost', database='pmvpos', port='3306')
print(conexion)

#COLORES
#FAFAFA

class loginAdmin:
    def loginPM():
        try: 
            base = Tk()
            base.geometry("500x280+500+50")
            base.title("LOGIN ADMIN PLAYAMAR")
            base.resizable(width=False, height=False)
            fondo = tk.PhotoImage(file="images/login.png")
            fondologin = tk.Label(base, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

            groupBox = LabelFrame()







            base.mainloop()

        except ValueError as error:
            print("Error al mostrar la interfaz: {}".format(error))

    loginPM()

user = 'admin'
pwd = '1234'

options = ()
print("Ingresa el usuario y contraseña")

print("usuario: ")
user = input(str)
print ("contraseña")
pwd = input(int)

if user == user and pwd == pwd :
    print ("credenciales correctas")
else:
    print("usuario o contraseña incorrecta")

class FormularioProductos:

    def FormularioP():

        try: 
            base = Tk()
            base.geometry("1200x300")
            base.title("Inventario Productos")

            groupBox = LabelFrame()






            base.mainloop()

        except ValueError as error:
            print("Error al mostrar la interfaz: {}".format(error))

    FormularioP()