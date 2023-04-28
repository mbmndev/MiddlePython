# 3.- Dado un texto con una lista de ciudades con su emblema mas importante, pedir las ciudades para que las entre el usuario por teclado y crear un diccionario con su ciudad y su emblema. **Nota** el diccionario deberá ordenarse por su clave.
def normal():
    entrada = input(
        "Ingresa las ciudades y sus emblemas de la siguiente manera pais:emblema,pais:emblema ")
    ciudades = entrada.split(",")
    dicionario = {}
    for ciudad in ciudades:
        ciudad_emblema = ciudad.split(":")
        dicionario[ciudad_emblema[0].replace(" ", "").capitalize(
        )] = ciudad_emblema[1].replace(" ", "").capitalize()
    ciudades_ordenadas = dict(sorted(dicionario.items()))
    print("Acontinuacion se muestra el diccionario de las ciudades y emblemas, de forma normal")
    print(ciudades_ordenadas)


def compresion():
    entrada = input(
        "Ingresa las ciudades y sus emblemas de la siguiente manera pais:emblema,pais:emblema ")
    ciudades = entrada.split(",")
    dicionario = {ciudad_emblema[0].replace(" ", "").capitalize(): ciudad_emblema[1].replace(
        " ", "").capitalize() for ciudad_emblema in [ciudad.split(":") for ciudad in ciudades]}
    ciudades_ordenadas = dict(sorted(dicionario.items()))
    print("Acontinuacion se muestra el diccionario de las ciudades y emblemas, usando compresion")
    print(ciudades_ordenadas)


def principal():
    compresion()


if __name__ == "__main__":
    principal()
    # normal()
    # # compresion()
