import os
import shutil

# ============================
# VALIDACIÓN DE CARPETAS
# ============================

def validar_o_crear_carpeta(ruta_carpeta: str) -> bool:
    if os.path.isdir(ruta_carpeta):
        return True
    try:
        os.makedirs(ruta_carpeta)
        return True
    except Exception:
        return False


def validar_todas_las_carpetas(lista_carpetas: list) -> bool:
    for carpeta in lista_carpetas:
        if not validar_o_crear_carpeta(carpeta):
            return False
    return True


# ============================
# VALIDACIÓN DE FICHEROS
# ============================

def validar_fichero(ruta_fichero: str) -> bool:
    return os.path.isfile(ruta_fichero)


def validar_todos_los_ficheros(lista_ficheros: list) -> bool:
    for fichero in lista_ficheros:
        if not validar_fichero(fichero):
            return False
    return True


def validar_fichero_no_vacio(ruta_fichero: str) -> bool:
    try:
        return os.path.getsize(ruta_fichero) > 0
    except Exception:
        return False


def validar_ficheros_no_vacios(lista_ficheros: list) -> bool:
    for fichero in lista_ficheros:
        if not validar_fichero_no_vacio(fichero):
            return False
    return True


def validar_fichero_legible(ruta_fichero: str) -> bool:
    encodings_a_probar = [
        'utf-8',
        'latin-1',
        'windows-1252'
    ]

    try:
        with open(ruta_fichero, 'rb') as f:
            raw = f.read()

        for enc in encodings_a_probar:
            try:
                raw.decode(enc)
                return True
            except Exception:
                continue

        raise Exception('No se pudo decodificar el fichero con ninguna codificación estándar.')

    except Exception as e:
        raise e


def validar_ficheros_legibles(lista_ficheros: list) -> bool:
    for fichero in lista_ficheros:
        if not validar_fichero_legible(fichero):
            return False
    return True


# ============================
# COPIA DE FICHEROS
# ============================

def copiar_fichero(origen: str, destino: str) -> bool:
    try:
        shutil.copy2(origen, destino)
        return True
    except Exception:
        return False


def copiar_lista_ficheros(lista_origen: list, lista_destino: list) -> bool:
    for origen, destino in zip(lista_origen, lista_destino):
        if not copiar_fichero(origen, destino):
            return False
    return True
