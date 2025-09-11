import math

class Circulo:
    pi:float = math.pi
    
    def __init__(self,radio:float):
        self.radio = radio
        
        
    def estrablecerRadio(self,radio:float):
        self.radio = radio;
    
    def obtenerRadio(self):
        return self.radio
    
    def obterDiametro(self):
        return self.radio*2
    
    def obtenerArea(self):
        #return math.pi * (self.radio **2)
        return self.pi * (self.radio **2)
    
    def obtenerPerimetro(self):
        #return 2 * math.pi * self.radio
        return 2 * self.pi * self.radio
    
    
    
    