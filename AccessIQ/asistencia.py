from config import ARCHIVO_CONFIG, ARCHIVO_REGISTROS, HORA_ENTRADA_DEFAULT
from personal import buscar_por_dni, contar_personal_activo
from storage import cargar_json, fecha_hoy, guardar_json, hora_actual
from ui import (
    mostrar_ayuda_registro_asistencia,
    mostrar_error,
    mostrar_exito,
    mostrar_info,
    mostrar_titulo,
    pausar,
    solicitar_dni,
    solicitar_entero,
    solicitar_fecha,
)


def cargar_config():
    default = {
        "hora_entrada": HORA_ENTRADA_DEFAULT,
        "empresa": "AccessIQ",
    }
    config = cargar_json(ARCHIVO_CONFIG, default)
    if "hora_entrada" not in config:
        config["hora_entrada"] = HORA_ENTRADA_DEFAULT
    return config


def guardar_config(config):
    guardar_json(ARCHIVO_CONFIG, config)


def cargar_registros():
    return cargar_json(ARCHIVO_REGISTROS, [])


def guardar_registros(lista):
    guardar_json(ARCHIVO_REGISTROS, lista)


def calcular_estado(hora, hora_limite):
    if hora == 0:
        return "FALTA"
    if 0 < hora <= hora_limite:
        return "PUNTUAL"
    if hora > hora_limite:
        return "TARDANZA"
    return ""


def _siguiente_id_registro(lista):
    if len(lista) == 0:
        return 1
    maximo = 0
    i = 0
    while i < len(lista):
        if lista[i]["id"] > maximo:
            maximo = lista[i]["id"]
        i = i + 1
    return maximo + 1


def registrar_asistencia():
    if contar_personal_activo() == 0:
        mostrar_titulo("REGISTRAR ASISTENCIA")
        mostrar_error(
            "Primero debe registrar personal (Menu > Gestion de personal > Registrar)."
        )
        pausar()
        return

    config = cargar_config()
    hora_limite = config["hora_entrada"]

    mostrar_titulo("REGISTRAR ASISTENCIA")
    mostrar_ayuda_registro_asistencia()
    print("Hora limite configurada:", hora_limite, ":00\n")

    dni = solicitar_dni()
    persona = buscar_por_dni(dni)
    if persona is None:
        mostrar_error(
            "Trabajador no encontrado o inactivo. Verifique el DNI o registre al personal."
        )
        pausar()
        return

    print("\n  Trabajador:", persona["nombre"])
    print("  Cargo:", persona["cargo"])

    print("\n  Hora de ingreso (0-23). Enter = hora actual (" + str(hora_actual()) + ")")
    texto_hora = input("  Hora: ").strip()
    if texto_hora == "":
        hora = hora_actual()
        print("  Usando hora actual:", hora)
    else:
        try:
            hora = int(texto_hora)
            if hora < 0 or hora > 23:
                raise ValueError
        except ValueError:
            mostrar_error("Hora invalida.")
            pausar()
            return

    fecha = solicitar_fecha()
    estado = calcular_estado(hora, hora_limite)

    registros = cargar_registros()
    registro = {
        "id": _siguiente_id_registro(registros),
        "personal_id": persona["id"],
        "nombre": persona["nombre"],
        "dni": persona["dni"],
        "cargo": persona["cargo"],
        "fecha": fecha,
        "hora": hora,
        "estado": estado,
    }
    registros.append(registro)
    guardar_registros(registros)

    mostrar_exito("Asistencia registrada")
    print("  Estado:", estado)
    print("  Fecha:", fecha)
    print("  Hora:", hora)
    pausar()


def configurar_horario():
    config = cargar_config()
    mostrar_titulo("CONFIGURAR HORARIO DE ENTRADA")
    print("Hora actual limite:", config["hora_entrada"], ":00")
    print("Los trabajadores que ingresen hasta esa hora seran PUNTUALES.\n")

    nueva_hora = solicitar_entero(
        "Nueva hora limite de entrada",
        1,
        12,
        ejemplo="8",
    )
    config["hora_entrada"] = nueva_hora
    guardar_config(config)
    mostrar_exito("Hora limite actualizada a " + str(nueva_hora) + ":00")
    pausar()
