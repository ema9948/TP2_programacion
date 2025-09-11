class Cancion:
    
    def __init__(self,nombre,duracion,genero):
        self.nombre =  nombre
        self.duracion = duracion
        self.genero = genero
    
    
    def obtenerNombre(self):
      return  self.nombre
  
    def obtenerDuracion(self):
        return self.duracion;
    
    def obtenerGenero(self):
        return self.genero
    