from asistencia import configurar_horario, registrar_asistencia
from auth import crear_administrador, existe_administrador, iniciar_sesion
from config import EMPRESA_DEFAULT
from personal import (
    contar_personal_activo,
    desactivar_personal,
    listar_personal,
    registrar_personal,
)
from reportes import reporte_detallado, reporte_por_trabajador, reporte_resumen
from storage import asegurar_carpeta_data, cargar_json
from config import ARCHIVO_CONFIG
from ui import mostrar_separador, mostrar_titulo, pausar, solicitar_opcion


def _nombre_empresa():
    config = cargar_json(ARCHIVO_CONFIG, {"empresa": EMPRESA_DEFAULT})
    return config.get("empresa", EMPRESA_DEFAULT)


def menu_personal():
    while True:
        mostrar_titulo("GESTION DE PERSONAL")
        print("1. Registrar nuevo trabajador")
        print("2. Listar personal activo")
        print("3. Desactivar trabajador")
        print("0. Volver al menu principal")
        mostrar_separador("-", 50)

        opcion = solicitar_opcion("Opcion", ["0", "1", "2", "3"])

        if opcion == "1":
            registrar_personal()
        elif opcion == "2":
            listar_personal()
        elif opcion == "3":
            desactivar_personal()
        elif opcion == "0":
            break


def menu_asistencia():
    while True:
        mostrar_titulo("REGISTRO DE ASISTENCIA")
        print("Personal activo registrado:", contar_personal_activo())
        print()
        print("1. Registrar asistencia del dia")
        print("2. Configurar hora limite de entrada")
        print("0. Volver al menu principal")
        mostrar_separador("-", 50)

        opcion = solicitar_opcion("Opcion", ["0", "1", "2"])

        if opcion == "1":
            registrar_asistencia()
        elif opcion == "2":
            configurar_horario()
        elif opcion == "0":
            break


def menu_reportes():
    while True:
        mostrar_titulo("REPORTES")
        print("1. Reporte detallado (todos los registros)")
        print("2. Reporte general (totales)")
        print("3. Reporte por trabajador (DNI)")
        print("0. Volver al menu principal")
        mostrar_separador("-", 50)

        opcion = solicitar_opcion("Opcion", ["0", "1", "2", "3"])

        if opcion == "1":
            reporte_detallado()
        elif opcion == "2":
            reporte_resumen()
        elif opcion == "3":
            reporte_por_trabajador()
        elif opcion == "0":
            break


def menu_principal():
    while True:
        empresa = _nombre_empresa()
        mostrar_titulo(empresa.upper() + " - PANEL ADMIN")
        print("Personal activo:", contar_personal_activo())
        print()
        print("1. Gestion de personal")
        print("2. Registro de asistencia")
        print("3. Reportes")
        print("0. Cerrar sesion")
        mostrar_separador("-", 50)
        print("Tip: registre primero al personal, luego marque asistencias.")

        opcion = solicitar_opcion("Opcion", ["0", "1", "2", "3"])

        if opcion == "1":
            menu_personal()
        elif opcion == "2":
            menu_asistencia()
        elif opcion == "3":
            menu_reportes()
        elif opcion == "0":
            print("\nSesion cerrada. Hasta pronto.")
            break


def ejecutar():
    asegurar_carpeta_data()

    mostrar_titulo("ACCESSIQ - CONTROL DE ASISTENCIA")
    print("Sistema mejorado de registro y reportes.")
    print("Continuacion del trabajo de Fundamentos de Programacion.")
    mostrar_separador("-", 50)

    if not existe_administrador():
        if not crear_administrador():
            return
    else:
        if not iniciar_sesion():
            return

    menu_principal()


if __name__ == "__main__":
    ejecutar()
