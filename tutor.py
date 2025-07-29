import tkinter as tk
import  mysql.connector as msqlc
from tkinter import ttk
from buscador import buscador




class tutor:

    def __init__(self,vent):

        self.ventana=tk.Toplevel()
        self.ventana.geometry("1600x900")
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

        #funcion para cargar datos de practicas

        def cargar_datos_practicas():

            try:  

                cursor=self.conexion.cursor()
                cursor.execute("SELECT*FROM PracticasAprobadas")
                datos=cursor.fetchall()
                
                for fila in datos:
                 tree.insert("", tk.END, values=fila)


            except msqlc.Error as e:

                print(e)


        def cargar_datos_tree2_pendiente():

            try:  

                cursor=self.conexion.cursor()
                cursor.execute("SELECT*FROM PracticasPendientes")
                datos=cursor.fetchall()
                
                for fila in datos:
                 tree2.insert("", tk.END, values=fila)


            except msqlc.Error as e:

                print(e)

        def aprobar_practica():
            entradai = entrada_id.get()
            if entradai:
                try:
                    cursor = self.conexion.cursor()
                    querry="UPDATE practicas SET ESTADO=1 WHERE idpracticas=%s"
                    datos=(entradai,)
                    cursor.execute(querry, datos)
                    self.conexion.commit()
                    print(f"Practica con ID {entradai} aprobada.")
                except msqlc.Error as e:
                    print(f"Error al aprobar la practica: {e}")
            else:
                print("Por favor, ingrese un ID válido.")
        

        def actualizar():
            for item in tree.get_children():
                tree.delete(item)
            cargar_datos_practicas()

            for item in tree2.get_children():
                tree2.delete(item)
            cargar_datos_tree2_pendiente()

        def aprobar_practica_y_actualizar():
            aprobar_practica()
            actualizar()

        #estructura de tabla de practicas

        etiqueta_tabla=tk.Label(self.ventana,text="Practicas Aprobadas")
        etiqueta_tabla.pack()


        columnas = ("ID", "Nombre", "Empresa", "Horas", "Feha", "Descripción", "Tutor")
        tree = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        for col in columnas:
            tree.heading(col, text=col)
        cargar_datos_practicas()
        tree.pack()

       #estructura de tabla de practicas pendientes

        etiqueta_tabla2=tk.Label(self.ventana,text="Practicas Pendientes")
        etiqueta_tabla2.pack()

        columnas2 = ("ID", "Nombre", "Empresa", "Horas", "Feha", "Descripción", "Tutor")
        tree2 = ttk.Treeview(self.ventana, columns=columnas2, show="headings")
        for col in columnas2:
            tree2.heading(col, text=col)
        cargar_datos_tree2_pendiente()
        tree2.pack()

        etiqueta_aprobar_practica=tk.Label(self.ventana,text="Ingrese ID para aprobar Practica")
        entrada_id=tk.Entry(self.ventana)
        etiqueta_aprobar_practica.pack()
        entrada_id.pack()

        boton_aprobar=tk.Button(self.ventana,text="Aprobar Practica",command=aprobar_practica_y_actualizar)
        boton_aprobar.pack()

        boton_buscar_por_empresa = tk.Button(self.ventana, text="BUSCAR POR EMPRESA", command=lambda: buscador(self.ventana).buscar_empresa())
        boton_buscar_por_empresa.pack(side=tk.BOTTOM, anchor=tk.W)

        boton_buscar_por_estudiante = tk.Button(self.ventana, text="BUSCAR POR ESTUDIANTE", command=lambda: buscador(self.ventana).buscar_estudiante())
        boton_buscar_por_estudiante.pack(side=tk.BOTTOM, anchor=tk.W)

        boton_buscar_por_fecha = tk.Button(self.ventana, text="BUSCAR POR FECHA", command=lambda: buscador(self.ventana).buscar_fecha())
        boton_buscar_por_fecha.pack(side=tk.BOTTOM, anchor=tk.W)

       


       #boton para volver

        def volver():
            self.conexion.close()
            self.vent.deiconify()
            self.ventana.destroy()
            
        volverb=tk.Button(self.ventana,text="volver",command=volver)
        volverb.pack()

 
       

