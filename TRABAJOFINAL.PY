from empleados import buscar_empleado, total_empleados, existe_empleado

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

    # MENU
    while True:

        print("===== SISTEMA DE ASISTENCIA =====")
        print("1. Buscar empleado")
        print("2. Registrar asistencia")
        print("3. Ver reporte")
        print("4. Ver total de empleados")
        print("5. Salir")

        opcion = input("Ingrese opcion: ")

        # BUSCAR EMPLEADO
        if opcion == "1":

            dato = input("Ingrese nombre o DNI del empleado: ")

            buscar_empleado(dato, empleados, dni)

        # REGISTRAR INGRESO
        elif opcion == "2":

            nombre = input("Ingrese apellido y nombre: ")
            dni_ingresado = input("Ingrese DNI: ")

            encontrado = existe_empleado(nombre, dni_ingresado, empleados, dni)

            if encontrado == True:

                hora = input("Ingrese hora de llegada(HH:MM): ")
                dia = input("Ingrese dia/mes/año: ")

                # SEPARAR HORAS Y MINUTOS
                hora_partes = hora.split(":")

                hora_num = int(hora_partes[0])
                minuto_num = int(hora_partes[1])

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
                print("Fecha:", dia)
                print("Estado:", estado)

            else:
                print("\nEmpleado no encontrado")

        # REPORTE DE INGRESO
        elif opcion == "3":

            print("===== REPORTE DE ASISTENCIA =====")

            for i in range(len(reporte_nombres)):

                print("Trabajador:", reporte_nombres[i])
                print("DNI:", reporte_dni[i])
                print("Hora de llegada:", reporte_horas[i])
                print("Estado:", reporte_estado[i])

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
