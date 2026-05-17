from asistencia import cargar_registros
from ui import mostrar_info, mostrar_separador, mostrar_titulo, pausar, solicitar_dni


def _contar_por_estado(registros):
    contadores = {"PUNTUAL": 0, "TARDANZA": 0, "FALTA": 0}
    i = 0
    while i < len(registros):
        estado = registros[i]["estado"]
        if estado in contadores:
            contadores[estado] = contadores[estado] + 1
        i = i + 1
    return contadores


def reporte_detallado():
    registros = cargar_registros()
    mostrar_titulo("REPORTE DETALLADO")

    if len(registros) == 0:
        mostrar_info("No hay registros de asistencia.")
        pausar()
        return

    i = 0
    while i < len(registros):
        r = registros[i]
        mostrar_separador("-", 50)
        print("Registro #", r["id"])
        print("Trabajador:", r["nombre"])
        print("DNI:", r["dni"])
        print("Cargo:", r["cargo"])
        print("Fecha:", r["fecha"])
        print("Hora:", r["hora"])
        print("Estado:", r["estado"])
        i = i + 1

    print()
    pausar()


def reporte_resumen():
    registros = cargar_registros()
    mostrar_titulo("REPORTE GENERAL")

    if len(registros) == 0:
        mostrar_info("No hay registros de asistencia.")
        pausar()
        return

    contadores = _contar_por_estado(registros)
    total = len(registros)

    print("Total de registros :", total)
    print("Puntuales          :", contadores["PUNTUAL"])
    print("Tardanzas          :", contadores["TARDANZA"])
    print("Faltas             :", contadores["FALTA"])

    if total > 0:
        pct_puntual = round((contadores["PUNTUAL"] / total) * 100, 1)
        print("\nPorcentaje de puntualidad:", str(pct_puntual) + "%")

    pausar()


def reporte_por_trabajador():
    registros = cargar_registros()
    mostrar_titulo("REPORTE POR TRABAJADOR")

    if len(registros) == 0:
        mostrar_info("No hay registros de asistencia.")
        pausar()
        return

    dni = solicitar_dni()
    filtrados = []
    i = 0
    while i < len(registros):
        if registros[i]["dni"] == dni:
            filtrados.append(registros[i])
        i = i + 1

    if len(filtrados) == 0:
        mostrar_info("No hay registros para ese DNI.")
        pausar()
        return

    print("\nHistorial de:", filtrados[0]["nombre"])
    contadores = _contar_por_estado(filtrados)

    j = 0
    while j < len(filtrados):
        r = filtrados[j]
        mostrar_separador("-", 50)
        print("Fecha:", r["fecha"], "| Hora:", r["hora"], "| Estado:", r["estado"])
        j = j + 1

    print()
    mostrar_separador("-", 50)
    print("Resumen del trabajador:")
    print("  Puntuales:", contadores["PUNTUAL"])
    print("  Tardanzas:", contadores["TARDANZA"])
    print("  Faltas:", contadores["FALTA"])
    pausar()
