from empleados import buscar_empleado, total_empleados
def main():
    # ARREGLOS DE EMPLEADOS
    empleados = ["RAMOS CUSTODIO CRISTIAN WALTER","ALVARADO OJANAMA LUIS ALONSO","MENDEZ SANCHEZ ELIZABETH ALEXANDRA","CARDENAS QUIHUI CARLOS YAMIL","MELENDEZ ORTIZ JOEL EDILBERTO","VARGAS CAUSAL XIMENA AKEMY","MENDEZ CCORAHUA JHON ANTONI","CUCHO CUICAPUZA MITSY JHASDELI",
    "MECHADO ESPINOZA GENARO PASCUAL","LOYOLA JIMENEZ BRUCE AXEL","PEREZ MALMACEDA MIGUEL ANGEL","MALDONADO FARFAN GIOVANNA EDITH","RUIZ ROCA SAMANTA","PONCE CHILQUE JESSENIA ROXANA","RUIZ CHINCHAY JACKELINE ISABEL","SANCHEZ GONZALES EDGARD DANIEL","PEREDA POLO KATHERINE JANETH","VALENCIA GUERRERO LAZARO CLEVER","VARGAS JARAMILLO EMELY ALEJANDRA","VILLACORTA REYES MARIANO FERNANDO"]

    dni = ["90728638", "45436442", "75930246", "75455244","44677427", "71755540", "48845247", "47879234","42231592", "76622235", "40442266", "10333834","72239502", "42333337", "47234141", "76923415","73223425", "75323452", "72791237", "10844389"]

    # LISTAS DEL REPORTE
    reporte_nombres = []
    reporte_dni = []
    reporte_horas = []
    reporte_estado = []

    # HORARIO DE ENTRADA
    hora_entrada = 8

    # MENU
    while True:

    print("===== SISTEMA DE ASISTENCIA =====")
    print("1. Registrar asistencia")
    print("2. Ver reporte")
    print("3. Buscar empleado")
    print("4. Ver total de empleados")
    print("5. Salir")

    opcion = input("Ingrese opcion: ")

    # REGISTRAR INGRESO
    if opcion == "1":

        nombre = input("Ingrese apellido y nombre: ")
        dni_ingresado = input("Ingrese DNI: ")
        hora = input("Ingrese hora de llegada(HH:MM): ")
        dia= input("Ingrese dia/mes/año")
        
        encontrado = False
        #SEPARAR HORAS Y MINUTOS
        hora_partes = hora.split(":")

        hora_num = int(hora_partes[0])
        minuto_num = int(hora_partes[1])

        # VALIDAR EMPLEADO
        for i in range(len(empleados)):

            if empleados[i] == nombre and dni[i] == dni_ingresado:

                encontrado = True

                # VALIDAR CONDICION DEL EMPLEADO
                if hora_num == 8 and minuto_num <= 10:
                   estado = "PUNTUAL"

                elif hora_num == 8 and minuto_num >= 11:
                    estado = "TARDE"

                elif hora_num > 8:
                    estado = "TARDE"

                else:
                    estado = "FALTO"

                # GUARDAR DATOS
                reporte_nombres.append(nombre)
                reporte_dni.append(dni_ingresado)
                reporte_horas.append(hora)
                reporte_estado.append(estado)

                print("\nAsistencia registrada")
                print("Estado:", estado)

        if encontrado == False:
            print("\nEmpleado no encontrado")

    # REPORTE DE INGRESO
    elif opcion == "2":

        print("===== REPORTE DE ASISTENCIA ===___0")

        for i in range(len(reporte_nombres)):

            print("Trabajador:", reporte_nombres[i])
            print("DNI:", reporte_dni[i])
            print("Hora de llegada:", reporte_horas[i])
            print("Estado:", reporte_estado[i])

    # BUSCAR EMPLEADO
    elif opcion == "3":

        dato = input("Ingrese nombre o DNI del empleado: ")

        buscar_empleado(dato, empleados, dni)

    # MOSTRAR TOTAL DE EMPLEADOS
    elif opcion == "4":

        total_empleados(empleados)

    # SALIR DEL SISTEMA
    elif opcion == "5":

        print("Sistema finalizado")
        break

    # OPCION INCORRECTA
    else:
        print("Opcion incorrecta")
        
main()

