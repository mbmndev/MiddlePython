# 2.- Crear un diccionario que contenga el cuadrado de cada número del 1 al 5:
def normal():
    diccionario = {}
    for x in range(1, 6):
        diccionario[x] = pow(x, 2)
    print("Acontinuacion se muestra el diccionario de los cuadrados del 1 al 6 de forma normal")
    print(diccionario)


def comprension():
    diccionario = {x: pow(x, 2) for x in range(1, 6)}
    print("Acontinuacion se muestra el diccionario de los cuadrados del 1 al 6 usando la comprension de coleccion")
    print(diccionario)


if __name__ == "__main__":
    # normal()
    comprension()
