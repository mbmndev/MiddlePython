from collections import Counter
# 2.- Crear un diccionario que contenga las palabras en una lista y la cantidad de veces que aparecen en ella.


def normal():
    lista = ["Banana", "Fresa", "Banana", "Naranja",
             "Sandia", "Pera", "Naranja", "Naranja"]
    print(f"La lista contiene la siguiente los siguientes elementos:{lista}")
    diccionario = dict(Counter(lista))
    print("Acontinuacion se muestra el diccionario de la cantidad de veces que aparece una palabra en una lista, de forma normal")
    print(diccionario)


def compresion():
    lista = ["Banana", "Fresa", "Banana", "Naranja",
             "Sandia", "Pera", "Naranja", "Naranja"]
    print(f"La lista contiene la siguiente los siguientes elementos:{lista}")
    diccionario = {fruta: lista.count(fruta) for fruta in lista}
    print("Acontinuacion se muestra el diccionario de la cantidad de veces que aparece una palabra en una lista, usando compresion")
    print(diccionario)


def principal():
    compresion()


if __name__ == "__main__":
    principal()
    # normal()
    # # compresion()
