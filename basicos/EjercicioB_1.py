# 1.- Crear una lista que contenga las letras de una palabra, cada una en mayúscula:
def normal():
    entrada = input("Introduce una palabra ")
    lista = list(entrada.upper())
    print("La siguiente lista ha sido hecha de forma normal")
    print(lista)


def compresion():
    entrada = input("Introduce una palabra ")
    lista = [letra.upper() for letra in entrada]
    print("La siguiente lista ha sido hecha de forma de compresion de colecciones")
    print(lista)


def principal():
    compresion()


if __name__ == "__main__":
    principal()
    # normal()
    # # compresion()
