import tkinter as tk
import  mysql.connector as msqlc
from tkinter import ttk
from buscador import buscador
from reporte import reportes
from tkinter import messagebox

class cordinador:
     def __init__(self,vent):

        self.ventana=tk.Toplevel()
        self.ventana.geometry("1600x1000")
        self.ventana.title("tutor")
        self.vent=vent
        self.conexion=msqlc.connect(

                   host="maglev.proxy.rlwy.net",
                    port= 59637,  
                    user="coordinador",
                    password="coordinador",
                    database="new_schema"

                )

     def campos(self):
            
           

            #FUNCION PARA CARGAR DATOS DE EMPRESAS

            def cargar_Datos_empresas():    

                tree_empresas.delete(*tree_empresas.get_children())

                try:  

                    cursor=self.conexion.cursor()
                    cursor.execute("SELECT*FROM EMPRESAS")
                    datos=cursor.fetchall()
                    
                    for fila in datos:
                        tree_empresas.insert("", tk.END, values=fila)


                except msqlc.Error as e:

                    print(e)

                cursor.close()


                

            #FUNCIONA PARA AGREGAR EMPRESAS
            def agregar_empresa():

                

                empresa_inerfaz = tk.Toplevel(self.ventana)
                empresa_inerfaz.geometry("300x200")
                empresa_inerfaz.title("Agregar Empresa")

                etiqueta_nombre = tk.Label(empresa_inerfaz, text="Nombre de la Empresa:")
                etiqueta_nombre.pack()

                campo_nombre = tk.Entry(empresa_inerfaz)
                campo_nombre.pack()

                etiqueta_tipo = tk.Label(empresa_inerfaz, text="Tipo de Empresa:")
                etiqueta_tipo.pack()

                campo_tipo = tk.Entry(empresa_inerfaz)
                campo_tipo.pack()

                etiqueta_descripcion = tk.Label(empresa_inerfaz, text="Descripción:")
                etiqueta_descripcion.pack()

                campo_descripcion = tk.Entry(empresa_inerfaz)
                campo_descripcion.pack()

                def guardar_empresa():
                    nombre = campo_nombre.get()
                    tipo = campo_tipo.get()
                    descripcion = campo_descripcion.get()



                    try:
                        cursor = self.conexion.cursor()
                        querry = """INSERT INTO EMPRESAS(nombre, tipo, descripcion)
                                    VALUES (%s, %s, %s)"""
                        datos = (nombre, tipo, descripcion)
                        cursor.execute(querry, datos)
                        self.conexion.commit()
                        empresa_inerfaz.destroy()
                        cargar_Datos_empresas()
                        print("Empresa agregada correctamente.")
                    except msqlc.Error as e:
                        print(f"Error al agregar la empresa: {e}")

                boton_guardar = tk.Button(empresa_inerfaz, text="Guardar", command=guardar_empresa)
                boton_guardar.pack()


            def eliminar_empresa():
                empresa_inerfaz = tk.Toplevel(self.ventana)
                empresa_inerfaz.geometry("300x200")
                empresa_inerfaz.title("Eliminar Empresa")

                etiqueta_id = tk.Label(empresa_inerfaz, text="ID de la Empresa a Eliminar:")
                etiqueta_id.pack()

                campo_id = tk.Entry(empresa_inerfaz)
                campo_id.pack()

                def eliminar():
                    id_empresa = campo_id.get()
                    try:
                        cursor = self.conexion.cursor()
                        querry = "DELETE FROM EMPRESAS WHERE id_empresa = %s"
                        datos = (id_empresa,)
                        cursor.execute(querry, datos)
                        self.conexion.commit()
                        empresa_inerfaz.destroy()
                        cargar_Datos_empresas()
                        messagebox.showinfo("Éxito", "Empresa eliminada correctamente.")
                    except msqlc.Error as e:
                        messagebox.showerror("Error", f"Error al eliminar la empresa: {e}")

                boton_eliminar = tk.Button(empresa_inerfaz, text="Eliminar", command=eliminar)
                boton_eliminar.pack()

            #FUNCION PARA CARGAR DATOS DE TUTORES

            def cargar_datos_tutores():

                tree_tutores.delete(*tree_tutores.get_children())


                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM Nombres_tutores")
                datos = cursor.fetchall()
                for fila in datos:
                    tree_tutores.insert("", tk.END, values=fila)
                cursor.close()


            def agregar_tutor():
 

                tutor_inerfaz = tk.Toplevel(self.ventana)
                tutor_inerfaz.geometry("300x200")
                tutor_inerfaz.title("Agregar Tutor")

                etiqueta_nombre = tk.Label(tutor_inerfaz, text="Nombre del Tutor:")
                etiqueta_nombre.pack()

                campo_nombre = tk.Entry(tutor_inerfaz)
                campo_nombre.pack()

                etiqueta_apellido = tk.Label(tutor_inerfaz, text="Apellido del Tutor:")
                etiqueta_apellido.pack()

                campo_apellido = tk.Entry(tutor_inerfaz)
                campo_apellido.pack()

                etiqueta_correo = tk.Label(tutor_inerfaz, text="Correo del Tutor:")
                etiqueta_correo.pack()

                campo_correo = tk.Entry(tutor_inerfaz)
                campo_correo.pack()

                etiqueta_telefono = tk.Label(tutor_inerfaz, text="Teléfono del Tutor:")
                etiqueta_telefono.pack()

                campo_telefono = tk.Entry(tutor_inerfaz)
                campo_telefono.pack()

                etiqueta_cedula = tk.Label(tutor_inerfaz, text="Cédula del Tutor:")
                etiqueta_cedula.pack()

                campo_cedula = tk.Entry(tutor_inerfaz)
                campo_cedula.pack()

                def guardar_tutor():
                    nombre = campo_nombre.get()
                    apellido = campo_apellido.get()
                    correo = campo_correo.get()
                    telefono = campo_telefono.get()
                    cedula = campo_cedula.get()

                    try:
                        cursor = self.conexion.cursor()
                        querry = """INSERT INTO TUTORES(nombre, apellido, correo, telefono, cedula)
                                    VALUES (%s, %s, %s, %s, %s)"""
                        datos = (nombre, apellido, correo, telefono, cedula)
                        cursor.execute(querry, datos)
                        self.conexion.commit()
                        tutor_inerfaz.destroy()
                        cargar_datos_tutores()
                        messagebox.showinfo("Éxito", "Tutor agregado correctamente.")
                    except msqlc.Error as e:
                        messagebox.showerror("Error", f"Error al agregar el tutor: {e}")

                boton_guardar = tk.Button(tutor_inerfaz, text="Guardar", command=guardar_tutor)
                boton_guardar.pack()

            def eliminar_tutor():
                tutor_inerfaz = tk.Toplevel(self.ventana)
                tutor_inerfaz.geometry("300x200")
                tutor_inerfaz.title("Eliminar Tutor")

                etiqueta_id = tk.Label(tutor_inerfaz, text="cedula del Tutor a Eliminar:")
                etiqueta_id.pack()

                campo_id = tk.Entry(tutor_inerfaz)
                campo_id.pack()

                def eliminar():
                    id_tutor = campo_id.get()
                    try:
                        cursor = self.conexion.cursor()
                        querry = "DELETE FROM TUTORES WHERE cedula = %s"
                        datos = (id_tutor,)
                        cursor.execute(querry, datos)
                        self.conexion.commit()
                        tutor_inerfaz.destroy()
                        cargar_datos_tutores()
                        messagebox.showinfo("Éxito", "Tutor eliminado correctamente.")
                    except msqlc.Error as e:
                        messagebox.showerror("Error", f"Error al eliminar el tutor: {e}")

                boton_eliminar = tk.Button(tutor_inerfaz, text="Eliminar", command=eliminar)
                boton_eliminar.pack()

            def cargar_datos_estudiantes():


                tree_estudiantes.delete(*tree_estudiantes.get_children())


                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM Nombres_estudiantes")
                datos = cursor.fetchall()
                for fila in datos:
                    tree_estudiantes.insert("", tk.END, values=fila)
                cursor.close()


            def agregar_estudiante():

                estudiante_inerfaz = tk.Toplevel(self.ventana)
                estudiante_inerfaz.geometry("300x200")
                estudiante_inerfaz.title("Agregar Estudiante")

                etiqueta_nombre = tk.Label(estudiante_inerfaz, text="Nombre del Estudiante:")
                etiqueta_nombre.pack()

                campo_nombre = tk.Entry(estudiante_inerfaz)
                campo_nombre.pack()
                

                etiqueta_apellido = tk.Label(estudiante_inerfaz, text="Apellido del Estudiante:")
                etiqueta_apellido.pack()

                campo_apellido = tk.Entry(estudiante_inerfaz)
                campo_apellido.pack()

                etiqueta_carrera = tk.Label(estudiante_inerfaz, text="Carrera del Estudiante:")
                etiqueta_carrera.pack()

                campo_carrera = tk.Entry(estudiante_inerfaz)
                campo_carrera.pack()

                etiqueta_nacimiento = tk.Label(estudiante_inerfaz, text="Fecha de Nacimiento:")
                etiqueta_nacimiento.pack()

                campo_nacimiento = tk.Entry(estudiante_inerfaz)
                campo_nacimiento.pack()

                etiqueta_cedula = tk.Label(estudiante_inerfaz, text="Cédula del Estudiante:")
                etiqueta_cedula.pack()

                campo_cedula = tk.Entry(estudiante_inerfaz)
                campo_cedula.pack()



                def guardar_estudiante():
                    nombre = campo_nombre.get()
                    apellido = campo_apellido.get()
                    carrera = campo_carrera .get()
                    nacimiento = campo_nacimiento.get()
                    cedula = campo_cedula.get()

                    try:
                        cursor = self.conexion.cursor()
                        querry = """INSERT INTO ESTUDIANTES(nombre, apellido, carrera, nacimiento, cedula)
                                    VALUES (%s, %s, %s, %s, %s)"""
                        datos = (nombre, apellido, carrera, nacimiento, cedula)
                        cursor.execute(querry, datos)
                        self.conexion.commit()
                        estudiante_inerfaz.destroy()
                        cargar_datos_estudiantes()
                        messagebox.showinfo("Éxito", "Estudiante agregado correctamente.")
                    except msqlc.Error as e:
                        messagebox.showerror("Error", f"Error al agregar el estudiante: {e}")

                boton_guardar = tk.Button(estudiante_inerfaz, text="Guardar", command=guardar_estudiante)
                boton_guardar.pack()

            def eliminar_estudiante():
                estudiante_inerfaz = tk.Toplevel(self.ventana)
                estudiante_inerfaz.geometry("300x200")
                estudiante_inerfaz.title("Eliminar Estudiante")

                etiqueta_id = tk.Label(estudiante_inerfaz, text="Cédula del Estudiante a Eliminar:")
                etiqueta_id.pack()

                campo_id = tk.Entry(estudiante_inerfaz)
                campo_id.pack()

                def eliminar():
                    id_estudiante = campo_id.get()
                    try:
                        cursor = self.conexion.cursor()
                        querry = "DELETE FROM ESTUDIANTES WHERE cedula = %s"
                        datos = (id_estudiante,)
                        cursor.execute(querry, datos)
                        self.conexion.commit()
                        estudiante_inerfaz.destroy()
                        cargar_datos_estudiantes()
                        messagebox.showinfo("Éxito", "Estudiante eliminado correctamente.")
                    except msqlc.Error as e:
                        messagebox.showerror("Error", f"Error al eliminar el estudiante: {e}")

                boton_eliminar = tk.Button(estudiante_inerfaz, text="Eliminar", command=eliminar)
                boton_eliminar.pack()

           #eTIQUETA EMPRESAS

            etiqueta_nombre=tk.Label(self.ventana,text="EMPRESAS")
            etiqueta_nombre.pack()
           
            #TABLA EMPRESAS

            columnas = ("ID","NOMBRE","Tipo","Descripcion")
            tree_empresas = ttk.Treeview(self.ventana, columns=columnas, show="headings")
            for col in columnas:
                tree_empresas.heading(col, text=col)
            cargar_Datos_empresas()
            tree_empresas.pack()

            # BOTON PARA AGREGAR EMPRESAS

            boton_agregar_empresa = tk.Button(self.ventana, text="AGREGAR EMPRESA", command=agregar_empresa)
            boton_agregar_empresa.pack()

            #boton para eliminar empresa
            
            boton_eliminar_empresa = tk.Button(self.ventana, text="ELIMINAR EMPRESA", command=eliminar_empresa)
            boton_eliminar_empresa.pack()

            

            #ETIQUETA TUTORES
            etiqueta_tutores = tk.Label(self.ventana, text="Tutores")
            etiqueta_tutores.pack()

            #TABLA TUTORES
            columnas_tutores = ("ID", "Nombres", "Correo", "Telefono", "Cedula")
            tree_tutores = ttk.Treeview(self.ventana, columns=columnas_tutores, show="headings")
            for col in columnas_tutores:
                tree_tutores.heading(col, text=col)
            cargar_datos_tutores()
            tree_tutores.pack()

            # BOTON PARA AGREGAR TUTORES
            boton_agregar_tutor = tk.Button(self.ventana, text="AGREGAR TUTOR", command=agregar_tutor)
            boton_agregar_tutor.pack()

            # BOTON PARA ELIMINAR TUTORES
            boton_eliminar_tutor = tk.Button(self.ventana, text="ELIMINAR TUTOR", command=eliminar_tutor)
            boton_eliminar_tutor.pack()



            #ETIQUETA ESTUDIANTES

            etiqueta_estudiantes = tk.Label(self.ventana, text="Estudiantes")
            etiqueta_estudiantes.pack()

            #TABLA ESTUDIANTES
            columnas_estudiantes = ("ID", "Nombre", "Carrera", "Nacimiento", "Cedula")
            tree_estudiantes = ttk.Treeview(self.ventana, columns=columnas_estudiantes, show="headings")
            for col in columnas_estudiantes:
                tree_estudiantes.heading(col, text=col)
            cargar_datos_estudiantes()
            tree_estudiantes.pack()

            # BOTON PARA AGREGAR ESTUDIANTES
            boton_agregar_estudiante = tk.Button(self.ventana, text="AGREGAR ESTUDIANTE", command=agregar_estudiante)
            boton_agregar_estudiante.pack()


            # BOTON PARA ELIMINAR ESTUDIANTES
            boton_eliminar_estudiante = tk.Button(self.ventana, text="ELIMINAR ESTUDIANTE", command=eliminar_estudiante)
            boton_eliminar_estudiante.pack()    

            #BOTON PARA BUSQUEDA DE PRACTICAS

         
            boton_buscar_por_empresa = tk.Button(self.ventana, text="BUSCAR POR EMPRESA", command=lambda: buscador(self.ventana).buscar_empresa())
            boton_buscar_por_empresa.pack(side=tk.BOTTOM, anchor=tk.W)

            boton_buscar_por_estudiante = tk.Button(self.ventana, text="BUSCAR POR ESTUDIANTE", command=lambda: buscador(self.ventana).buscar_estudiante())
            boton_buscar_por_estudiante.pack(side=tk.BOTTOM, anchor=tk.W)

            boton_buscar_por_fecha = tk.Button(self.ventana, text="BUSCAR POR FECHA", command=lambda: buscador(self.ventana).buscar_fecha())
            boton_buscar_por_fecha.pack(side=tk.BOTTOM, anchor=tk.W)

            boton_buscar_por_estudiante = tk.Button(self.ventana, text="BUSCAR   ESTUDIANTE", command=lambda: buscador(self.ventana).buscar_estudiante_por_cedula())
            boton_buscar_por_estudiante.pack(side=tk.BOTTOM, anchor=tk.E)


            boton_generar_reporte = tk.Button(self.ventana, text="GENERAR REPORTE", command=lambda: reportes(self.ventana).generar_reporte())
            boton_generar_reporte.pack(side=tk.BOTTOM, anchor=tk.E)



            #boton para volver

            def volver():
                self.conexion.close()
                self.vent.deiconify()
                self.ventana.destroy()
                
            volverb=tk.Button(self.ventana,text="volver",command=volver)
            volverb.pack()



