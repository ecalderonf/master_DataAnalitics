'''__resumen__ = "Funciones de carga, conversión de tipos, tratamiento de fechas, gestión de nulos y duplicados, normalización de categorías y limpieza específica para los datasets BANK y CUSTOMER."
__author__ = "ecalderonf"
__copyright__ = "Copyright 2026, ecalderonf"
__version__ = "beta"
__email__ = "edu.calderon.es@gmail.com"
__status__ = "Prototype"'''

import pandas as pd
import numpy as np


# ============================================================
# CARGA DE DATOS
# ============================================================

def cargar_csv(ruta: str) -> pd.DataFrame:
    try:
        return pd.read_csv(ruta)
    except Exception as e:
        print(f'Error leyendo CSV {ruta}: {e}')
        raise


def cargar_excel(ruta: str) -> pd.DataFrame:
    try:
        # Lee todas las hojas en un dict {nombre_hoja: DataFrame}
        return pd.read_excel(ruta, sheet_name=None)
    except Exception as e:
        print(f'Error leyendo Excel {ruta}: {e}')
        raise


# ============================================================
# CONVERSIONES DE TIPOS
# ============================================================

def convertir_comas_a_float(df: pd.DataFrame, columnas: list[str]):
    control = {}
    for col in columnas:
        antes = df[col].isna().sum()
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(',', '.', regex=False)
            .replace('nan', np.nan)
            .astype(float)
        )
        despues = df[col].isna().sum()
        control[col] = {'nulos_creados': max(0, despues - antes)}
    return df, control


def convertir_a_int(df: pd.DataFrame, columnas: list[str]):
    control = {}
    for col in columnas:
        antes = df[col].isna().sum()
        df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
        despues = df[col].isna().sum()
        control[col] = {'nulos_creados': max(0, despues - antes)}
    return df, control


def convertir_a_float(df: pd.DataFrame, columnas: list[str]):
    control = {}
    for col in columnas:
        antes = df[col].isna().sum()
        df[col] = pd.to_numeric(df[col], errors='coerce')
        despues = df[col].isna().sum()
        control[col] = {'nulos_creados': max(0, despues - antes)}
    return df, control


# ============================================================
# FECHAS
# ============================================================

def convertir_fecha_espanol(df: pd.DataFrame, columna: str):
    meses = {
        'enero': '01', 'febrero': '02', 'marzo': '03', 'abril': '04',
        'mayo': '05', 'junio': '06', 'julio': '07', 'agosto': '08',
        'septiembre': '09', 'octubre': '10', 'noviembre': '11', 'diciembre': '12'
    }

    def parsear(fecha):
        if pd.isna(fecha):
            return pd.NaT
        try:
            dia, mes_txt, anio = fecha.split('-')
            mes = meses.get(mes_txt.lower(), None)
            if mes is None:
                return pd.NaT
            return pd.to_datetime(f'{anio}-{mes}-{dia}', format='%Y-%m-%d')
        except Exception:
            return pd.NaT

    df[columna] = df[columna].apply(parsear)
    return df


def convertir_fecha_excel(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    dtype_col = df[columna].dtype

    # Si es numérica → tratamos como número de días de Excel
    if np.issubdtype(dtype_col, np.number):
        df[columna] = pd.to_datetime(
            df[columna],
            errors='coerce',
            unit='D',
            origin='1899-12-30'
        )
    else:
        # Si no es numérica (string, datetime, etc.) → conversión estándar
        df[columna] = pd.to_datetime(df[columna], errors='coerce')

    return df


# ============================================================
# NULOS Y DUPLICADOS
# ============================================================

def rellenar_nulos(df: pd.DataFrame, estrategia: dict[str, any]):
    control = {}
    for col, valor in estrategia.items():
        antes = df[col].isna().sum()
        df[col] = df[col].fillna(valor)
        despues = df[col].isna().sum()
        control[col] = {'nulos_rellenados': antes - despues}
    return df, control


def eliminar_filas_con_nulos(df: pd.DataFrame, columnas: list[str]):
    antes = len(df)
    df = df.dropna(subset=columnas)
    despues = len(df)
    control = {'filas_eliminadas': antes - despues}
    return df, control


def eliminar_duplicados(df: pd.DataFrame, columna_id: str):
    antes = len(df)
    df = df.drop_duplicates(subset=[columna_id], keep='first')
    despues = len(df)
    control = {'duplicados_eliminados': antes - despues}
    return df, control


# ============================================================
# CATEGORÍAS Y RENOMBRADO
# ============================================================

def normalizar_categorias(df: pd.DataFrame, columna: str, mapa: dict):
    df[columna] = df[columna].replace(mapa)
    return df


def renombrar_columnas(df: pd.DataFrame, mapa: dict[str, str]):
    df = df.rename(columns=mapa)
    control = {'columnas_renombradas': len(mapa)}
    return df, control


# ============================================================
# FUNCIONES ESPECÍFICAS PARA CADA FUENTE
# ============================================================

def limpiar_bank_data(df: pd.DataFrame):
    control_total = {}

    # ============================
    # 1) COMAS → FLOAT
    # ============================
    df, c1 = convertir_comas_a_float(df, ['cons.price.idx', 'cons.conf.idx', 'euribor3m'])
    control_total['comas_a_float'] = c1

    # ============================
    # 2) FECHA (ESPAÑOL)
    # ============================
    df = convertir_fecha_espanol(df, 'date')

    # ============================
    # 3) NUMÉRICAS (todas las que deben serlo)
    # ============================
    columnas_numericas = [
        'age', 'duration', 'campaign', 'pdays', 'previous',
        'emp.var.rate', 'cons.price.idx', 'cons.conf.idx',
        'euribor3m', 'nr.employed'
    ]

    c_num = {}
    for col in columnas_numericas:
        antes = df[col].isna().sum()
        df[col] = pd.to_numeric(df[col], errors='coerce')
        despues = df[col].isna().sum()
        c_num[col] = {'nulos_creados': max(0, despues - antes)}

    control_total['convertir_numericas'] = c_num

    # ============================
    # 4) CATEGÓRICAS → rellenar NaN con 'UNKNOWN'
    # ============================
    columnas_categoricas = [
        'job', 'marital', 'education', 'default',
        'housing', 'loan', 'contact', 'poutcome', 'y'
    ]

    c_cat = {}
    for col in columnas_categoricas:
        antes = df[col].isna().sum()
        df[col] = df[col].fillna('UNKNOWN')
        despues = df[col].isna().sum()
        c_cat[col] = {'rellenados': antes - despues}

    control_total['categoricas'] = c_cat

    # ============================
    # 5) NORMALIZACIÓN DE BINARIOS (default, housing, loan)
    # ============================
    mapa_default = {'0.0': 0, '1.0': 1, 0.0: 0, 1.0: 1}
    df = normalizar_categorias(df, 'default', mapa_default)
    df = normalizar_categorias(df, 'housing', mapa_default)
    df = normalizar_categorias(df, 'loan', mapa_default)

    # ============================
    # 6) ELIMINAR DUPLICADOS POR ID
    # ============================
    df, c3 = eliminar_duplicados(df, 'id_')
    control_total['duplicados'] = c3

    # ============================
    # 7) ELIMINAR COLUMNAS INÚTILES
    # ============================
    columnas_a_eliminar = ['Unnamed: 0', 'latitude', 'longitude']
    existentes = [c for c in columnas_a_eliminar if c in df.columns]

    df = df.drop(columns=existentes)

    control_total['columnas_eliminadas'] = {
        'columnas': existentes,
        'total_eliminadas': len(existentes)
    }    

    return df, control_total



def limpiar_customer_data(df: pd.DataFrame):
    control_total = {}

    # ============================
    # 1) FECHA (Excel → datetime)
    # ============================
    df = convertir_fecha_excel(df, 'Dt_Customer')

    # ============================
    # 2) NUMÉRICAS
    # ============================
    columnas_numericas = ['Income', 'Kidhome', 'Teenhome', 'NumWebVisitsMonth']

    c_num = {}
    for col in columnas_numericas:
        antes = df[col].isna().sum()
        df[col] = pd.to_numeric(df[col], errors='coerce')
        despues = df[col].isna().sum()
        c_num[col] = {'nulos_creados': max(0, despues - antes)}

    control_total['convertir_numericas'] = c_num

    # ============================
    # 3) CATEGÓRICAS
    # ============================
    # En este dataset, la única categórica real es ID
    columnas_categoricas = ['ID']

    c_cat = {}
    for col in columnas_categoricas:
        antes = df[col].isna().sum()
        df[col] = df[col].fillna('UNKNOWN')
        despues = df[col].isna().sum()
        c_cat[col] = {'rellenados': antes - despues}

    control_total['categoricas'] = c_cat

    # ============================
    # 4) ELIMINAR DUPLICADOS POR ID
    # ============================
    df, c3 = eliminar_duplicados(df, 'ID')
    control_total['duplicados'] = c3

    # ============================
    # 5) ELIMINAR COLUMNAS INÚTILES
    # ============================
    columnas_a_eliminar = ['Unnamed: 0']
    existentes = [c for c in columnas_a_eliminar if c in df.columns]

    df = df.drop(columns=existentes)

    control_total['columnas_eliminadas'] = {
        'columnas': existentes,
        'total_eliminadas': len(existentes)
    }    

    return df, control_total


# ============================================================
# GUARDADO
# ============================================================

def guardar_df(df: pd.DataFrame, ruta_salida: str) -> bool:
    try:
        if ruta_salida.lower().endswith('.xlsx'):
            df.to_excel(ruta_salida, index=False)
        else:
            df.to_csv(ruta_salida, index=False)
        return True
    except Exception:
        return False
