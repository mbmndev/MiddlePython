#2. Crear una clase `Flor` que tenga los atributos `nombre` (cadena de caracteres) y `color` (cadena de caracteres). 
# El constructor debe recibir ambos atributos como argumentos e inicializarlos. 
# Agregar un método `mostrar_informacion` que imprima por pantalla el nombre y color de la flor. 
#Crear dos objetos de la clase `Flor` e invocar el método `mostrar_informacion` para ambos.

class Flor:

    def __init__(self,nombre,color):
        self.Nombre=nombre
        self.Color=color
    def mostrarInformacion(self):
        print(f"{self.Nombre} de color {self.Color}")
        
flor1=Flor("Rosa","Roja")
flor2=Flor("Clavel","Azul")

flor1.mostrarInformacion()
flor2.mostrarInformacion()