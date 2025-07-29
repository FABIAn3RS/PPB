
class Servicios_Uuser:

    def __init__(self, claseUsers,claseHorarios,claseRutas,clasePuntos):

        self.users=claseUsers
        self.horario=claseHorarios
        self.rutas=claseRutas
        self.puntos=clasePuntos

     #METODOS PARA LOS USUARIOS   

    def crear_usuario(self, nombre, contraseña):

        usuario = self.users(nombre, contraseña)
        usuario.guardar()

    def eliminar_usuario(self, nombre, contraseña):
        usuario = self.users(nombre, contraseña)
        usuario.eliminar()


    def leer_usuarios(self):
        pass

#METODOS PARA LOS PUNTOS

    def crear_puntos(self,nombre,coodenada):
        punto=self.puntos(nombre,coodenada)
        punto.guardar()

    def eliminar_puntos(self,nombre,coodenada):
        punto=self.puntos(nombre,coodenada)
        punto.eliminar()

    def mostrar_puntos(self,nombre,coodenada):
         punto=self.puntos(nombre,coodenada)
         return punto.leer()
    
    #METODOS PARA LAS RUTAS  


    def crear_rutas(self,nombre):

        ruta=self.rutas(nombre)

        ruta.guardar()


    def eliminar_rutas(self,nombre):
     
         ruta=self.rutas(nombre)

         ruta.eliminar()


    def leer_rutas(self,nombre):

        
         ruta=self.rutas(nombre)

         return ruta.leer()

    # HORARIO

    def crear_horario(self,nombre,horario):

        hora=self.horario(nombre,horario)
        hora.guardar()

    def eliminar_horario(self,nombre,horario):
        hora=self.horario(nombre,horario)
        hora.eliminar()

    def leer_horario(self,nombre,horario):
         hora=self.horario(nombre,horario)
         return hora.leer()
    
    def leer_horario_especifico(self,nombre,horario):

        hora=self.horario(nombre,horario)

        return hora.leer_horario_especifico()






        












