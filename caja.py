import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import mysql.connector
conexion = mysql.connector.connect(user='sam1', password='1234', host='localhost', database='pmvpos', port='3306')
print(conexion)

#COLORES
#FAFAFA
#EDF0F3
#182F43
class loginAdmin:
    def loginPM():
        try: 
            

            base = Tk()
            base.geometry("546x502+500+50")
            base.title("LOGIN ADMIN PLAYAMAR")
            base.resizable(width=False, height=False)
            fondo = tk.PhotoImage(file="images/login5.png")
            fondologin = tk.Label(base, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)
            #COLORES
            color_entrar = "#EDF0F3"
            color_login = "#FFFFFF"
            color_usuario="#FAFAFA"
            color_contraseña="#FFFFFF"

            usuario_login = tk.StringVar()
            pwd_login = tk.StringVar()

            #ENTRADAS

            entradauser = tk.Entry(base, textvar=usuario_login, width=30, font = ("Roboto", 13) , relief="flat", bg=color_usuario)
            entradauser.place(x=170, y=260)

            entradapwd = tk.Entry(base, textvar=pwd_login, width=30, font = ("Roboto", 13), relief="flat", bg=color_usuario, show="*")
            entradapwd.place(x= 170, y = 370)
            
            
                  

            #BOTONES
            boton = tk.Button(base, text="Entrar", cursor="hand2", bg=color_login, width=12, relief="flat", font=("Roboto", 13), command=lambda: login())
            boton.place(x=257, y=440)

            def login():
                nombre = entradauser.get()
                contraseña = entradapwd.get()

                if nombre == "admin" and contraseña == "1234":
                    programapmv()
                else:
                    tkinter.messagebox.showinfo("Error","Credenciales incorrectas")
                
            def programapmv():
                  base.withdraw()
                  paginaprincipal.pmvinter()


                  
         
        except ValueError as error:
                    print("Error al mostrar la interfaz: {}".format(error))

        base.mainloop()

class paginaprincipal:
    def pmvinter():
        try:
           
            Pbase = tk.Toplevel()
            Pbase.title("Inventario Productos")
            Pbase.geometry("1024x640+500+50")
            fondo = tk.PhotoImage(file="images/login1.png")
            fondo1 = tk.Label(Pbase, image=fondo).place(x=0, y=0, relheight=1, relwidth=1)
                        
                        
        except ValueError as error:
                    print("Error al mostrar la interfaz: {}".format(error))       

        Pbase.mainloop()  
        
loginAdmin.loginPM()            
#user = 'admin'
#pwd = '1234'

#options = ()
#print("Ingresa el usuario y contraseña")

#print("usuario: ")
#user = input(str)
#print ("contraseña")
#pwd = input(int)

#if user == user and pwd == pwd :
#    print ("credenciales correctas")
#else:
#    print("usuario o contraseña incorrecta")


#class FormularioProductos:

#base.withdraw()