from cancion import Cancion
from circulo import Circulo

print(r"""


      
██████╗ ██████╗ ██╗   ██╗██████╗  ██████╗     ██╗  ██╗
██╔════╝ ██╔══██╗██║   ██║██╔══██╗██╔═══██╗    ╚██╗██╔╝
██║  ███╗██████╔╝██║   ██║██████╔╝██║   ██║     ╚███╔╝ 
██║   ██║██╔══██╗██║   ██║██╔═══╝ ██║   ██║     ██╔██╗ 
╚██████╔╝██║  ██║╚██████╔╝██║     ╚██████╔╝    ██╔╝ ██╗
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝      ╚═════╝     ╚═╝  ╚═╝

""")

#   --- CLASE CANCION ---

# Creando las instacias de la clase cancion
cancion1 = Cancion("Noche Estrellada", 315, "Indie Rock")
cancion2 = Cancion("Ritmo Salvaje", 210, "Reggae")
cancion3 = Cancion("Caída Libre", 270, "Metal")

#Imprimiendo los valores de cda instacion
print(f"\nCanción 1: {cancion1.nombre} | Duración: {cancion1.duracion} segundos | Género: {cancion1.genero}")
print(f"Canción 2: {cancion2.nombre} | Duración: {cancion2.duracion} segundos | Género: {cancion2.genero}")
print(f"Canción 3: {cancion3.nombre} | Duración: {cancion3.duracion} segundos | Género: {cancion3.genero}")

#modificando/actualizando el valor  a una propiedad de una instancia 
print(f"\nCambiando el género de Canción 3...")
print(f"Género original de Canción 3: {cancion3.genero}")
cancion3.genero = "Post Rock"
print(f"Nuevo género de Canción 3: {cancion3.genero}")

#instancias actualizadas
print(f"\n¡Aquí están los géneros actualizados!")
print(f"Canción 1: {cancion1.genero} | Canción 2: {cancion2.genero} | Canción 3: {cancion3.genero}")

#   --- CLASE CIRCULO ---

circulo1 = Circulo(111.20);
circulo2 = Circulo(250.21);
circulo3 = Circulo(30.22);
circulo4 = Circulo(70.55);
circulo5 = Circulo(70.55);

print(f"El diámetro del círculo1 es: {circulo1.obterDiametro()} | El diámetro del círculo2 es: {circulo2.obterDiametro()} | El diámetro del círculo3 es: {circulo3.obterDiametro()}  ")

print(f"El diámetro del círculo2 es: {circulo1.pi} | El diámetro del círculo2 es: {circulo2.pi} | El diámetro del círculo3 es: {circulo3.pi}  ")

print(f"El radio de Circulo4 y Circulo5 son iguales? { circulo4.obtenerRadio() == circulo5.obtenerRadio()}")

print(f"El perimetro de Circulo4 y Circulo5 son iguales? { circulo4.obtenerPerimetro() == circulo5.obtenerPerimetro()}")
