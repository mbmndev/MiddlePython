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
    


alumnos_lista = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 20, "notas": [7, 8, 9]},
    {"nombre": "María", "apellido": "González", "edad": 22, "notas": [6, 9, 10]},
    {"nombre": "Pedro", "apellido": "García", "edad": 21, "notas": [5, 7, 8]} ]

alumno={"nombre": "", "apellido": "", "edad": 0, "notas": 0}

nombre=""
apellido=""
edad=0
notas=0

listaAlumnos=ListaAlumnos(alumnos_lista,"","",0,0,alumno)

while True:
    nombre=input("Ingrese el nombre del alumno: ".capitalize())
    if nombre.isalpha():
        apellido=input("Introduzca el apellido del alumno:".capitalize())
        if apellido.isalpha():
            edad=input("Introduzca la edad del alumno :")
            if edad.isdigit():
                edadInt=int(edad)
                notas=input("Introduzca las notas del alumno :")
                if notas.isdigit():
                    notasInt=int(notas)
                    
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


listaAlumnos.mostrarAlumnos()
