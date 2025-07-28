import tkinter as tk
from tkinter import filedialog,messagebox
import shutil
import os
from Usuarios.backend_Servicios import Servicios_Uuser as SU

from Usuarios.FuncUsers import ModHorarios,ModPuntos,ModRutas,ModUsuario

import webview 


service=SU(ModUsuario,ModHorarios,ModRutas,ModPuntos)



# Carpeta donde está este archivo
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

                            

class administrador:
    # Recibe el nombre del diccionario de usuarios
    def __init__(self, nombre,ventanamain, uppdate=False, carpeta=os.path.join('Data'), archivo='info_puntos_interes.txt'):

        carpeta = os.path.abspath(carpeta)  # Esto convierte la ruta en absoluta
        self.ruta_archivo = os.path.join(carpeta, archivo)
        self.nombre=nombre
        self.uppdate=uppdate
        self.interruptor=False#tienen que ver con la act de botones
        self.cahe_boton=[]#tienen que ver con la act de botones
        self.ventanamain=ventanamain
        self.sesion=True

       

  
    
        #abre la ventana donde esta todo lo del admin

    def abrir_ventana_admin(self,):
            
            
            ventanadmin=tk.Toplevel(self.ventanamain)
            ventanadmin.geometry('1500x600')
            ventanadmin.title('ventana de admin')
            ventanadmin.resizable(False,False)

            

            #recibe el valor del nombre que va a guardar en caso de que exista y si no existe lo crea
            
            def cambiar_rutas(i):

                
                archivo_nuevo = filedialog.askopenfilename(title="Selecciona el archivo NUEVO")
                if not archivo_nuevo:
                 return
                
                
                #ruta donde busca o crea el archivo
                ruta = os.path.join(BASE_DIR, 'lineas', f'{i}.html')
                
                #recibe la ruta y el archivo que va a copiar
                try:
                     def abrir_mapa(numero):
                        ruta = os.path.join(BASE_DIR, 'lineas', f'{numero}.html')
                        x=webview.create_window(f"{numero}", ruta, width=1300, height=600)
                        x.on_top=True
                        webview.start()

                     shutil.copy2(archivo_nuevo, ruta)
                     messagebox.showinfo("Éxito", f"Archivo reemplazado:\n{os.path.basename(ruta)}")
                     abrir_mapa(i)
                    
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo reemplazar el archivo:\n{str(e)}")


            def etiqueta_nombre_Admin():
                nombrestring=str(self.nombre)
            
                textosaludo = tk.Label(ventanadmin, text="", font=("Arial", 23))
                textosaludo.configure(text='bienvenido '+nombrestring)
                textosaludo.place(anchor="center",x=200,y=20)



            def administrar_rutas():

            #boton para agregar rutas y su barra
                def ingreso_para_agreagar_rutas():

                    #concecta con la clase bus y manda las rutas nuevas y los horarios nuevos ingresados en la interfaz del tkinter
                    def agreagar_rutas():
                            ruta=entrut.get()
                            #posi=entpos.get()
                            service.crear_rutas(ruta)
                            

                            #esta parte agrega el horario a horarios

                            hora=str(enthor.get())
                            service.crear_horario(ruta,hora)
                            messagebox.showinfo('info',"La ruta ha sido creaada, reinicie para aplicar los cambios")
                            actualizar_botones(borrar)

                        
                    
                    boton1=tk.Button(ventanadmin,text='agregar ruta',font=("Arial", 11),command=agreagar_rutas)
                    boton1.place(anchor="center",x=100,y=80)

                    enthor = tk.Entry(ventanadmin)
                    enthor.place(anchor="center",x=100,y=125)
                    enthor.insert(0,"ingrese horario")

                    entrut = tk.Entry(ventanadmin)
                    entrut.place(anchor="center",x=100,y=150)
                    entrut.insert(0,'ingrese nombre de ruta')


                #boton para elimnar rutas

                def ingreso_para_quitar_rutas():

                    
                  #hace la funcion de mandar los datos de la ruta que se quiere ELIMINAR con el nombre sin ingresar el horario      


                    def quitar_rutas():
                        pos=entpos.get()
                        service.eliminar_rutas(pos)

                        #elimina el diccionario

                        service.eliminar_horario(pos,"empty")
                        messagebox.showinfo('info','La ruta ha sido borrada, reinicie para aplicar los cambios')
                        actualizar_botones(borrar)

 



                    #boton para quiatar rutas y su barra
                    
                    boton2=tk.Button(ventanadmin,text='quitar ruta',font=("Arial", 11),command=quitar_rutas)
                    boton2.place(anchor="center",x=100,y=200)

                    entpos = tk.Entry(ventanadmin, text="ingrese posicion")
                    entpos.place(anchor="center",x=100,y=250)
                    entpos.insert(0,'ingrese nombre de ruta')

                   
            
                ingreso_para_agreagar_rutas()
                ingreso_para_quitar_rutas()

        #bucle para crear botones segun el txt de las rutas y que funcionan para remplazar las rutas o crearlas si no existen, manda una lista de los botones creados para actualizarlos luego
            def bucle_generador_de_botones():





                lineas=service.leer_rutas('empty')
                botones=[]

                posx=500
                posy=60
                posyin=posy

                for  texto in lineas:

                    if not texto:
                        continue

                    nombre=texto[0].strip()

                    boton = tk.Button(
                        ventanadmin,
                        text=texto,
                        width=20,
                        height=4,
                    # fg_color="#3347FF",
                        font=("Verdana", 7),command=lambda nombre=nombre : cambiar_rutas(nombre)
                    )


                    

                    boton.place(x=posx, y=posy)
                    
                    botones.append(boton)

                    posy += 80
                    if posy>500:
                        posx+=150
                        posy=posyin

                return botones





        #bucle que actualiza los botones del administrador en tiempo real y funciona con la agregacion o eliminacion de rutas de bus, recibe una lista de los botones ya existentes para comenzar el proceso
                     
            def actualizar_botones(lista_botones):
                    

                    if self.interruptor==False:
                     

                        for boton in lista_botones:
                            boton.destroy()


                        lineas=service.leer_rutas('empty')
                        botones=[]


                        posx=500
                        posy=60
                        posyin=posy

                        for  texto in lineas:

                            if not texto:
                                continue

                            nombre=texto[0].strip()

                            boton = tk.Button(
                                ventanadmin,
                                text=texto,
                                width=20,
                                height=4,
                            # fg_color="#3347FF",
                                font=("Verdana", 7),command=lambda nombre=nombre : cambiar_rutas(nombre)
                            )

                            boton.place(x=posx, y=posy)
                            botones.append(boton)
                        

                            posy += 80
                            if posy>500:
                                posx+=150
                                posy=posyin

                        self.interruptor=True
                        self.cahe_boton=botones


                    elif self.interruptor==True:
                         

                         
                        for boton in self.cahe_boton:
                            boton.destroy()


                        lineas=service.leer_rutas('empty')
                        botones=[]


                        posx=500
                        posy=60
                        posyin=posy

                        for  texto in lineas:

                            if not texto:
                                continue

                            nombre=texto[0].strip()

                            boton = tk.Button(
                                ventanadmin,
                                text=texto,
                                width=20,
                                height=4,
                            # fg_color="#3347FF",
                                font=("Verdana", 7),command=lambda nombre=nombre : cambiar_rutas(nombre)
                            )

                            boton.place(x=posx, y=posy)
                            botones.append(boton)
                            
                        

                            posy += 80
                            if posy>500:
                                posx+=150
                                posy=posyin

                        self.cahe_boton= botones    

                        self.interruptor=True
                         

                         




#toda la ventana de administracion de usuarios y sus funciones

            def administrar_usuarios():

                def ventana_users():

                    def agregar_usuario():

                        respuesta = messagebox.askyesno("Confirmación", "¿Está seguro que quieres añadir este usuario??")

                        if respuesta:
                                x=entcontra.get()
                                s=entuser.get()
                                service.crear_usuario(s,x)
                                uservetnt.destroy()
                                ventana_users()
                        else:
                              uservetnt.destroy()
                              ventana_users()
                      
                      

                    def quitar_usuario():
                         
                          respuesta = messagebox.askyesno("Confirmación", "¿Está seguro? que quieres elminar este usuario")

                          if respuesta:
                               
                                x = entcontra.get()
                                s = entusere.get()
                                service.eliminar_usuario(s,x)
                                uservetnt.destroy()
                                ventana_users()
                          else:
                                uservetnt.destroy()
                                ventana_users()

                    # ventana de admin de susrios
                    uservetnt=tk.Toplevel(ventanadmin)
                    uservetnt.title('administrar usuarios')
                    uservetnt.geometry('300x400')
                    uservetnt.attributes('-topmost', True)
                    uservetnt.resizable(False,False)

                    #botones y barras de ingreso

                    boton2=tk.Button(uservetnt,text='Agregar usuario',font=("Arial", 11),command=agregar_usuario)
                    boton2.pack(pady=10)

                    entuser = tk.Entry(uservetnt)
                    entuser.pack(pady=10)
                    entuser.insert(0,'ingrese nombre de Usuario')

                    entcontra = tk.Entry(uservetnt)
                    entcontra.pack(pady=10)
                    entcontra.insert(0,'ingrese contraseña de Usuario')

                    boton2=tk.Button(uservetnt,text='Quitar usuario',font=("Arial", 11),command=quitar_usuario)
                    boton2.pack(pady=10)

                    entusere = tk.Entry(uservetnt)
                    entusere.pack(pady=10)
                    entusere.insert(0,'ingrese nombre de Usuario')


                boton2=tk.Button(ventanadmin,text='Administrar Usuarios',font=("Arial", 11),command=ventana_users)
                boton2.place(anchor="center",x=100,y=570)
    

    #toda la ventana de puntos de interes y sus funciones
            def administrar_puntos_interes():
                 
                 
                 def administrar_puntos_de_interes_vent():
                            
                            def agregar_punto():
                                  respuesta = messagebox.askyesno("Confirmación", "¿Está seguro que quieres añadir este punto??")

                                  if respuesta:
                                            x=entname.get()
                                            s=entcoord.get()
                                            print(x,s)
                                            service.crear_puntos(x,s)
                                            uservetnt.destroy()
                                            administrar_puntos_de_interes_vent()
                                  else:
                                        uservetnt.destroy()
                                        administrar_puntos_de_interes_vent()
                            def quitar_punto():
                                 
                                  respuesta = messagebox.askyesno("Confirmación", "¿Está seguro que quieres eliminar este punto??")

                                  if respuesta:
                                            e=entnamee.get()
                                            s=entcoord.get()
                                            print(e,s)
                                            service.eliminar_puntos(e,s)
                                            uservetnt.destroy()
                                            administrar_puntos_de_interes_vent()
                                  else:
                                        uservetnt.destroy()
                                        administrar_puntos_de_interes_vent()
                            def mostrar_puntos():
                                    
                                    mostrar=tk.Toplevel(uservetnt)
                                    mostrar.title('puntos')
                                    mostrar.geometry('1100x600')                                                            
                                    uservetnt.attributes('-topmost', True)

                                    frame_texto = tk.Frame(mostrar)
                                    frame_texto.pack(fill="both", expand=True)

                                    scrollbar = tk.Scrollbar(frame_texto)
                                    scrollbar.pack(side="right", fill="y")

                                    outputs = tk.Text(frame_texto, height=34, width=110, wrap='word', yscrollcommand=scrollbar.set)
                                    outputs.pack(side="left", fill="both", expand=True)

                                    scrollbar.config(command=outputs.yview)


                                    entrada = tk.Entry(mostrar, width=50)
                                    entrada.place(x=900,y=10)

                                    def buscar_y_resaltar():
                                        outputs.tag_remove("resaltado", "1.0", tk.END)
                                        palabra = entrada.get()
                                        if not palabra:
                                            return

                                        inicio = "1.0"
                                        while True:
                                            inicio = outputs.search(palabra, inicio, stopindex=tk.END)
                                            if not inicio:
                                                break
                                            fin = f"{inicio}+{len(palabra)}c"
                                            outputs.tag_add("resaltado", inicio, fin)
                                            inicio = fin

                                        outputs.tag_config("resaltado", background="yellow")

                                    boton = tk.Button(mostrar, text="Buscar", command=buscar_y_resaltar)
                                    boton.place(x=900,y=30)

                                    
                                    text=service.mostrar_puntos('empty','empty')
                                    outputs.insert(1.0,text)

                                   
                                 

                        
                            uservetnt=tk.Toplevel(ventanadmin)
                            uservetnt.title('administrar puntos')
                            uservetnt.geometry('300x400')
                            uservetnt.attributes('-topmost', True)
                            uservetnt.resizable(False,False)


                            boton2=tk.Button(uservetnt,text='Agregar punto',font=("Arial", 11),command=agregar_punto)
                            boton2.pack(pady=10)

                            entname = tk.Entry(uservetnt)
                            entname.pack(pady=10)
                            entname.insert(0,'ingrese nombre de punto')

                            entcoord = tk.Entry(uservetnt)
                            entcoord.pack(pady=10)
                            entcoord.insert(0,'ingrese coordenada de punto')

                            boton2=tk.Button(uservetnt,text='Quitar punto',font=("Arial", 11),command=quitar_punto)
                            boton2.pack(pady=10)

                            entnamee = tk.Entry(uservetnt)
                            entnamee.pack(pady=10)
                            entnamee.insert(0,'ingrese nombre de punto')


                            boton2=tk.Button(uservetnt,text='mostrar',font=("Arial", 11),command=mostrar_puntos)
                            boton2.pack(pady=10)



                 boton2=tk.Button(ventanadmin,text='Administrar Puntos',font=("Arial", 11),command=administrar_puntos_de_interes_vent)
                 boton2.place(anchor="center",x=300,y=570)


            def volver():
                  
                  def volver():
                       ventanadmin.destroy()
                       self.sesion=False
                       self.ventanamain.deiconify()
                       
                 
                  boton2=tk.Button(ventanadmin,text='volver',font=("Arial", 11),command=volver)
                  boton2.place(anchor="center",x=500,y=570)
                 



            def cerrar_sesion():
                  
                  def cerrar_Sesion():
                       self.ventanamain.deiconify()
                       ventanadmin.destroy()

                       from main import main
                       cierre=main()
                       cierre.sesion=False
                      


                       


                       
                 
                 
                  boton2=tk.Button(ventanadmin,text='cerrar sesion',font=("Arial", 11),command=cerrar_Sesion)
                  boton2.place(anchor="center",x=600,y=570)
                 




                 
                 



                    
            volver()
            administrar_rutas()
            borrar=bucle_generador_de_botones()#esto se manda a la funcion de acrualizar  para que comiense el proceso
            etiqueta_nombre_Admin()
            administrar_puntos_interes()
            administrar_usuarios()
         



            
                

           


           

            


