import getpass
import re


def limpiar_pantalla():
    print("\n" * 2)


def mostrar_separador(caracter="=", largo=50):
    print(caracter * largo)


def mostrar_titulo(texto):
    limpiar_pantalla()
    mostrar_separador()
    print(texto.center(50))
    mostrar_separador()


def mostrar_exito(mensaje):
    print("\n[OK]", mensaje)


def mostrar_error(mensaje):
    print("\n[ERROR]", mensaje)


def mostrar_info(mensaje):
    print("\n[INFO]", mensaje)


def pausar(mensaje="Presione Enter para continuar..."):
    input("\n" + mensaje)


def solicitar_opcion(mensaje, opciones_validas):
    texto_opciones = ", ".join(opciones_validas)
    while True:
        valor = input(mensaje + " (" + texto_opciones + "): ").strip()
        if valor in opciones_validas:
            return valor
        mostrar_error("Opcion invalida. Elija: " + texto_opciones)


def solicitar_texto(etiqueta, ejemplo="", minimo=1, oculto=False):
    while True:
        if ejemplo:
            print("  Formato: " + ejemplo)
        if oculto:
            valor = getpass.getpass("  " + etiqueta + ": ").strip()
        else:
            valor = input("  " + etiqueta + ": ").strip()

        if len(valor) >= minimo:
            return valor
        mostrar_error(
            "Debe ingresar al menos " + str(minimo) + " caracter(es)."
        )


def solicitar_entero(etiqueta, minimo, maximo, ejemplo=""):
    while True:
        if ejemplo:
            print("  Formato: numero entre " + str(minimo) + " y " + str(maximo))
            print("  Ejemplo: " + ejemplo)
        texto = input("  " + etiqueta + ": ").strip()
        try:
            numero = int(texto)
            if minimo <= numero <= maximo:
                return numero
        except ValueError:
            pass
        mostrar_error(
            "Ingrese un numero valido entre " + str(minimo) + " y " + str(maximo) + "."
        )


def solicitar_dni():
    while True:
        print("  Formato: 8 digitos numericos")
        print("  Ejemplo: 90728638")
        dni = input("  DNI: ").strip()
        if re.fullmatch(r"\d{8}", dni):
            return dni
        mostrar_error("DNI invalido. Debe tener exactamente 8 digitos.")


def solicitar_fecha():
    while True:
        print("  Formato: DD/MM/AAAA")
        print("  Ejemplo: 17/05/2026")
        print("  Enter = usar fecha de hoy")
        fecha = input("  Fecha: ").strip()
        if fecha == "":
            from storage import fecha_hoy
            return fecha_hoy()
        if re.fullmatch(r"\d{2}/\d{2}/\d{4}", fecha):
            return fecha
        mostrar_error("Fecha invalida. Use el formato DD/MM/AAAA.")


def mostrar_ayuda_registro_personal():
    print("\n--- Como registrar personal ---")
    print("1. Nombre completo en MAYUSCULAS (apellidos primero).")
    print("   Ejemplo: RAMOS CUSTODIO CRISTIAN WALTER")
    print("2. DNI de 8 digitos, sin espacios.")
    print("   Ejemplo: 90728638")
    print("3. Cargo o area del trabajador.")
    print("   Ejemplo: Ventas / Almacen / RRHH")
    mostrar_separador("-", 50)


def mostrar_ayuda_registro_asistencia():
    print("\n--- Como registrar asistencia ---")
    print("1. Busque al trabajador por DNI (debe estar registrado antes).")
    print("2. Hora de ingreso en formato 24h (0 a 23).")
    print("   0  = se registra como FALTA")
    print("   1-8 = PUNTUAL (si la hora limite es 8)")
    print("   >8  = TARDANZA")
    print("3. Puede usar la hora actual presionando Enter.")
    mostrar_separador("-", 50)
