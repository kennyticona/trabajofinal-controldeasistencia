# VALIDAR SI EL EMPLEADO EXISTE
def existe_empleado(nombre, dni_ingresado, empleados, dni):

    for i in range(len(empleados)):

        if empleados[i] == nombre and dni[i] == dni_ingresado:
            return True

    return False


# BUSCAR EMPLEADO
def buscar_empleado(dato, empleados, dni):

    encontrado = False

    for i in range(len(empleados)):

        if empleados[i] == dato or dni[i] == dato:

            encontrado = True

            print("Empleado encontrado")
            print("Nombre:", empleados[i])
            print("DNI:", dni[i])

    if encontrado == False:

        print("Empleado no encontrado")


# MOSTRAR TOTAL DE EMPLEADOS
def total_empleados(empleados):

    print("Total de empleados registrados:", len(empleados))
