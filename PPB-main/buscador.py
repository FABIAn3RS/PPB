import tkinter as tk
import mysql.connector as msqlc
from tkinter import ttk


class buscador:
    def __init__(self, vent):
        self.ventana = tk.Toplevel()
        self.ventana.geometry("1600x400")
        self.ventana.title("Buscador")
        self.vent = vent
        self.conexion = msqlc.connect(
            host="maglev.proxy.rlwy.net",
            port=59637,
            user="usuario_app",
            password="123",
            database="new_schema"
        )

    def buscar_empresa(self):

        
        # Implementar la lógica para buscar empresas
        etiqueta_buscar = tk.Label(self.ventana, text="Buscar Practicas por Empresa")
        etiqueta_buscar.pack()

        campo_buscar = tk.Entry(self.ventana)
        campo_buscar.pack()

        def buscar_por_empresas():

            for item in tree_empresas.get_children():
                tree_empresas.delete(item)

            empresa = campo_buscar.get()
            cursor = self.conexion.cursor()
            query = "SELECT * FROM  PracticasGLOBAL_con_estado  WHERE empresa LIKE %s"
            datos = (empresa,)
            cursor.execute(query, datos)
            resultados = cursor.fetchall()
            print(resultados)
            cursor.close()

            for fila in resultados:
                tree_empresas.insert("", tk.END, values=fila)


        boton_buscar = tk.Button(self.ventana, text="Buscar", command=buscar_por_empresas)
        boton_buscar.pack()

        columnas = ("ID", "Nombre", "Cedula", "Empresa", "Horas", "Fecha", "Descripción", "Estado", "Tutor")
        tree_empresas = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        for col in columnas:
            tree_empresas.heading(col, text=col)
        tree_empresas.pack()


        def volver():
            self.conexion.close()
            self.vent.deiconify()
            self.ventana.destroy()

        volverb = tk.Button(self.ventana, text="volver", command=volver)
        volverb.pack()


    def buscar_estudiante(self):

        # Implementar la lógica para buscar estudiantes
        etiqueta_buscar = tk.Label(self.ventana, text="Buscar Practicas por Estudiante")
        etiqueta_buscar.pack()

        campo_buscar = tk.Entry(self.ventana)
        campo_buscar.pack()

        def buscar_por_estudiantes():

            for item in tree_estudiantes.get_children():
                tree_estudiantes.delete(item)

            nombre = campo_buscar.get()
            cursor = self.conexion.cursor()
            query = "SELECT * FROM PracticasGLOBAL_con_estado WHERE nombres_estudiante LIKE %s"
            datos = (nombre,)
            cursor.execute(query, datos)
            resultados = cursor.fetchall()
            print(resultados)
            cursor.close()

            for fila in resultados:
                tree_estudiantes.insert("", tk.END, values=fila)

            


        boton_buscar = tk.Button(self.ventana, text="Buscar", command=buscar_por_estudiantes)
        boton_buscar.pack()

        columnas = ("ID", "Nombre", "Cedula", "Empresa", "Horas", "Fecha", "Descripción", "Estado", "Tutor")
        tree_estudiantes = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        for col in columnas:
            tree_estudiantes.heading(col, text=col)
        tree_estudiantes.pack()

        def volver():
            self.conexion.close()
            self.vent.deiconify()
            self.ventana.destroy()

        volverb = tk.Button(self.ventana, text="volver", command=volver)
        volverb.pack()


    def buscar_fecha(self):

        etiqueta_buscar = tk.Label(self.ventana, text="Buscar Practicas por Fecha")
        etiqueta_buscar.pack()

        campo_buscar = tk.Entry(self.ventana)
        campo_buscar.pack()

        def buscar_por_fecha():


            for item in tree_fecha.get_children():
                tree_fecha.delete(item)

            fecha = campo_buscar.get()
            cursor = self.conexion.cursor()
            query = "SELECT * FROM PracticasGLOBAL_con_estado WHERE fecha LIKE %s"
            datos = (fecha,)
            cursor.execute(query, datos)
            resultados = cursor.fetchall()
            print(resultados)
            cursor.close()

            for fila in resultados:
                tree_fecha.insert("", tk.END, values=fila)


        boton_buscar = tk.Button(self.ventana, text="Buscar", command=buscar_por_fecha)
        boton_buscar.pack()

        columnas = ("ID", "Nombre", "Cedula", "Empresa", "Horas", "Fecha", "Descripción", "Estado", "Tutor")
        tree_fecha = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        for col in columnas:
            tree_fecha.heading(col, text=col)
        tree_fecha.pack()

        def volver():
            self.conexion.close()
            self.vent.deiconify()
            self.ventana.destroy()

        volverb = tk.Button(self.ventana, text="volver", command=volver)
        volverb.pack()