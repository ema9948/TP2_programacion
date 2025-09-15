'''1)  En  el  archivo  cancion.py,  generar  la clase correspondiente al siguiente 
diagrama: 
--------------------------------------------------------
Cancion
--------------------------------------------------------
    <<Atributos de instancia>>
nombre:string
duracion: int
genero: string
--------------------------------------------------------
    <<Constructores>>
Cancion(nombre: string, duracion: int, genero: string)
    <<Comandos>>
establecerNombre(nombre: string)
establecerDuracion(duracion: int)
establecerGenero(genero: string)
    <<Consultas>>
obtenerNombre(): string
obtenerDuracion(): int
obtenerGenero(): string
--------------------------------------------------------
      
Nota: la duración está medida en segundos 
'''


class Cancion:
# Cancion no tiene atributos de clase
    # Los atributos de clase irian aca
# Metodo de inicializacion
    def __init__(self, nombre, duracion, genero):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
# Comandos
    def establecerNombre(self, nombre):
        self.nombre = nombre
    
    def establecerDuracion(self, duracion):
        self.duracion = duracion

    def establecerGenero(self, genero):
        self.genero = genero
# Consultas
    def obtenerNombre(self):
        return self.nombre
    
    def obtenerDuracion(self):
        return self.duracion
    
    def obtenerGenero(self):
        return self.genero