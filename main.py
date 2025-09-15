'''Sección B (para entregar):''' 
import cancion
import circulo
from os import system

system('cls' if os.name == 'nt' else 'clear')

# Ejercicio 1
print('''1)  En  el  archivo  cancion.py,  generar  la clase correspondiente al siguiente 
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
''')
print("Realizado en cancion.py")
input("Presione Enter para continuar")
system('cls' if os.name == 'nt' else 'clear')

# Ejercicio 2
print('''2)  En el archivo main.py, instanciar la clase “Cancion” 3 veces.
''')
cancion1 = cancion.Cancion("Tone Loc - Funky Cold Medina", 248, "Rap") 
cancion2 = cancion.Cancion("Martin Solveig - Intoxicated", 194, "Dance")
cancion3 = cancion.Cancion("Lindsey Stirling - Carol of the Bells", 186, "Clasica")
print(f'''Se crearon 3 instancias de Cancion
    Nombre: {cancion1.obtenerNombre()}, Duracion: {cancion1.obtenerDuracion()}, Genero: {cancion1.obtenerGenero()} 
    Nombre: {cancion2.obtenerNombre()}, Duracion: {cancion2.obtenerDuracion()}, Genero: {cancion2.obtenerGenero()}
    Nombre: {cancion3.obtenerNombre()}, Duracion: {cancion3.obtenerDuracion()}, Genero: {cancion3.obtenerGenero()}

      ''')
input("Presione Enter para continuar")
system('cls' if os.name == 'nt' else 'clear')

# Ejercicio 3
print('''3)  En  el  archivo  main.py, imprimir el valor del atributo genero para cada 
instancia creada de la clase “Cancion”.
''')
print(f'''Generos
      {cancion1.obtenerGenero()} 
      {cancion2.obtenerGenero()}
      {cancion3.obtenerGenero()}''')
input("Presione Enter para continuar")
system('cls' if os.name == 'nt' else 'clear')

# Ejercicio 4
print('''4)  En el archivo main.py, modificar el valor del atributo genero de una de 
las instancias de “Cancion” e imprimir nuevamente su valor.
''')
cancion3.establecerGenero("Villancico")
print(f"Nuevo genero de {cancion3.obtenerNombre()}: {cancion3.obtenerGenero()}")
input("Presione Enter para continuar")
system('cls' if os.name == 'nt' else 'clear')

# Ejercicio 5
print('''5)  En  el  archivo  circulo.py,  generar  la  clase  correspondiente  al  siguiente 
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
obtener Radio(): float
obtener Diametro(): float
obtener Area(): float
obtener Perimetro(): float
-------------------------------

Nota: el radio está medido en centímetros 
''')
print("Realizado en circulo.py")
input("Presione Enter para continuar")
system('cls' if os.name == 'nt' else 'clear')

# Ejercicio 6
print('''6)  En el archivo main.py, instanciar la clase “Circulo” 3 veces.
''')
circulo1 = circulo.Circulo(20.0)
circulo2 = circulo.Circulo(40.0)
circulo3 = circulo.Circulo(60.0)

print(f'''Se crearon 3 instancias de la clase circulo.
      circulo 1 tiene {circulo1.obtenerRadio()} de radio
      circulo 2 tiene {circulo2.obtenerRadio()} de radio
      circulo 3 tiene {circulo3.obtenerRadio()} de radio
      ''')
input("Presione Enter para continuar")
system('cls' if os.name == 'nt' else 'clear')

# Ejercicio 7
print('''7)  En el archivo main.py, imprimir el valor del diámetro para cada instancia 
de “Circulo” creada.
''')
print(f'''
    circulo 1 tiene {circulo1.obtenerDiametro()} de diametro
    circulo 2 tiene {circulo2.obtenerDiametro()} de diametro
    circulo 3 tiene {circulo3.obtenerDiametro()} de diametro
    ''')

input("Presione Enter para continuar")
system('cls' if os.name == 'nt' else 'clear')

# Ejercicio 8
print('''8)  En  el  archivo  main.py,  imprimir  el  valor  del  atributo  PI  para  cada 
instancia de “Circulo” creada.
''')
print(f'''
    Pi en circulo1: {circulo1.PI}
    Pi en circulo2: {circulo2.PI}
    Pi en circulo3: {circulo3.PI}
    ''')
input("Presione Enter para continuar")
system('cls' if os.name == 'nt' else 'clear')

# Ejercicio 9
print('''9)  En  el  archivo main.py, crear 2 instancias más de “Circulo” que tengan 
valores  idénticos  para  el  radio,  e imprimir el resultado de compararlas 
utilizando el operador ==
''')
circulo4 = circulo.Circulo(100)
circulo5 = circulo.Circulo(100)
print(f"Al comparar los objetos con el operador == se obtiene {circulo4 == circulo5}")
input("Presione Enter para continuar")
system('cls' if os.name == 'nt' else 'clear')

# Ejercicio 10
print('''10) En el archivo main.py, imprimir el resultado de comparar los valores del 
perímetro de cada instancia creada en el punto anterior.
''')
print(f"Al comparar los perimetros de ambos objetos se obtiene {circulo4.obtenerPerimetro() == circulo5.obtenerPerimetro()}")
input("Presione Enter para finalizar")
system('cls' if os.name == 'nt' else 'clear')
