# 1.- Crear una lista que contenga los números del 1 al 20, pero reemplazando los múltiplos de 3 por `"EOI"`, los múltiplos de 5 por `"Cloud"` y los múltiplos de ambos por `"EOICloud"`.
def normal():
    lista = []
    for x in range(1, 21):
        if x % 3 == 0 and x % 5 == 0:
            lista.append("EOICloud")
        elif x % 3 == 0:
            lista.append("EOI")
        elif x % 5 == 0:
            lista.append("Cloud")
        else:
            lista.append(x)
    print("La siguiente lista ha sido hecha de forma normal")
    print(lista)


def compresion():
    lista = ["EOICloud" if i % 3 == 0 and i % 5 == 0 else "EOI" if i %
             3 == 0 else "Cloud" if i % 5 == 0 else i for i in range(1, 21)]
    print("La siguiente lista ha sido hecha de forma de compresion de colecciones")
    print(lista)


if __name__ == "__main__":
    # normal()
    compresion()
