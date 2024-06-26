import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import messagebox
import sqlite3 

conn = sqlite3.connect('pmvpos.db')
print(conn)

class aggProductos(ttk.Frame):
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
    def fEliminar(sefl):
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

    
        
        frame3=tk.Tk()
        frame3 = Frame(self, bg="brown")
        frame3.place(x=379, y=0, width=620, height=500)

        #frame3 = tk.Listbox()
        #frame3.insert


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
        frame3.grid.insert("",END, text="000", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="002", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="003", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="004", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="005", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="006", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="007", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="008", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="009", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="010", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="011", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="012", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="013", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="014", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="015", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="016", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="017", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="018", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="019", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="020", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="021", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="022", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="023", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="024", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="025", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="026", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="027", values=("Camarones al ajillo","50.000")) 
        frame3.grid.insert("",END, text="028", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="029", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="030", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="031", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="032", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="033", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="034", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="035", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="036", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="037", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="038", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="039", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="040", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="041", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="042", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="043", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="044", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="045", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="046", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="047", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="048", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="049", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="050", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="051", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="052", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="053", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="054", values=("Camarones al ajillo","50.000")) 
        frame3.grid.insert("",END, text="055", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="056", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="057", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="058", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="059", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="060", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="061", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="062", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="063", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="064", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="065", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="066", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="067", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="068", values=("Camarones al ajillo","50.000"))
        frame3.grid.insert("",END, text="069", values=("Camarones al ajillo","50.000"))
        
        self.pack()
        
        

        self.mainloop()
    
           

               
#aggProductos()
           
#ID = tv.insert("",END, text="Cursos")
        #tv.insert(ID,END, text="Algebra")
        #tv.insert(ID,END, text="Cálculo")
        #tv.insert(ID,END, text="Programación")
        #tv.insert(ID,END, text="Redes")
        #tv.insert(ID,END, text="Electrónica")
        #Nombre = tv.insert("", END, text="Carreras")
        #tv.insert(Nombre, END, text="ING de sistemas")
        #tv.insert(Nombre, END, text="Administración de empresas")
        #tv.insert(Nombre, END, text="Psicología")
        #tv.insert(Nombre, END, text="Lenguas extranjeras")
        #tv.insert(Nombre, END, text="Derecho")
        #tv.insert(Nombre, END, text="Contabilidad")