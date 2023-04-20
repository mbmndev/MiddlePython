import os
import sys
#from Varios import principal

from Ejercicios import EjercicioJSON1.py
from Ejercicios import EjercicioJSON2.py
from Ejercicios import EjercicioJSON3.py
from Ejercicios import EjercicioClases1.py
from Ejercicios import EjercicioClases2.py
from Ejercicios import EjercicioClases3.py
from Ejercicios import EjercicioClases4.py
from Ejercicios import EjercicioCompresionBasico1.py
from Ejercicios import EjercicioCompresionBasico2.py
from Ejercicios import EjercicioCompresionBasico3.py
from Ejercicios import EjercicioCompresionAvanzado1.py
from Ejercicios import EjercicioCompresionAvanzado2.py
from Ejercicios import EjercicioCompresionAvanzado3.py


while True:
    if sys.platform.startswith("linux"):
        # linux
        os.system('clear') 
    elif sys.platform == "darwin":
        # MAX OS X
        os.system('clear') 
    elif os.name == "nt":
        #Windows, Cigwyin, etc. (32/64-bit)
        os.system('cls') 
    # os.system("cls") #Limpia la pantalla en la consola
    # os.system("clear") #Limpia pantalla consola MAC y Linux
    
    print("Bienvenidos")
    print("Menu principal")

    print("1-Información sobre un usuario: ")
    print("2-Transacción financiera:")
    print("3-Información medica de paciente:")
    print("4-Crear una clase `Lapiz` que tenga los atributos `color` (cadena de caracteres) y `grosor` (entero). El constructor debe inicializar ambos atributos con valores por defecto. Agregar un método `escribir` que imprima por pantalla la frase Escribiendo con un lapiz de [color] y grosor [grosor]. Crear un objeto de la clase `Lapiz` e invocar el método `escribir`.")
    print("5-Crear una clase `Flor` que tenga los atributos `nombre` (cadena de caracteres) y `color` (cadena de caracteres). El constructor debe recibir ambos atributos como argumentos e inicializarlos. Agregar un método `mostrar_informacion` que imprima por pantalla el nombre y color de la flor. Crear dos objetos de la clase `Flor` e invocar el método `mostrar_informacion` para ambos.")
    print("6-Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de productos.")
    print("7-Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de alumnos.")
    print("8-Crear una lista que contenga las letras de una palabra, cada una en mayúscula:")
    print("9-Crear un diccionario que contenga el cuadrado de cada número del 1 al 5:")
    print("10-Crear un diccionario que contenga los nombres y edades de varias personas:")
    print("11-Crear una lista que contenga los números del 1 al 20, pero reemplazando los múltiplos de 3 por EOI, los múltiplos de 5 por Cloud y los múltiplos de ambos por EOICloud.")
    print("12-Crear un diccionario que contenga las palabras en una lista y la cantidad de veces que aparecen en ella")
    print("13-Dado un texto con una lista de ciudades con su emblema mas importante, pedir las ciudades para que las entre el usuario por teclado y crear un diccionario con su ciudad y su emblema. **Nota** el diccionario deberá ordenarse por su clave.")

    print("0-Salir")

    opcion = input("Seleccione una opción:")

    if opcion == "1":
        EjercicioJSON1.principal()
    elif opcion == "2":
        EjercicioJSON2.principal()
    elif opcion == "3":
        EjercicioJSON3.principal()
    elif opcion == "4":
        EjercicioClases1.principal() 
    elif opcion == "5":
        EjercicioClases2.principal() 
    elif opcion == "6":
        EjercicioClases3.principal() 
    elif opcion == "7":
        EjercicioClases4.principal()
    elif opcion == "8":
        EjercicioCompresionBasico1.principal()     
    elif opcion == "9":
        EjercicioCompresionBasico2.principal() 
    elif opcion == "10":
        EjercicioCompresionBasico3.principal() 
    elif opcion == "11":
        EjercicioCompresionAvanzado1.principal()
    elif opcion == "12":
        EjercicioCompresionAvanzado2.principal() 
    elif opcion == "13":
        EjercicioCompresionAvanzado3.principal()


    elif opcion == "0":
        print("Un placer atenderle. Chao!")
        break

    continuar=input("Presione enter para continuar...")