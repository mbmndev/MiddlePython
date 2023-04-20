# 3.- Crear un diccionario que contenga los nombres y edades de varias personas:
def normal():
    diccionario = {}
    cantidad = int(input("¿Cuantas personas quieres añadir?: "))
    for x in range(cantidad):
        nombre = input("introduce nombre de la persona: ")
        edad = input("introduce edad de la persona: ")
        diccionario[nombre] = int(edad)
    print("Acontinuacion se muestra el diccionario de las personas añadidas, de forma normal")
    print(diccionario)


def comprension():
    cantidad = int(input("¿Cuantas personas quieres añadir? "))
    diccionario = {input("introduce nombre de la persona: "): int(
        input("introduce edad de la persona: ")) for x in range(cantidad)}
    print("Acontinuacion se muestra el diccionario de las personas añadidas, usando la comprension de coleccion")
    print(diccionario)


if __name__ == "__main__":
    # normal()
    comprension()
