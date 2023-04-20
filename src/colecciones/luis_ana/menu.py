asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}


def menu():
    entrada = ''
    while entrada != "esc":
        menu = '''
                1. Calcular la cantidad total de sesiones a las que asistieron Ana y Luis en conjunto.
                2. Mostrar las sesiones a las que asistieron ambos alumnos.
                3. Mostrar las sesiones a las que asistió uno de los dos alumnos, pero no a las que asistieron ambos.
                4. Mostrar las sesiones a las que asistió Ana pero no Luis.
                5. Mostrar las sesiones a las que asistió Luis pero no Ana.
                6. ESC o esc para salir.
        '''
        entrada = input(menu).lower()
        if entrada == '1':
            print(
                f"~~Los alumnos han asistido un total de {Ejercicio_1()} asistencias")
        elif entrada == '2':
            print(
                f"~~Las sesiones a las que los alumnos asistieron son {Ejercicio_2()}")
        elif entrada == '3':
            print(
                f"~~La assistencias en las que no coiciden son {Ejercicio_3(Ejercicio_2())}")
        elif entrada == '4':
            setT = AsistioAlumno1NoAlumno2(
                Ejercicio_3(Ejercicio_2()), "Ana", "Luis")
            print(f"~~Asistio Ana pero no Luis {setT}")
        elif entrada == '5':
            setT = AsistioAlumno1NoAlumno2(
                Ejercicio_3(Ejercicio_2()), "Luis", "Ana")
            print(f"~~Asistio Luis pero no Ana {setT}")
        elif entrada == 'esc':
            print(f"~~Saliendo del menu")
        else:
            pass


def Ejercicio_1():
    # codigo con bucle for
    # sesionesTotales = 0
    # for alumno in asistencias:
    #     sesionesTotales += len(asistencias[alumno])
    # codigo compresion coleccion
    sesionesTotales = sum([len(asistencias[alumno]) for alumno in asistencias])
    return sesionesTotales


def Ejercicio_2():
    tupla = tuple()
    for alumno in asistencias:
        tupla += asistencias[alumno]
    return tupla


def Ejercicio_3(tupla=tuple()):
    # codigo con bucle for
    # setAsistenciasSincoinsidir = set()
    # for x in tupla:
    #     if (tupla.count(x)) == 1:
    #         setAsistenciasSincoinsidir.add(x)
    # codigo compresion coleccion
    setAsistenciasSincoinsidir = {x for x in tupla if tupla.count(x) == 1}
    return setAsistenciasSincoinsidir


def AsistioAlumno1NoAlumno2(setAsistenciasSincoinsidir=set(), alumno1=str(), alumno2=str()):
    # codigo con bucle for
    # ana
    # asistioAnaNoLuis=set()
    # for x in setAsistenciasSincoinsidir:
    #     if x in list(asistencias.get("Ana")):
    #         asistioAnaNoLuis.add(x)
    # luis
    # asistioLuisNoAna=set()
    # for x in setAsistenciasSincoinsidir:
    #     if x in list(asistencias.get("Luis")):
    #         asistioLuisNoAna.add(x)
    # codigo compresion coleccion
    asistioAlumno1NoAlumno2 = {
        x for x in setAsistenciasSincoinsidir if x in asistencias[alumno1] and x not in asistencias[alumno2]}
    return asistioAlumno1NoAlumno2


if __name__ == "__main__":
    menu()
