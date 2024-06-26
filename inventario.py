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
    def feliminar(self):
        pass
    def fbuscar(self):
        pass


    def create_widgets (self):
    #recuadro primero
        frame1= Frame(self, bg=None)
        frame1.place(x=10, y=10, width=990, height=100 )


        self.boton = Button(self, text="")


        #botones editar, guardar, eliminar

        lbl1 =Label(frame1, text="BUSCAR:")
        lbl1.place(x=10, y=5)
        self.txtID=Entry(frame1)
        self.txtID.place(x=3, y=26, width=250, height=30)
        #boton buscar 
        self.btnNuevo = Button(self, command=self.fbuscar, fg="white", )
        self.btnNuevo.place(x=260, y=36, width=30, height=30)

        #boton modificar

        self.editBtn = Button(self, text="MODIFICAR", command=self.feditar, fg="white", bg="#C5D107")
        self.editBtn.place(x=310, y=36, width=90, height=30)
        #boton eliminar
        self.elimBtn = Button(self, text="ELIMINAR", command=self.feliminar, fg="white", bg="red")
        self.elimBtn.place(x=410, y=36, width= 90, height=30)
        #boton guardar
        self.gdarBtn = Button(self, text="GUARDAR", command=self.fguardar, fg="white", bg="green")
        self.gdarBtn.place(x=510, y=36, width=90, height=30)


        #tabla del inventario y botones

        frame2 = ttk.Frame()
        frame2 = Frame(self, bg="green")
        frame2.place(x=5, y=76, width=990, height=600)

        #tabla frame2 inventario

        frame2.grid = ttk.Treeview(frame2, columns=("col1", "col2", "col3", "col4"))
        
        frame2.grid.column("#0", width=80)
        frame2.grid.column("col1", width=80, anchor=CENTER)
        frame2.grid.column("col2", width=80, anchor=CENTER)
        frame2.grid.column("col3", width=80, anchor=CENTER)
        frame2.grid.column("col4", width=80, anchor=CENTER)

        frame2.grid.heading("#0", text="ID", anchor=CENTER)
        frame2.grid.heading("col1", text="NOMBRE", anchor=CENTER)
        frame2.grid.heading("col2", text="CANTIDAD", anchor=CENTER)
        frame2.grid.heading("col3", text="PRECIO UNITARIO", anchor=CENTER)
        frame2.grid.heading("col4", text="TOTAL", anchor=CENTER)

        frame2.grid.place(x=0, y=0, width=990, height=600)

        frame2.grid.insert("",END, text="000", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="001", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="002", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="003", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="004", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="005", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="006", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="007", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="008", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="009", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="010", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="011", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="012", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="013", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="015", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="016", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="017", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="018", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="019", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="020", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="021", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="022", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="023", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="024", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="025", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="026", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="027", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="028", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="029", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="030", values=("Camarones al ajillo","50", "50.000", "100.000" ))
        frame2.grid.insert("",END, text="031", values=("Camarones al ajillo","50", "50.000", "100.000" ))




        
        self.pack()

        self.mainloop()
Inventario()

