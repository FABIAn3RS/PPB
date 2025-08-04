import tkinter as tk
import mysql.connector as msqlc
from tkinter import ttk
from tkinter import messagebox

class reportes:

    def __init__(self, vent):
        self.ventana = tk.Toplevel()
        self.ventana.geometry("400x400")
        self.ventana.title("Reportes")
        self.vent = vent
        self.conexion = msqlc.connect(
            host="maglev.proxy.rlwy.net",
            port=59637,
            user="usuario_app",
            password="123",
            database="new_schema"
        )

    def generar_reporte(self):

        etiqueta_reporte = tk.Label(self.ventana, text="Generar Reporte de Practicas")
        etiqueta_reporte.pack()

        caja_texto = tk.Text(self.ventana, height=10, width=50)
        caja_texto.pack(pady=10)



        # Insertar datos en la TextBox
        


        def buscar_datos_Cedula():

            caja_texto.delete('1.0', tk.END)


            nombre= buscador.get()
            cursor = self.conexion.cursor()

            #HORAS TOTALES

            try:

                query = "SELECT sum(horas) from reportes WHERE cedula  = %s AND estado=1"
                datos = (nombre,)
                cursor.execute(query, datos)
                total_horas = cursor.fetchall()
                print(total_horas)

                #PRACTICS REALIZADAS
                query2 = "SELECT count(*) from reportes WHERE cedula LIKE  %s AND estado=1"
                cursor.execute(query2, datos)
                total_practicas = cursor.fetchall()
                print(total_practicas)

                #DATOS DEL ESTUDIANTE
                query_nombre = "SELECT nombre FROM reportes WHERE cedula LIKE %s"
                querr_apellido = "SELECT apellido FROM reportes WHERE cedula LIKE %s"
                cursor.execute(querr_apellido, datos)
                apellido_estudiante = cursor.fetchall() 
                cursor.execute(query_nombre, datos)
                nombre_estudiante = cursor.fetchall()
                cursor.close()

                caja_texto.insert(tk.END, datos)
                caja_texto.insert(tk.END, f"""\nNombre: {nombre_estudiante[0][0]}\nApellido: {apellido_estudiante[0][0]}\nTotal Horas: {total_horas[0][0]}\nTotal Practicas: {total_practicas[0][0]}""")

            except msqlc.Error as e:
                messagebox.showerror("Error", f"Error al buscar datos: {e}")


        def buscar_datos_Nombre():

            caja_texto.delete('1.0', tk.END)

            nombre = buscador.get()
            cursor = self.conexion.cursor()

            try:

                #HORAS TOTALES
                query = "SELECT sum(horas) from reportes WHERE nombre LIKE %s AND estado=1"
                datos = (nombre,)
                cursor.execute(query, datos)
                total_horas = cursor.fetchall()
                print(total_horas)

                #PRACTICS REALIZADAS
                query2 = "SELECT count(*) from reportes WHERE nombre LIKE %s AND estado=1"
                cursor.execute(query2, datos)
                total_practicas = cursor.fetchall()
                print(total_practicas)

                    

                caja_texto.insert(tk.END, f"\nTotal Horas: {total_horas[0][0]}\nTotal Practicas: {total_practicas[0][0]}""")

            except msqlc.Error as e:
                messagebox.showerror("Error", f"Error al buscar datos: {e}")

        datos = "Nombre: Carlos Ramírez\nHoras: 150\nEmpresa: Tech Solutions"

        buscador = tk.Entry(self.ventana)
        buscador.pack(pady=10)

        

        buscador_button = tk.Button(self.ventana, text="Buscar por Cedula", command=buscar_datos_Cedula)
        buscador_button.pack(pady=10)
 

        


    

 