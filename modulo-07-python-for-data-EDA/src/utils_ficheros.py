'''__resumen__ = "Funciones utilitarias para validación de carpetas y ficheros, copia de datos, conversión de estructuras a tablas HTML y generación del informe EDA en formato HTML."
__author__ = "ecalderonf"
__copyright__ = "Copyright 2026, ecalderonf"
__version__ = "beta"
__email__ = "edu.calderon.es@gmail.com"
__status__ = "Prototype"'''


import os
import shutil
import json
from typing import Any, Dict

RUTA_INFORME_EDA = os.path.join("reports", "informe_EDA.html")

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


def _dict_to_html_table(data: Dict[str, Any], titulo: str = "") -> str:
    html = []

    if titulo:
        html.append(f"<h3>{titulo}</h3>")

    html.append("<table border='1' cellspacing='0' cellpadding='6' style='border-collapse: collapse;'>")
    html.append("<tr><th>Clave</th><th>Valor</th></tr>")

    for clave, valor in data.items():

        # Caso 1: valor simple
        if not isinstance(valor, (list, dict)):
            html.append(f"<tr><td>{clave}</td><td>{valor}</td></tr>")
            continue

        # Caso 2: valor es lista
        if isinstance(valor, list):
            # Convertimos la lista en tabla de una columna
            sub = ["<table border='1' cellspacing='0' cellpadding='4' style='border-collapse: collapse;'>"]
            sub.append("<tr><th>Elemento</th></tr>")
            for item in valor:
                sub.append(f"<tr><td>{item}</td></tr>")
            sub.append("</table>")
            html.append(f"<tr><td>{clave}</td><td>{''.join(sub)}</td></tr>")
            continue

        # Caso 3: valor es diccionario → tabla con columnas dinámicas
        if isinstance(valor, dict):
            sub = ["<table border='1' cellspacing='0' cellpadding='4' style='border-collapse: collapse;'>"]

            # columnas = claves internas
            columnas = list(valor.keys())
            sub.append("<tr>" + "".join(f"<th>{c}</th>" for c in columnas) + "</tr>")

            # fila = valores internos
            fila = []
            for c in columnas:
                v = valor[c]
                if isinstance(v, list):
                    v = ", ".join(str(x) for x in v)
                fila.append(f"<td>{v}</td>")
            sub.append("<tr>" + "".join(fila) + "</tr>")

            sub.append("</table>")
            html.append(f"<tr><td>{clave}</td><td>{''.join(sub)}</td></tr>")
            continue

    html.append("</table>")
    return "\n".join(html)


def generar_informe_eda(
    data_estructural: Dict[str, Any],
    data_univariante: Dict[str, Any],
    data_bivariante: Dict[str, Any],
    data_visualizacion: Dict[str, Any],
    ruta_salida: str = RUTA_INFORME_EDA,
) -> str:
    """
    Genera un informe HTML sencillo con los resultados del EDA
    y lo guarda en `ruta_salida`. Devuelve la ruta del fichero generado.
    """
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

    partes = []

    partes.append("<!DOCTYPE html>")
    partes.append("<html lang='es'>")
    partes.append("<head>")
    partes.append("<meta charset='UTF-8'>")
    partes.append("<title>Informe EDA</title>")
    partes.append("<style>")
    partes.append("body { font-family: Arial, sans-serif; margin: 20px; color: #333; }")
    partes.append("h1, h2, h3, h4 { color: #333; }")
    partes.append("table { border-collapse: collapse; margin-bottom: 25px; width: 100%; font-size: 14px; }")
    partes.append("table th { background-color: #D4670F; color: #333; padding: 8px; border: 1px solid #D4670F; text-align: left; }")
    partes.append("table td { background-color: #FFD48A; padding: 8px; border: 1px solid #D4670F; }")
    partes.append("table tr:nth-child(even) td { background-color: #F7C07C; }")
    partes.append("img { max-width: 100%; height: auto; margin-top: 10px; border: 1px solid #D4670F; padding: 4px; background: #FFF7EF; }")
    partes.append("</style>")
    partes.append("</head>")
    partes.append("<body>")

    partes.append("<h1>Informe de Análisis Exploratorio de Datos (EDA)</h1>")

    # Estructural
    partes.append("<h2>Análisis estructural</h2>")
    partes.append(_dict_to_html_table(data_estructural))

    partes.append("<h3>Interpretación</h3>")    
    partes.append('<textarea rows="10" style="width:100%; font-size:14px;" readonly>')
    partes.append("El dataset BANK presenta una estructura rica en variables categóricas y un volumen notable de nulos en columnas numéricas clave, lo que es habitual en campañas telefónicas masivas. La variedad de categorías en job, education y marital sugiere perfiles muy heterogéneos. CUSTOMER, en cambio, es un dataset compacto, sin nulos y con variables numéricas limpias, lo que facilita su uso como dataset auxiliar. No se detectan columnas constantes en ninguno de los dos, lo que indica buena variabilidad estructural.")
    partes.append("</textarea>")

    # Univariante
    partes.append("<h2>Análisis univariante</h2>")
    partes.append(_dict_to_html_table(data_univariante))

    partes.append("<h3>Interpretación</h3>")    
    partes.append('<textarea rows="10" style="width:100%; font-size:14px;" readonly>')
    partes.append("Las distribuciones muestran patrones claros: en BANK, la edad se concentra en adultos jóvenes y medios, mientras que la duración de las llamadas se agrupa mayoritariamente entre 1 y 10 minutos. Las categorías dominantes (admin., blue-collar, technician, married, university.degree) reflejan perfiles típicos de campañas bancarias. La conversión global es baja, coherente con campañas telefónicas reales. CUSTOMER presenta distribuciones extremadamente uniformes, lo que indica ausencia de sesgos fuertes en ingresos, visitas web o estructura familiar.")
    partes.append("</textarea>")

    # Bivariante
    partes.append("<h2>Análisis bivariante</h2>")
    partes.append(_dict_to_html_table(data_bivariante))

    partes.append("<h3>Interpretación</h3>")    
    partes.append('<textarea rows="10" style="width:100%; font-size:14px;" readonly>')
    partes.append("En BANK emergen patrones de negocio muy definidos: los extremos de edad convierten mejor, ciertas profesiones destacan (student, retired), el canal celular supera claramente al telefónico y las llamadas largas muestran tasas de conversión muy superiores. Además, la presión de campaña afecta negativamente: más llamadas reducen la conversión. En CUSTOMER, las relaciones internas son prácticamente planas: ingresos, visitas web y estructura familiar no muestran asociaciones relevantes, lo que confirma que es un dataset homogéneo y estable.")
    partes.append("</textarea>")    

    # Visualización
    partes.append("<h2>Visualización de datos</h2>")
    for origen, ruta_img in data_visualizacion.items():
        partes.append(f"<h3>{origen}</h3>")
        ruta_rel = os.path.relpath(ruta_img, os.path.dirname(ruta_salida))
        partes.append(f"<p>Gráfica generada:</p>")
        partes.append(f"<img src='{ruta_rel}' alt='Gráfica {origen}'>")

    partes.append("</body>")
    partes.append("</html>")

    html_final = "\n".join(partes)

    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(html_final)

    return ruta_salida