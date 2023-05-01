# Programa 1: Información sobre un usuario:

# El JSON generado deberá ser.
# {"nombre": "Juan", "edad": 30, "email": "juan@acme.com", "trabajo": {"empresa": "Acme Corp", "puesto": "Ingeniero de software"}}

import json


def principal():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    email = input("Ingrese su email: ")
    empresa = input("Ingrese el nombre de su empresa: ")
    puesto = input("Ingrese su puesto de trabajo: ")

    usuario = {
        "nombre": nombre,
        "edad": edad,
        "email": email,
        "trabajo": {
            "empresa": empresa,
            "puesto": puesto
        }
    }

    json_usuario = json.dumps(usuario)
    print(json_usuario)


if __name__ == "main":
    principal()
