from alumno import alumno as al
from tutor import tutor as tt
from coordinador import cordinador as cordinador   
import tkinter as tk

class login:


    def __init__(self):
        
        self.ventana=tk.Tk()
        self.ventana.geometry("900x900")
        self.ventana.title("inico")


    def botones(self):

        def opening1():
            l=al(self.ventana)
            l.campos()
            self.ventana.withdraw()

        def opening2():
            t=tt(self.ventana)
            t.tablas()
            self.ventana.withdraw()

        def opening3():
            c=cordinador(self.ventana)
            c.campos()
            self.ventana.withdraw()
            
             
        titulo=tk.Label(self.ventana,text="SELECCIONE USUARIO",height=10)
        titulo.pack()

        boton_estudiantes=tk.Button(self.ventana,text="ALUMNO",width=50,height=10,command=opening1)
        boton_estudiantes.pack()

       

        boton_maestros=tk.Button(self.ventana,text="TUTOR",width=50,height=10,command=opening2)
        boton_maestros.pack()

        boton_coordinador=tk.Button(self.ventana,text="COORDINADOR",width=50,height=10,command=opening3)
        boton_coordinador.pack()



    def abrir_ventana(self):


        self.ventana.mainloop()
    
        


abridor=login()
abridor.botones()
abridor.abrir_ventana()