import tkinter as tk
import  mysql.connector as msqlc
from tkinter import messagebox
from tkinter import ttk



class alumno():

    def __init__(self,vent):
        
        self.ventana=tk.Toplevel()
        self.ventana.geometry("300x600")
        self.ventana.title("Formulario de Practicas")
        self.vent=vent
        self.conexion=msqlc.connect(

                    host="maglev.proxy.rlwy.net",
                    port= 59637,  
                    user="usuario_app",
                    password="123",
                    database="new_schema"

                )

    def campos(self):

        #campo cedula

        etiqueta_cedula=tk.Label(self.ventana,text="cedula")
        etiqueta_cedula.pack()

        campo_cedula=tk.Entry(self.ventana)
        campo_cedula.pack()

        #campo fecha

        etiqueta_fecha=tk.Label(self.ventana,text="FECHA(YYYY-MM-DD)")
        etiqueta_fecha.pack()

        campo_fecha=tk.Entry(self.ventana)
        campo_fecha.pack()

        #CAMPO EMPRESA

        etiqueta_empresa=tk.Label(self.ventana,text="EMPRESA")
        etiqueta_empresa.pack()

        def datos_empresas():
            cursor = self.conexion.cursor()
            cursor.execute("SELECT nombre FROM EMPRESAS")
            resultados = [fila[0] for fila in cursor.fetchall()]
            cursor.close()
            return resultados
        

        combo_empresas = ttk.Combobox(self.ventana, width=40)
        combo_empresas.pack()

        opciones = datos_empresas()
        print(opciones)
        combo_empresas['values'] = opciones




        #campo horas

        etiqueta_horas=tk.Label(self.ventana,text="HORAS REALIZADAS(INT)")
        etiqueta_horas.pack()
        campo_horas=tk.Entry(self.ventana)
        campo_horas.pack()


        #campo descripcion

        etiqueta_descrip=tk.Label(self.ventana,text="DESCRIPCION")
        etiqueta_descrip.pack()

        campo_descrip=tk.Entry(self.ventana)
        campo_descrip.pack()

        #campo tutor

        etiqueta_tutor=tk.Label(self.ventana,text="TUTOR")
        etiqueta_tutor.pack()
       
        def datos_tutores():
            cursor = self.conexion.cursor()
            cursor.execute("SELECT nombre_tutor FROM  Nombres_tutores")
            resultados = [fila[0] for fila in cursor.fetchall()]
            cursor.close()
            return resultados
        
        campo_tutor = ttk.Combobox(self.ventana, width=40)
        campo_tutor.pack()

        opciones = datos_tutores()
        print(opciones)
        campo_tutor['values'] = opciones

        #boton

        def mandar():
            cedula=campo_cedula.get()
            fecha=campo_fecha.get()
            empresa=combo_empresas.get()
            hora=campo_horas.get()
            descrip=campo_descrip.get()
            tutor=campo_tutor.get()

            try:

                
                cursor = self.conexion.cursor()

                # Obtener ID de empresa
                cursor.execute("SELECT id_empresa FROM EMPRESAS WHERE nombre = %s", (empresa,))
                id_empresa = cursor.fetchone()
                if not id_empresa:
                    raise messagebox.showerror('error','Empresa no encontrada')
                id_empresa = id_empresa[0]

                # Obtener ID del tutor
                cursor.execute("SELECT id_tutor FROM  Nombres_tutores WHERE nombre_tutor = %s", (tutor,))
                id_tutor = cursor.fetchone()
                if not id_tutor:
                    raise messagebox.showerror('error',"Tutor no encontrado")
                id_tutor = id_tutor[0]

                # Obtener ID del estudiante
                cursor.execute("SELECT id_estudiante FROM ESTUDIANTES WHERE cedula = %s", (cedula,))
                id_estudiante = cursor.fetchone()
                if not id_estudiante:
                    raise messagebox.showerror('error',"estudiante no encontrado")
                id_estudiante = id_estudiante[0]

                query = """
                            INSERT INTO PRACTICAS (id_estudiante, id_empresa, fecha, horas, descripcion, id_tutor)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            """

                datos = (id_estudiante, id_empresa, fecha, hora, descrip, id_tutor)
                cursor.execute(query, datos)
                self.conexion.commit()


            except msqlc.Error as e :

                messagebox.showerror("error",e)

            self.ventana.destroy()
            self.vent.deiconify()


        guardar=tk.Button(self.ventana,text="guardar",command=mandar)
        guardar.pack()


        def volver():
            self.conexion.close()
            self.vent.deiconify()
            self.ventana.destroy()
            
        volverb=tk.Button(self.ventana,text="volver",command=volver)
        volverb.pack()

       
    

