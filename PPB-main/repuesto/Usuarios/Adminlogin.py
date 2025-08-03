 
class Administrador ( ):

    def __init__(self, id, contraseña):
        self.id = id
        self.contraseña = contraseña
        
    def entrar(self):
               
        #CUERPO PRINCIPAL solo comprueba si la clave y el valor coinciden

        usuarios={}

        id = self.id.strip()
        contraseña= self.contraseña.strip()

        with open('Data/usuarios.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()
               
                if ':' in linea:
                        
                    clave, valor = linea.split(':', 1)
                    usuarios[clave.strip()] = valor.strip()

            if id  in usuarios and contraseña==usuarios[id]:

                return True

            else: 

                #envia un valor para axtualizar la info de lo que dice la ventana de login

                print('no encuentra')    
                return False
               
                #esta clase solo tiene una funcion, por eso esta al final, porque es la unica que se ejecuta siempre 
