import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import messagebox
import sqlite3 

conn = sqlite3.connect('pmvpos.db')
print(conn)

class Inventario (ttk.Frame):
    def __init__ (self, master=None):
        super().__init__(master, width=1000, height=680)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def feditar(self):
        pass
    def fguardar(self):
        pass
    def eliminar(self):
        pass
    def fbuscar(self):
        pass


    def create_widgets (self):
    #recuadro primero
        frame1= Frame(self, bg="green")
        frame1.place(x=10, y=10, width=950, height=100 )

        self.boton = Button(self, text="")


        #botones editar, guardar, eliminar

        lbl1 =Label(frame1, text="BUSCAR:")
        lbl1.place(x=10, y=5)
        self.txtID=Entry(frame1)
        self.txtID.place(x=3, y=26, width=250, height=30)
        #boton buscar 
        self.btnNuevo = Button(self, command=self.fbuscar, fg="white", )
        self.btnNuevo.place(x=260, y=36, width=30, height=30)

        self.pack()

        self.mainloop()
Inventario()

