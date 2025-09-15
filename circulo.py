'''5)  En  el  archivo  circulo.py,  generar  la  clase  correspondiente  al  siguiente 
diagrama: 
-------------------------------
Circulo
    <<Atributos de clase>>
PI: float
    <<Atributos de instancia>>
radio: float
-------------------------------
    <<Constructores>>
Circulo(radio: float)
    <<Comandos>>
establecerRadio(radio: float)
    <<Consultas>>
obtenerRadio(): float
obtenerDiametro(): float
obtenerArea(): float
obtenerPerimetro(): float
-------------------------------

Nota: el radio está medido en centímetros 
'''
import math

class Circulo():
# atributos de clase
    PI = math.pi
# Metodo de inicializacion
    def __init__(self, radio):
        self.radio = radio
# Comandos
    def establecerRadio(self, radio):
        self.radio = radio
# Consultas
    def obtenerRadio(self):
        return self.radio
    def obtenerDiametro(self):
        return self.radio * 2
    def obtenerArea(self):
        return self.PI * self.radio * self.radio
    def obtenerPerimetro(self):
        return self.PI * self.obtenerDiametro()