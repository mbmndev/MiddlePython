#4. Dada la siguiente lista de alumnos. 
#
#   ```
#   alumnos_lista = [
#       {"nombre": "Juan", "apellido": "Pérez", "edad": 20, "notas": [7, 8, 9]},
#       {"nombre": "María", "apellido": "González", "edad": 22, "notas": [6, 9, 10]},
#       {"nombre": "Pedro", "apellido": "García", "edad": 21, "notas": [5, 7, 8]} ]
#   ```

#   Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de alumnos.

#   La clase deberá tener un método que incorpore el promedio de las notas del alumno.

#   
import statistics

class ListaAlumnos:
    alumnos_lista=[]
    objeto={}


    def __init__(self,alumnos_lista,objeto):
        self.Alumnos_lista=alumnos_lista

        self.Objeto=objeto

    def crearAlumno(self,objeto):
        self.Objeto=objeto
        self.Alumnos_lista.append(self.Objeto)

    def mostrarAlumnos(self):
        for alumnos in self.Alumnos_lista:
            print(alumnos)
    def promedio(self):
        aux=0
        for i in range(len(self.Alumnos_lista)):
            mean = statistics.mean(self.Alumnos_lista[i]["notas"])
            name=self.Alumnos_lista[i]["nombre"]
            print(f"El promedio del alumno {name} es: {mean:.2f}")
           


alumnos_lista = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 20, "notas": [7, 8, 9]},
    {"nombre": "María", "apellido": "González", "edad": 22, "notas": [6, 9, 10]},
    {"nombre": "Pedro", "apellido": "García", "edad": 21, "notas": [5, 7, 8]} ]

alumno={"nombre": "", "apellido": "", "edad": 0, "notas": 0}

nombre=""
apellido=""
edad=0
notas=0

listaAlumnos=ListaAlumnos(alumnos_lista,alumno)

while True:
    nombre=input("Ingrese el nombre del alumno: ".capitalize())
    if nombre.isalpha():
        apellido=input("Introduzca el apellido del alumno:".capitalize())
        if apellido.isalpha():
            edad=input("Introduzca la edad del alumno :")
            if edad.isdigit():
                edadInt=int(edad)
                notas=input("Introduzca las 3 notas del alumno entre espacios :").split()
                if len(notas)<=3:
                    notas=[int(i) for i in notas]
                    alumno["nombre"]=nombre
                    alumno["apellido"]=apellido
                    alumno["edad"]=edadInt
                    alumno["notas"]=notas

                    listaAlumnos.crearAlumno(alumno)

                    continuar=input("Escriba s si desea introducir otro producto:")
                    if continuar!="s" or continuar!="S":
                        break
                    continue
                else:print("Error al introducir las notas")    
            else: print("Error al introducir la edad")
        else: print("Error al introducir el apellido")
    else: print("Error al introducir el nombre")

print()
print("Lista de Alumnos:")
listaAlumnos.mostrarAlumnos()
print()
listaAlumnos.promedio()

