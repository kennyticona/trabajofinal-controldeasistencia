def registro_empleado(nombre, dni_ingresado, empleados, dni, hora):

    encontrado = False
    estado = ""

    for i in range(len(empleados)):

        if empleados[i] == nombre and dni[i] == dni_ingresado:

            encontrado = True

            print("Asistencia registrada")

            # VALIDAR ESTADO
            if 0 < hora <= 8:
                estado = "PUNTUAL"

            elif hora == 0:
                estado = "FALTA"

            elif hora > 8:
                estado = "TARDANZA"

            print("Estado:", estado)

    if encontrado == False:
        print("Empleado no encontrado")

    return estado


def main():

    empleados = ["RAMOS CUSTODIO CRISTIAN WALTER","ALVARADO OJANAMA LUIS ALONSO","MENDEZ SANCHEZ ELIZABETH ALEXANDRA","CARDENAS QUIHUI CARLOS YAMIL","MELENDEZ ORTIZ JOEL EDILBERTO","VARGAS CAUSAL XIMENA AKEMY","MENDEZ CCORAHUA JHON ANTONI","CUCHO CUICAPUZA MITSY JHASDELI","MECHADO ESPINOZA GENARO PASCUAL","LOYOLA JIMENEZ BRUCE AXEL",
    "PEREZ MALMACEDA MIGUEL ANGEL", "MALDONADO FARFAN GIOVANNA EDITH","RUIZ ROCA SAMANTA","PONCE CHILQUE JESSENIA ROXANA","RUIZ CHINCHAY JACKELINE ISABEL","SANCHEZ GONZALES EDGARD DANIEL","PEREDA POLO KATHERINE JANETH","VALENCIA GUERRERO LAZARO CLEVER","VARGAS JARAMILLO EMELY ALEJANDRA",
    "VILLACORTA REYES MARIANO FERNANDO"]

    dni = ["90728638", "45436442", "75930246", "75455244","44677427", "71755540", "48845247", "47879234","42231592", "76622235", "40442266", "10333834","72239502", "42333337", "47234141", "76923415","73223425", "75323452", "72791237", "10844389"]


    # CONTADORES
    contador_puntual = 0
    contador_falta = 0
    contador_tardanza = 0

    while True:

        print("===== SISTEMA DE ASISTENCIA =====")
        print("1. Registrar asistencia")
        print("2. Ver reporte")
        print("3. Salir")

        opcion = input("Ingrese opcion: ")

        # REGISTRAR
        if opcion == "1":

            hora_ingreso = int(input("Ingrese la hora de ingreso: "))

            fecha_ingreso = input("Ingrese fecha: ")

            nombre = input("Ingrese apellido y nombre: ")

            dni_ingresado = input("Ingrese dni: ")

            estado = registro_empleado(nombre,dni_ingresado,empleados,dni,hora_ingreso)

            # CONTADORES
            if estado == "PUNTUAL":
                contador_puntual = contador_puntual + 1

            elif estado == "FALTA":
                contador_falta = contador_falta + 1

            elif estado == "TARDANZA":
                contador_tardanza = contador_tardanza + 1

            print("Fecha:", fecha_ingreso)

        # VER REPORTE
        elif opcion == "2":

            print("===== REPORTE GENERAL =====")
            print("Puntuales:", contador_puntual)
            print("Tardanzas:", contador_tardanza)
            print("Faltas:", contador_falta)

        # SALIR
        elif opcion == "3":

            print("Sistema finalizado")
            break

        else:
            print("Opcion incorrecta")

main()
