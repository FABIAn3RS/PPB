import customtkinter as ctk
import webview
from PIL import Image, ImageTk
from Usuarios.Adminlogin import Administrador as lg
from Usuarios.administrador import administrador as AD


from Usuarios.FuncUsers import ModHorarios,ModRutas

from Usuarios.backend_Servicios import Servicios_Uuser as SU

service=SU("ModUsuario",ModHorarios,ModRutas,"ModPuntos")


import os



BASE_DIR = os.path.dirname(__file__)

class main():

    def __init__(self):

      
        self.sesion=False
        self.interruptor=False
        self.cachebotones=[]


    def abrir_ventana(self):


          # Tema y estilo general del tkinter

        ctk.set_appearance_mode("")  # "light", "dark", "system"
        ctk.set_default_color_theme("blue")

        #  ventana principal
        self.ventana = ctk.CTk()
        self.ventana.geometry("1600x880")
        self.ventana.title("Líneas de Buses")
        self.ventana.configure(fg_color="#eeeeee")
        self.ventana.resizable(False,False)

       
        # Fondo 
        imagen = Image.open("Data/NOTEP.png")
        imagen = imagen.resize((1600, 880))

        #Icono de admin
        image11 = Image.open("Data/admin.png")
        image1 = ImageTk.PhotoImage(image11.resize((70, 70)))
        imagen_tk = ImageTk.PhotoImage(imagen)
        fondo = ctk.CTkLabel(self.ventana, image=imagen_tk, text="")
        fondo.place(x=0, y=0, relwidth=1, relheight=1)







        # ventana para el login y conexión con la clase de login

        def abrirlogin():

            if self.sesion == False:

                loginvent = ctk.CTkToplevel(self.ventana)
                loginvent.title("Login")
                loginvent.geometry("300x250")
                loginvent.attributes("-topmost", True)  # Hace que la ventana esté siempre encima


                toplogin = ctk.CTkLabel(loginvent, text='Ingrese sus credenciales', font=("Arial", 14))
                toplogin.pack(pady=10)

                entuser = ctk.CTkEntry(loginvent, placeholder_text="Usuario")
                entuser.pack(pady=10)

                entcontra = ctk.CTkEntry(loginvent, placeholder_text="Contraseña", show="*")
                entcontra.pack(pady=10)

                #llama al login para verificar los datos de la ventanita

                def comprobar_datos():
                    contra = entcontra.get()
                    user = entuser.get()
                    entra = lg(user, contra)
                    resultado=entra.entrar()

                    if not resultado:
                        toplogin.configure(text="Usuario o contraseña incorrectos")
                    
                    else:
                        loginvent.destroy()
                        self.ventana.withdraw()
                        continuar=AD(user,self.ventana)
                        continuar.abrir_ventana_admin()

                        self.sesion=True

                comprobar_boton = ctk.CTkButton(loginvent, text="Comprobar", command=comprobar_datos)
                comprobar_boton.pack(pady=10)


            elif self.sesion  ==True:
                    
                    self.ventana.withdraw()
                    continuar=AD("",self.ventana)
                    continuar.abrir_ventana_admin()
            
            

             

        # una funcion para ejecutar 2 funciones en el buvle de botones

        def abrir_mapayhorario(i):

            #conexion con horarios
            def horarios(i):
                
                return service.leer_horario_especifico(i,'empty')

            # Función para abrir un mapa específico
            def abrir_mapa(numero):
                ruta = os.path.join(BASE_DIR, 'lineas', f'{numero}.html')
                x=webview.create_window(f"{numero}", ruta, width=1300, height=600)
                x.on_top=True

                webview.start()

            plantilla=horarios(i)
            x=ventana_para_horarios()
            x.configure(text=plantilla)


            
            self.ventana.after(100,abrir_mapa,i)#hace que se ejecute unos milisegundos despues para darle chance de actualizar los horarios al main
           


        # Botón para admin

        def boton_admin():
            

            boton2 = ctk.CTkButton(self.ventana, text="", fg_color="#eeeeee",width=10, image=image1, command=abrirlogin)
            boton2.place(x=30, y=40)

        # Ventana de horarios

        def ventana_para_horarios():
            
            ethorarios = ctk.CTkLabel(self.ventana, text="HORARIOS", anchor= "center", font=("Cascadia Mono", 30),width=300, text_color="#000000" ,corner_radius=30,height=50)
            ethorarios.place(x=1220, y=60)
            return ethorarios

        botones=[]

        def bucles_para_los_botones():



        # Lista de nombres de líneas

           
            lineas=service.leer_rutas('empty')

            # Crear botones para cada línea , esto estaMUY ligado a la clase de buses ya que funciona al contenido de esta

            posicionx=120
            posiciony = 150
            posicionyinicial=posiciony

            # un contador para saber cuantas rutas se encuentran en el txt y si muestra la interfaz con botones grandes o pequeños

            # el bucle tiene una funcion para abrir dos funciones a la vez

            contadorlineas=0

            for nolineas in lineas:
                contadorlineas+=1

    
            for  texto in lineas:

                if not texto:
                    continue

                nombre=texto[0].strip()

                if contadorlineas>=19:

                    #botones 
                    boton = ctk.CTkButton(
                        self.ventana,
                        text=texto,
                        width=150,
                        fg_color="#4d6e99",
                        border_width=8,
                        border_color= "#a9b6ce",
                        font=("Cascadia Mono", 10, "bold"),
                        height=30,
                        corner_radius=30,
                    # fg_color="#3347FF",
                        command=lambda nombre=nombre : abrir_mapayhorario(nombre)
                    )
                    boton.place(x=posicionx, y=posiciony)
                    botones.append(boton)

                    posiciony += 40
                    if posiciony>700:  
                        posicionx+=200
                        posiciony=posicionyinicial

                elif contadorlineas<19:

                    nombre=texto[0].strip()


                    boton = ctk.CTkButton(
                        self.ventana,
                        text=texto,
                        width=200,
                        height=60,
                        corner_radius=20,
                        fg_color="#4d6e99",
                        border_width=8,
                        border_color= "#a9b6ce",
                        font=("Cascadia Mono", 14, "bold"),
                        command=lambda nombre=nombre : abrir_mapayhorario(nombre)
                    )
                    boton.place(x=posicionx, y=posiciony)
                    botones.append(boton)


                    posiciony += 80
                    if posiciony>500:
                        posicionx+=300
                        posiciony=posicionyinicial

            return botones
        

        primera_lista= bucles_para_los_botones()



        def actualizacionbotones(primera_lista):

                def actualizar_botones(primera_lista):

                    if self.interruptor==False:

                        for boton in primera_lista:
                         boton.destroy()

                    elif self.interruptor==True:
                        
                        for boton in self.cachebotones:
                         boton.destroy()

                    lineas=service.leer_rutas('empty')
                    botones2=[]

                    # Crear botones para cada línea , esto estaMUY ligado a la clase de buses ya que funciona al contenido de esta

                    posicionx=120
                    posiciony = 150
                    posicionyinicial=posiciony

                    # un contador para saber cuantas rutas se encuentran en el txt y si muestra la interfaz con botones grandes o pequeños

                    # el bucle tiene una funcion para abrir dos funciones a la vez

                    contadorlineas=0

                    for nolineas in lineas:
                        contadorlineas+=1

            
                    for  texto in lineas:

                        if not texto:
                            continue

                        nombre=texto[0].strip()

                        if contadorlineas>=19:

                            #botones 
                            boton = ctk.CTkButton(
                                self.ventana,
                                text=texto,
                                width=150,
                                fg_color="#4d6e99",
                                border_width=8,
                                border_color= "#a9b6ce",
                                font=("Cascadia Mono", 10, "bold"),
                                height=30,
                                corner_radius=30,
                            # fg_color="#3347FF",
                                command=lambda nombre=nombre : abrir_mapayhorario(nombre)
                            )
                            boton.place(x=posicionx, y=posiciony)
                            botones2.append(boton)

                            posiciony += 40
                            if posiciony>700:
                                posicionx+=200
                                posiciony=posicionyinicial

                        elif contadorlineas<19:

                            nombre=texto[0].strip()


                            boton = ctk.CTkButton(
                                self.ventana,
                                text=texto,
                                width=200,
                                height=60,
                                corner_radius=20,
                                fg_color="#4d6e99",
                                border_width=8,
                                border_color= "#a9b6ce",
                                font=("Cascadia Mono", 14, "bold"),
                                command=lambda nombre=nombre : abrir_mapayhorario(nombre)
                            )
                            boton.place(x=posicionx, y=posiciony)
                            botones2.append(boton)


                            posiciony += 80
                            if posiciony>500:
                                posicionx+=300
                                posiciony=posicionyinicial

                    self.interruptor=True
                    self.cachebotones=botones2


                botonreset=ctk.CTkButton(self.ventana,text="actualizar",command=lambda botones_viejos= primera_lista: actualizar_botones(botones_viejos))
                botonreset.place(x=1450,y=850)
                

           


          

             
        

        actualizacionbotones(primera_lista)    
        boton_admin()
        ventana_para_horarios()



     
        


        self.ventana.mainloop()

    
   

        #Imagen adicional a la izquierda



   
if __name__ == "__main__":
    obj1 = main()
    obj1.abrir_ventana()
