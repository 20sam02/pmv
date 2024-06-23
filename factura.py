import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import messagebox
import sqlite3 

conn = sqlite3.connect('pmvpos.db')
print(conn)

class FacturaGen (Frame):
    def __init__(self, master= None):
        super().__init__(master, width=1000, height=680)
        self.master = master
        self.pack()
        self.create_widgets()
    
    #FUNCIONES DE LOS BOTONES DEL PRIMER WIDGET
    def fanadir(self):
        pass

    def fModificar(self):
         pass
    def fEliminar(self):
         pass
    
    #FUNCIONES DE LOS BOTONES DEL SEGUNDO WIDGET

    def fGuardar(self):
         pass
    def fCancelar(self):
         pass
    
    def create_widgets(self):

        #primero recuadro
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=0, width=180, height= 230)

        #botones eliminar, modificar y añadir
        self.btnNuevo = Button(self, text="Añadir", command=self.fanadir, bg="blue", fg="white")
        self.btnNuevo.place(x=55, y=30, width=80, height=30)

        self.btnNuevo = Button(self, text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnNuevo.place(x=55, y=80, width=80, height=30)

        self.btnNuevo = Button(self, text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnNuevo.place(x=55, y=130, width=80, height=30)



        #segundo recuadro
        frame2 = Frame(self, bg="#74E16A")
        frame2.place(x=190, y=0, width=185, height= 230)

        #ingresar la informacion
        lbl1 =Label(frame2, text="ID:")
        lbl1.place(x=10, y=5)
        self.txtID=Entry(frame2)
        self.txtID.place(x=3, y=26, width=80, height=20)

        lbl2 =Label(frame2, text="NOMBRE:")
        lbl2.place(x=10, y=66)
        self.txtID=Entry(frame2)
        self.txtID.place(x=3, y=86, width=150, height=20)

        lbl3 =Label(frame2, text="PRECIO:")
        lbl3.place(x=10, y=126)
        self.txtID=Entry(frame2)
        self.txtID.place(x=3, y=148, width=110, height=20)


        #acciones
        self.btnGuardar = Button(frame2, text="Guardar", bg="green", fg="white", command=self.fGuardar)
        self.btnGuardar.place(x=8, y=190, width=75, height=35)

        self.btnCancelar = Button(frame2, text="Eliminar", bg="red", fg="white", command=self.fCancelar)
        self.btnCancelar.place(x=100, y=190, width=75, height=35)

        #TERCER RECUADRO
        frame3 = Frame(self, bg="brown")
        frame3.place(x=379, y=0, width=620, height=500)

        #objetos

        
        frame3.grid= ttk.Treeview(frame3, columns=("col1", "col2"))

        frame3.grid.column("#0", width=80)
        frame3.grid.column("col1", width=80, anchor=CENTER)
        frame3.grid.column("col2", width=80, anchor=CENTER)

        frame3.grid.heading("#0", text="ID", anchor=CENTER)
        frame3.grid.heading("col1", text="Nombre", anchor=CENTER)
        frame3.grid.heading("col2", text="Precio", anchor=CENTER)
        frame3.grid.place(x=0, y=0, width=620, height=500)
        
        frame3.grid.insert("",END, text="001", values=("Menú","20.000"))
     
        
        

        self.mainloop()

FacturaGen()