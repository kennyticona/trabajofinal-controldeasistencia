import hashlib

from config import ARCHIVO_ADMIN, MAX_INTENTOS_LOGIN
from storage import cargar_json, existe_archivo, guardar_json
from ui import (
    mostrar_error,
    mostrar_exito,
    mostrar_separador,
    mostrar_titulo,
    pausar,
    solicitar_texto,
)


def _hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def existe_administrador():
    return existe_archivo(ARCHIVO_ADMIN)


def obtener_administrador():
    return cargar_json(ARCHIVO_ADMIN, None)


def crear_administrador():
    mostrar_titulo("CONFIGURACION INICIAL - ACCESSIQ")
    print("Bienvenido. Es la primera vez que usa el sistema.")
    print("Cree la cuenta del administrador principal.\n")
    print("Formato sugerido:")
    print("  Usuario : minimo 4 caracteres (ejemplo: admin.empresa)")
    print("  Password: minimo 4 caracteres (ejemplo: Access2026!)")
    mostrar_separador()

    while True:
        usuario = solicitar_texto(
            "Usuario administrador",
            ejemplo="admin.empresa",
            minimo=4,
        )
        password = solicitar_texto(
            "Contrasena",
            ejemplo="Access2026!",
            minimo=4,
            oculto=True,
        )
        confirmacion = solicitar_texto(
            "Confirmar contrasena",
            ejemplo="Access2026!",
            minimo=4,
            oculto=True,
        )

        if password != confirmacion:
            mostrar_error("Las contrasenas no coinciden. Intente de nuevo.")
            continue

        admin = {
            "usuario": usuario,
            "password_hash": _hash_password(password),
            "nombre": solicitar_texto(
                "Nombre completo del administrador",
                ejemplo="Maria Lopez Garcia",
                minimo=3,
            ),
        }
        guardar_json(ARCHIVO_ADMIN, admin)
        mostrar_exito("Administrador creado correctamente.")
        pausar()
        return True


def iniciar_sesion():
    admin = obtener_administrador()
    if admin is None:
        mostrar_error("No hay administrador configurado.")
        return False

    mostrar_titulo("INICIO DE SESION")
    print("Ingrese sus credenciales de administrador.\n")

    intentos = 0
    while intentos < MAX_INTENTOS_LOGIN:
        usuario = solicitar_texto("Usuario", ejemplo=admin.get("usuario", "admin"))
        password = solicitar_texto("Contrasena", ejemplo="********", oculto=True)

        if usuario == admin["usuario"] and _hash_password(password) == admin["password_hash"]:
            nombre = admin.get("nombre", usuario)
            mostrar_exito("Sesion iniciada. Hola, " + nombre + "!")
            pausar()
            return True

        intentos = intentos + 1
        restantes = MAX_INTENTOS_LOGIN - intentos
        if restantes > 0:
            mostrar_error("Credenciales incorrectas. Intentos restantes: " + str(restantes))
        else:
            mostrar_error("Acceso denegado.")
    return False
