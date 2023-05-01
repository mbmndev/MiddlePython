### Programa 3: Información medica de paciente:

#El JSON generado deberá ser:

#{"nombre": "Pedro", "apellido": "Pérez", "edad": 45, "peso": 80.5, "altura": 1.75, "historial_medico": {"alergias": ["penicilina", "mariscos"], "problemas_cardiacos": false, "medicamentos": [{"nombre": "Ibuprofeno", "dosis": "200mg"}, {"nombre": "Paracetamol", "dosis": "500mg"}]}, "ultima_revision": "2022-10-01", "proximo_turno": "2023-05-15"}

import json
def principal():
    nombre = input("Ingrese el nombre del paciente: ")
    apellido = input("Ingrese el apellido del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    peso = float(input("Ingrese el peso del paciente en kg: "))
    altura = float(input("Ingrese la altura del paciente en metros: "))
    alergias = input("Ingrese las alergias del paciente separadas por coma (si no tiene alergias, escriba 'ninguna'): ")
    problemas_cardiacos = input("¿Tiene el paciente problemas cardiacos? (sí o no): ").lower() == "sí"
    medicamentos = []

    while True:
        nombre_medicamento = input("Ingrese el nombre del medicamento (o escriba 'ninguno' para terminar): ")
        if nombre_medicamento == "ninguno":
            break
        dosis_medicamento = input("Ingrese la dosis del medicamento: ")
        medicamento = {
            "nombre": nombre_medicamento,
            "dosis": dosis_medicamento
        }
        medicamentos.append(medicamento)

    ultima_revision = input("Ingrese la fecha de la última revisión médica en formato ISO 8601 (ejemplo: 2022-10-01): ")
    proximo_turno = input("Ingrese la fecha del próximo turno médico en formato ISO 8601 (ejemplo: 2023-05-15): ")

    historial_medico = {
        "alergias": alergias.split(","),
        "problemas_cardiacos": problemas_cardiacos,
        "medicamentos": medicamentos
    }

    paciente = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "peso": peso,
        "altura": altura,
        "historial_medico": historial_medico,
        "ultima_revision": ultima_revision,
        "proximo_turno": proximo_turno
    }

    json_paciente = json.dumps(paciente)
    print(json_paciente)
if __name__ == "__main__":
    principal()