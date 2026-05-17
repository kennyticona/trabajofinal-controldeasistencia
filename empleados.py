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


def total_empleados(empleados):

    print("Total de empleados registrados:", len(empleados))
