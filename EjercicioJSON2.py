### Programa 2: Transacción financiera:
#El JSON generado deberá ser.

#{"id": 123456789, "fechayhora": "2023-04-18T12:30:00Z", "monto": 500.25, "tipo": "compra", "producto": {"nombre": "Smartphone", "precio": 450.00, "descripcion": "Un teléfono inteligente de última generación"}}

import json

id = int(input("Ingrese el ID de la transacción: "))
fechayhora = input("Ingrese la fecha y hora en formato ISO 8601 (ejemplo: 2023-04-18T12:30:00Z): ")
monto = float(input("Ingrese el monto de la transacción: "))
tipo = input("Ingrese el tipo de transacción: ")
nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
descripcion_producto = input("Ingrese una descripción del producto: ")

producto = {
    "nombre": nombre_producto,
    "precio": precio_producto,
    "descripcion": descripcion_producto
}

transaccion = {
    "id": id,
    "fechayhora": fechayhora,
    "monto": monto,
    "tipo": tipo,
    "producto": producto
}

json_transaccion = json.dumps(transaccion)
print(json_transaccion)

