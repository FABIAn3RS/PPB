from Usuarios.interfaz_funciones_admin import InterfazAdmin
import os
import csv
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class ModUsuario(InterfazAdmin):

    def __init__(self,nombre,contraseña):

        self.__nombre=nombre
        self.__contraseña=contraseña
        self.direccion='Data/usuarios.txt'


    #propiedad para que no se pueda cambiar el nombre sin llamar al metodo agregar usuario

    @property
    def nombre(self):
        return self.__nombre
    
  

    #propiedad para que no se pueda cambiar la contraseña sin llamar al metodo agregar usuario
    @property
    def contraseña(self):

        return self.__contraseña
    





    def leer(self):

        print('pendiente')


    def guardar(self):

         self.__nombre = self.__nombre.strip()
         self.__contraseña=self.__contraseña.strip()

         with open(self.direccion, 'a', encoding='utf-8') as archivo:
            archivo.write(f"{self.nombre}:{self.contraseña}\n")

 
    

    def eliminar(self):

        self.__nombre = self.__nombre.strip()
        users = {}

        # Leer todos los usuarios
        with open(self.direccion, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if ':' in linea:
                    clave, valor = linea.split(':', 1)
                    users[clave.strip()] = valor.strip()

        # Eliminar el usuario
        users.pop(self.__nombre, None)

        # Guardar el nuevo diccionario
        with open(self.direccion, 'w', encoding='utf-8') as archivo:
            for clave, valor in users.items():
                archivo.write(f"{clave}:{valor}\n")



class ModPuntos(InterfazAdmin):

    

    #hereda coordenadas de la clase lugar
    def __init__(self, nombre, coordenadas):
       

        self.__nombre = nombre
        self.__coordenadas=coordenadas
        

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def coordenadas(self):
        return self.__coordenadas
    

    def guardar(self):

        carpeta=os.path.join('Data')
        archivo='info_puntos_interes.txt'
 
        

        try:
                    
                    datos={}


                    # crea la carpeta si no existe
                    if not os.path.exists(carpeta):
                        os.makedirs(carpeta)
                    
                    # hace la ruta uniendo la variable de carpeta y archivo
                    ruta_archivo = os.path.join(BASE_DIR, carpeta, archivo)
                    print(ruta_archivo)

                    # lee el archivo si existe y verifica duplicados
                    if os.path.exists(ruta_archivo):




                        with open(ruta_archivo, 'r',encoding='utf-8') as f:
                            lineas = f.readlines()

                        for linea in lineas:
                            datos = linea.strip().split(':')

                            if len(datos) >= 2:
                                nombre_existente, coordenadas_existentes= datos

                                if self.__nombre == nombre_existente or self.__coordenadas == coordenadas_existentes:
                                    raise ValueError("Ya existe un punto de interés con el mismo nombre o coordenadas.")
                                

                    # guardar el punto de interés


                    with open(ruta_archivo, 'a', encoding='utf-8') as f:
                        f.write(f"{self.__nombre}: {self.__coordenadas}\n")
                    print("Punto de interés guardado exitosamente.")


        except Exception as e:

                    print(f"Error: {e}")    



    def leer(self):
             
            carpeta=os.path.join('Data')
            archivo='info_puntos_interes.txt'
                

            ruta_archivo = os.path.join(BASE_DIR, carpeta, archivo)

            texto=""

            diccion={}

            with open(ruta_archivo, 'r', encoding='utf-8') as archivos:
             for linea in archivos:
                linea = linea.strip()
            
                if ':' in linea:
                
                    clave, valor = linea.split(':', 1)
                    clave = clave.strip()
                    valor = valor.strip()
                    diccion[clave] = valor


                for elements ,valor in diccion.items():
                    texto+=(f"Lugar: {elements} → cordenada: {valor}"+'\n'+'\n')

            return texto
         
            
    

    def eliminar(self):
            
            # crea un diccionario y lo llena con el contenido del txt , esto es para uitar rutas
            
            carpeta=os.path.join('Data')
            archivo='info_puntos_interes.txt'
         
            diccion={}

            self.__nombre=self.__nombre.strip()


            ruta_archivo = os.path.join(BASE_DIR, carpeta, archivo)


            with open(ruta_archivo, 'r', encoding='utf-8') as archivos:
             for linea in archivos:
                linea = linea.strip()
            
                if ':' in linea:
                
                    clave, valor = linea.split(':', 1)
                    clave = clave.strip()
                    valor = valor.strip()
                    diccion[clave] = valor


            diccion.pop(self.__nombre,None)
            print(self.__nombre)

            with open(ruta_archivo, 'w', encoding='utf-8') as archivos:
                    for clave, valor in diccion.items():
                        archivos.write(f"{clave}:{valor}\n")
         

        
class ModRutas(InterfazAdmin):
    
     

    def __init__(self,nombre):

        self.nombre=nombre
        self.rutas=[]
        self.direccion='Data/datosbus.csv'
             

    def guardar(self):
        
        self.nombre = self.nombre.upper()
        self.nombre=self.nombre.replace(" ", "")
        self.nombre=self.nombre.strip()
        self.nombre=self.nombre.replace(':','')
          # Normaliza el texto
        print(self.nombre)

        with open(self.direccion, mode='a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([self.nombre])  # Guarda como ['LINEA1'], etc.

        print("Dato añadido correctamente al archivo.")


    def leer(self):

       with open(self.direccion, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            self.rutas = list(lector)


            return self.rutas

    def eliminar(self):
         self.nombre = self.nombre.strip().upper()
         self.nombre=self.nombre.replace(' ','')
         nuevas_rutas = []


        # Releer archivo actualizado
         with open(self.direccion, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            self.rutas = list(lector)

            for fila in self.rutas:
                if len(fila) > 0 and fila[0].strip().upper() != self.nombre:


                 nuevas_rutas.append(fila)

            self.rutas = nuevas_rutas

         with open(self.direccion, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(self.rutas)

         print("Dato eliminado correctamente del archivo.")

        #esto por salud mental no lo voy a comentar
        

class ModHorarios(InterfazAdmin):


    def __init__(self,lineabus,horario):

        self.lineabus=lineabus
        self.horario=horario
        self.direccion='Data/datoshorarios.txt'


    def leer_horario_especifico(self):
         
         horarios={}
         
         self.lineabus = self.lineabus.strip().upper()
         

         with open(self.direccion, 'r', encoding='utf-8') as archivo:
           for linea in archivo:
             linea = linea.strip()
             
             if ':' in linea:
                  
                    clave, valor = linea.split(':', 1)
                    clave = clave.strip().upper()
                    valor = valor.strip()
                    horarios[clave] = valor

         return horarios[self.lineabus]
    

    def leer(self):
         
         horarios={}
        
         with open(self.direccion, 'r', encoding='utf-8') as archivo:
           for linea in archivo:
             linea = linea.strip()
             
             if ':' in linea:
                  
                    clave, valor = linea.split(':', 1)
                    clave = clave.strip().upper()
                    valor = valor.strip()
                    horarios[clave] = valor

           return horarios



    def guardar(self):
        str(self.lineabus)
        nombre_horario=self.lineabus
        nombre_horario=nombre_horario.strip().upper()
        nombre_horario=nombre_horario.replace(' ','')
        nombre_horario=nombre_horario.replace(':','')

        self.horario=self.horario.strip()
        self.horario=self.horario.replace(":"," ")
        

        



        with open(self.direccion, 'a', encoding='utf-8') as archivo:
                archivo.write(f"{nombre_horario}:{self.horario}\n")



    
    def eliminar(self):
      
      horarios={}


      with open(self.direccion, 'r', encoding='utf-8') as archivo:
           for linea in archivo:
             linea = linea.strip()
             
             if ':' in linea:
                  
                    clave, valor = linea.split(':', 1)
                    clave = clave.strip().upper()
                    valor = valor.strip()
                    horarios[clave] = valor

           self.lineabus=self.lineabus.strip().upper()
           self.lineabus=self.lineabus.replace(' ','')

           horarios.pop(self.lineabus,None)

      with open(self.direccion, 'w', encoding='utf-8') as archivo:
            for clave, valor in horarios.items():
                archivo.write(f"{clave}:{valor}\n")


    



if __name__ == "__main__":
    obj1 =ModUsuario()
    obj2=ModPuntos()
    obj3=ModRutas()
    obj3=ModHorarios()