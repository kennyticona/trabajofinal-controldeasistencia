def registro_empleado(nombre, dni_ingresado, empleados, dni, hora):

    encontrado = False

    for i in range(len(empleados)):

        if empleados[i] == nombre and dni[i] == dni_ingresado:

            encontrado = True
            print("Asistencia registrada")
           
    if encontrado == False:
        print("Empleado no encontrado")

def hora_ingreso_trabajador(hora_ingreso, hora_ingreso_establecida):
    if 0 <hora_ingreso <= hora_ingreso_establecida:
        print("Puntual")
    elif hora_ingreso == 0:
        print("Falta")
    elif hora_ingreso > hora_ingreso_establecida:
        print("Tardanza")

def main():
    
    empleados = ["RAMOS CUSTODIO CRISTIAN WALTER","ALVARADO OJANAMA LUIS ALONSO","MENDEZ SANCHEZ ELIZABETH ALEXANDRA","CARDENAS QUIHUI CARLOS YAMIL","MELENDEZ ORTIZ JOEL EDILBERTO","VARGAS CAUSAL XIMENA AKEMY","MENDEZ CCORAHUA JHON ANTONI","CUCHO CUICAPUZA MITSY JHASDELI","MECHADO ESPINOZA GENARO PASCUAL","LOYOLA JIMENEZ BRUCE AXEL",
    "PEREZ MALMACEDA MIGUEL ANGEL", "MALDONADO FARFAN GIOVANNA EDITH","RUIZ ROCA SAMANTA","PONCE CHILQUE JESSENIA ROXANA","RUIZ CHINCHAY JACKELINE ISABEL","SANCHEZ GONZALES EDGARD DANIEL","PEREDA POLO KATHERINE JANETH","VALENCIA GUERRERO LAZARO CLEVER","VARGAS JARAMILLO EMELY ALEJANDRA",
    "VILLACORTA REYES MARIANO FERNANDO"]

    dni = ["90728638", "45436442", "75930246", "75455244","44677427", "71755540", "48845247", "47879234","42231592", "76622235", "40442266", "10333834","72239502", "42333337", "47234141", "76923415","73223425", "75323452", "72791237", "10844389"]


    hora_ingreso = int(input("Ingrese la hora de ingreso: "))
    hora_ingreso_establecida = 8
    fecha_ingreso = input("Ingrese fecha de hoy dia/mes/año: ")
    nombre = input("Ingrese apellido y nombre: ")
    dni_ingresado =input("Ingrese dni: ")
    

    print("Generando estado de asistencia")
    registro_empleado(nombre, dni_ingresado, empleados, dni, hora_ingreso)
    hora_ingreso_trabajador(hora_ingreso, hora_ingreso_establecida)
    print("fecha" ,fecha_ingreso)

main()