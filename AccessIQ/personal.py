from config import ARCHIVO_PERSONAL
from storage import cargar_json, guardar_json
from ui import (
    mostrar_ayuda_registro_personal,
    mostrar_error,
    mostrar_exito,
    mostrar_info,
    mostrar_separador,
    mostrar_titulo,
    pausar,
    solicitar_dni,
    solicitar_texto,
)


def cargar_personal():
    return cargar_json(ARCHIVO_PERSONAL, [])


def guardar_personal(lista):
    guardar_json(ARCHIVO_PERSONAL, lista)


def _siguiente_id(lista):
    if len(lista) == 0:
        return 1
    maximo = 0
    i = 0
    while i < len(lista):
        if lista[i]["id"] > maximo:
            maximo = lista[i]["id"]
        i = i + 1
    return maximo + 1


def buscar_por_dni(dni):
    lista = cargar_personal()
    i = 0
    while i < len(lista):
        if lista[i]["dni"] == dni and lista[i]["activo"]:
            return lista[i]
        i = i + 1
    return None


def buscar_por_id(personal_id):
    lista = cargar_personal()
    i = 0
    while i < len(lista):
        if lista[i]["id"] == personal_id:
            return lista[i]
        i = i + 1
    return None


def registrar_personal():
    mostrar_titulo("REGISTRAR PERSONAL")
    mostrar_ayuda_registro_personal()

    nombre = solicitar_texto(
        "Nombre completo (MAYUSCULAS)",
        ejemplo="RAMOS CUSTODIO CRISTIAN WALTER",
        minimo=5,
    ).upper()

    dni = solicitar_dni()

    if buscar_por_dni(dni) is not None:
        mostrar_error("Ya existe un trabajador activo con ese DNI.")
        pausar()
        return

    cargo = solicitar_texto(
        "Cargo o area",
        ejemplo="Ventas",
        minimo=2,
    )

    from storage import fecha_hoy

    lista = cargar_personal()
    nuevo = {
        "id": _siguiente_id(lista),
        "nombre": nombre,
        "dni": dni,
        "cargo": cargo,
        "activo": True,
        "fecha_registro": fecha_hoy(),
    }
    lista.append(nuevo)
    guardar_personal(lista)
    mostrar_exito("Personal registrado: " + nombre)
    pausar()


def listar_personal(solo_activos=True):
    lista = cargar_personal()
    mostrar_titulo("LISTA DE PERSONAL")

    if len(lista) == 0:
        mostrar_info("No hay personal registrado. Use la opcion 1 para agregar.")
        pausar()
        return

    activos = 0
    i = 0
    while i < len(lista):
        persona = lista[i]
        if solo_activos and not persona["activo"]:
            i = i + 1
            continue

        if persona["activo"]:
            activos = activos + 1

        estado_txt = "ACTIVO" if persona["activo"] else "INACTIVO"
        mostrar_separador("-", 50)
        print("ID:", persona["id"])
        print("Nombre:", persona["nombre"])
        print("DNI:", persona["dni"])
        print("Cargo:", persona["cargo"])
        print("Registrado:", persona["fecha_registro"])
        print("Estado:", estado_txt)
        i = i + 1

    print()
    mostrar_separador("-", 50)
    print("Total mostrados:", activos if solo_activos else len(lista))
    pausar()


def desactivar_personal():
    mostrar_titulo("DESACTIVAR PERSONAL")
    print("El trabajador no se elimina, solo se marca como inactivo.\n")
    dni = solicitar_dni()

    lista = cargar_personal()
    encontrado = False
    i = 0
    while i < len(lista):
        if lista[i]["dni"] == dni:
            encontrado = True
            if not lista[i]["activo"]:
                mostrar_info("Este trabajador ya estaba inactivo.")
            else:
                lista[i]["activo"] = False
                guardar_personal(lista)
                mostrar_exito("Trabajador desactivado: " + lista[i]["nombre"])
            break
        i = i + 1

    if not encontrado:
        mostrar_error("No se encontro personal con ese DNI.")
    pausar()


def contar_personal_activo():
    lista = cargar_personal()
    total = 0
    i = 0
    while i < len(lista):
        if lista[i]["activo"]:
            total = total + 1
        i = i + 1
    return total
