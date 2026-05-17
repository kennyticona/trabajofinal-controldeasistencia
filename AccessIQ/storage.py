import json
import os
from datetime import datetime


def _ruta_absoluta(ruta):
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, ruta)


def asegurar_carpeta_data():
    carpeta = _ruta_absoluta("data")
    if not os.path.isdir(carpeta):
        os.makedirs(carpeta)
    return carpeta


def existe_archivo(ruta):
    return os.path.isfile(_ruta_absoluta(ruta))


def cargar_json(ruta, valor_default):
    asegurar_carpeta_data()
    ruta_completa = _ruta_absoluta(ruta)
    if not os.path.isfile(ruta_completa):
        return valor_default
    try:
        with open(ruta_completa, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, OSError):
        return valor_default


def guardar_json(ruta, datos):
    asegurar_carpeta_data()
    ruta_completa = _ruta_absoluta(ruta)
    with open(ruta_completa, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)


def fecha_hoy():
    return datetime.now().strftime("%d/%m/%Y")


def hora_actual():
    return datetime.now().hour
