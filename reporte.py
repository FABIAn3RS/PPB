import tkinter as tk
import mysql.connector as msqlc
from tkinter import ttk

class reportes:

    def __init__(self, vent):
        self.ventana = tk.Toplevel()
        self.ventana.geometry("400x400")
        self.ventana.title("Reportes")
        self.vent = vent
        self.conexion = msqlc.connect(
            host="maglev.proxy.rlwy.net",
            port=59637,
            user="root",
            password="XTYDQGTzDpJjBcGyChGTybLHiJbfFUac",
            database="new_schema"
        )

    def generar_reporte(self):

        etiqueta_reporte = tk.Label(self.ventana, text="Generar Reporte de Practicas")
        etiqueta_reporte.pack()

        caja_texto = tk.Text(self.ventana, height=10, width=50)
        caja_texto.pack(pady=10)



        # Insertar datos en la TextBox
        



        def buscar_datos():

            caja_texto.delete('1.0', tk.END)


            nombre= buscador.get()
            cursor = self.conexion.cursor()

            #HORAS TOTALES

            query = "SELECT sum(horas) from Practicasaprobadas WHERE nombre LIKE  %s"
            datos = (nombre,)
            cursor.execute(query, datos)
            total_horas = cursor.fetchall()
            print(total_horas)

            #PRACTICS REALIZADAS
            query2 = "SELECT count(*) from Practicasaprobadas WHERE nombre LIKE  %s"
            cursor.execute(query2, datos)
            total_practicas = cursor.fetchall()
            print(total_practicas)

            caja_texto.insert(tk.END, datos)
            caja_texto.insert(tk.END, f"\nTotal Horas: {total_horas[0][0]}\nTotal Practicas: {total_practicas[0][0]}")



        datos = "Nombre: Carlos Ramírez\nHoras: 150\nEmpresa: Tech Solutions"
      
        buscador=tk.Entry(self.ventana)
        buscador.pack(pady=10)

        buscador_button = tk.Button(self.ventana, text="Buscar", command=buscar_datos)
        buscador_button.pack(pady=10)




    

 