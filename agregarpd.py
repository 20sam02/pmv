import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import messagebox
import sqlite3 

conn = sqlite3.connect('pmvpos.db')
print(conn)

class aggProductos(Frame):
    def __init__(self, master= None):
        super().__init__(master, width=680, height=680)
        self.master = master
        self.pack()
        self.create_widgets()
    def fnuevo(self):
        pass
    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=0, width=180, height= 360)

        frame1 = Button(self, text="Nuevo")

        
        self.mainloop()
    def widgets(self):
           

               self.mainloop()
           
