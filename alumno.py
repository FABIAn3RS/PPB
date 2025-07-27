import tkinter as tk
import  mysql.connector as msqlc
from tkinter import messagebox
from tkinter import ttk



class alumno():

    def __init__(self,vent):
        
        self.ventana=tk.Toplevel()
        self.ventana.geometry("1000x500")
        self.ventana.title("alumno")
        self.vent=vent
        self.conexion=msqlc.connect(

                    host="maglev.proxy.rlwy.net",
                    port= 59637,  
                    user="root",
                    password="XTYDQGTzDpJjBcGyChGTybLHiJbfFUac",
                    database="railway"

                )

    def campos(self):

        #campo nombre

        etiqueta_nombre=tk.Label(self.ventana,text="NOMBRES")
        etiqueta_nombre.pack()

        campo_nombre=tk.Entry(self.ventana)
        campo_nombre.pack()

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
            cursor.execute("SELECT nombre FROM empresas")
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

        #boton

        def mandar():
            nombre=campo_nombre.get()
            fecha=campo_fecha.get()
            empresa=combo_empresas.get()
            hora=campo_horas.get()
            descrip=campo_descrip.get()

            try:

                

                cursor=self.conexion.cursor()
                querry="""INSERT INTO practicas(NOMBRE,EMPRESA,FECHA,HORAS,DESCRIPCION)
                    VALUES (%s, %s, %s, %s, %s)
                """

                datos=(nombre,empresa,fecha,hora,descrip)
                cursor.execute(querry,datos)
                self.conexion.commit()

                messagebox.showinfo("exito","Datos subidos correctamente")


            except msqlc.Error as e :

                messagebox.showerror("error",e)

               


        guardar=tk.Button(self.ventana,text="guardar",command=mandar)
        guardar.pack()


        def volver():
            self.conexion.close()
            self.vent.deiconify()
            self.ventana.destroy()
            
        volverb=tk.Button(self.ventana,text="volver",command=volver)
        volverb.pack()

       
    


if __name__=="main":

    al=alumno()


"""""  ventana1=tk.Tk()

a=alumno()
a.campos()
ventana1.mainloop()
 
"""""
 