from alumno import alumno as al
from tutor import tutor as tt
from coordinador import cordinador as cordinador   
import tkinter as tk
from PIL import Image, ImageTk


class login:


    def __init__(self):
        
        self.ventana=tk.Tk()
        self.ventana.geometry("900x900")
        self.ventana.title("inico")
        self.fondo=None

    def botones(self):

        imagen = Image.open("fondos.jpg")  # Puedes usar .png también

        # Redimensionar si es necesario
        imagen = imagen.resize((900, 950))

        # Convertir para tkinter
        self.fondo = ImageTk.PhotoImage(imagen)


        # Mostrar en un Label
        label_imagen = tk.Label(self.ventana, image=self.fondo)
        label_imagen.place(x=0,y=0)





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
            
             
        titulo=tk.Label(self.ventana,text="SELECCIONE USUARIO",font=("Arial",30))
        titulo.pack()

        boton_estudiantes=tk.Button(self.ventana,text="ALUMNO",font=("Arial",12),command=opening1)
        boton_estudiantes.pack()

       

        boton_maestros=tk.Button(self.ventana,text="TUTOR",font=("Arial",12),command=opening2)
        boton_maestros.pack()

        boton_coordinador=tk.Button(self.ventana,text="COORDINADOR",font=("Arial",12),command=opening3)
        boton_coordinador.pack()



    def abrir_ventana(self):


        self.ventana.mainloop()
    
        


abridor=login()
abridor.botones()
abridor.abrir_ventana()