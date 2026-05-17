def hora_ingreso_trabajador(hora_ingreso, hora_ingreso_establecida):
    if 0 <hora_ingreso <= hora_ingreso_establecida:
        print("Puntual")
    elif hora_ingreso == 0:
        print("Falta")
    elif hora_ingreso > hora_ingreso_establecida:
        print("Tardanza")

def main():
    hora_ingreso = int(input("Ingrese la hora de ingreso: "))
    hora_ingreso_establecida = 8
    fecha_ingreso = input("Ingrese fecha de hoy dia/mes/año: ")
    

    print("Generando estado de asistencia")
    hora_ingreso_trabajador(hora_ingreso, hora_ingreso_establecida)


main()
