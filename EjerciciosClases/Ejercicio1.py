#1. Crear una clase `Lapiz` que tenga los atributos `color` (cadena de caracteres) y `grosor` (entero). 
#El constructor debe inicializar ambos atributos con valores por defecto. 
#Agregar un método `escribir` que imprima por pantalla la frase "Escribiendo con un lapiz de [color] y grosor [grosor]". 
# Crear un objeto de la clase `Lapiz` e invocar el método `escribir`.

class Lapiz:

    
    def __init__(self,color="negro",grosor=0):
        self.Color=color
        self.Grosor=grosor

       
    def __escribir(self):
        print(f"Escribiendo con un lapiz de color {self.Color} y grosor {self.Grosor}")
        #print("Escribiendo")
    def escribirColor(self):
        self.__escribir()

lapiz=Lapiz()
lapiz.escribirColor()