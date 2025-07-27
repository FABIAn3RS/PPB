import tkinter as tk
import  mysql.connector as msqlc
from tkinter import ttk




class tutor:

    def __init__(self,vent):

        self.ventana=tk.Toplevel()
        self.ventana.geometry("1600x500")
        self.ventana.title("tutor")
        self.vent=vent
        self.conexion=msqlc.connect(

                    host="maglev.proxy.rlwy.net",
                    port= 59637,  
                    user="root",
                    password="XTYDQGTzDpJjBcGyChGTybLHiJbfFUac",
                    database="railway"

                )



    def tablas(self):

        def cargar_datos():

            try:  

                cursor=self.conexion.cursor()
                cursor.execute("SELECT*FROM practicas")
                datos=cursor.fetchall()
                
                for fila in datos:
                 tree.insert("", tk.END, values=fila)


            except msqlc.Error as e:

                print(e)

        columnas = ("ID", "Nombre", "Empresa", "Horas", "Feha", "Descripción","Estado")
        tree = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        for col in columnas:
            tree.heading(col, text=col)
        cargar_datos()
        tree.pack()

       
