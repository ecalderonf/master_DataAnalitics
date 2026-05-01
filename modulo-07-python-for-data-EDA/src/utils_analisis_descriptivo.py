'''
__resumen__ = "Funciones de análisis descriptivo: métricas estructurales, distribuciones univariantes y relaciones bivariantes para los datasets BANK y CUSTOMER."
__author__ = "ecalderonf"
__copyright__ = "Copyright 2026, ecalderonf"
__version__ = "beta"
__email__ = "edu.calderon.es@gmail.com"
__status__ = "Prototype"'''

import pandas as pd
import numpy as np

# ============================================
# 1) Número de filas y columnas
# ============================================
def metricas_dimensiones(df: pd.DataFrame, nombre: str):
    filas, columnas = df.shape
    print(f"[{nombre}] Dimensiones → filas: {filas}, columnas: {columnas}")
    return {"filas": filas, "columnas": columnas}


# ============================================
# 2) Porcentaje de nulos por columna
# ============================================
def metricas_nulos(df: pd.DataFrame, nombre: str):
    nulos = df.isna().mean() * 100
    print(f"[{nombre}] Porcentaje de nulos por columna (solo > 0%):")

    resultado = {}

    for col, pct in nulos.items():
        if pct > 0:
            pct_fmt = float(f"{pct:.2f}")   # ← FORMATO EXACTO: 2 enteros + 2 decimales
            print(f"   - {col}: {pct_fmt:.2f}%")
            resultado[col] = pct_fmt

    return resultado


# ============================================
# 3) Número de categorías por variable categórica
# ============================================
def metricas_categorias(df: pd.DataFrame, columnas_categoricas: list, nombre: str):
    resultado = {}
    print(f"[{nombre}] Número de categorías por columna categórica (excluyendo IDs/unívocas):")

    for col in columnas_categoricas:
        if col in df.columns:

            # Número de categorías
            n_cat = df[col].nunique(dropna=False)

            # Si todas las filas son distintas → es un ID → ignorar
            if n_cat == len(df):
                continue

            # Obtener lista de categorías (ordenadas)
            valores = sorted(df[col].dropna().unique().tolist())

            # Guardar en resultado
            resultado[col] = {
                "num_categorias": n_cat,
                "categorias": valores
            }

            # Imprimir en consola
            print(f"   - {col}: {n_cat} categorías")
            print(f"       valores: {valores}")

    return resultado


# ============================================
# 4) Columnas constantes o casi constantes
# ============================================
def metricas_columnas_constantes(df: pd.DataFrame, nombre: str, umbral: float = 0.99):
    resultado = {}
    print(f"[{nombre}] Columnas constantes o casi constantes:")
    for col in df.columns:
        proporciones = df[col].value_counts(normalize=True, dropna=False)
        max_prop = proporciones.iloc[0]
        if max_prop >= umbral:
            resultado[col] = float(max_prop)
            print(f"   - {col}: {max_prop:.4f} (constante o casi constante)")
    return resultado


# ============================================
# FUNCIÓN PRINCIPAL PARA AGRUPAR LAS 4 MÉTRICAS
# ============================================
def analisis_estructural(df: pd.DataFrame, nombre: str, columnas_categoricas: list):
    control = {}

    control["dimensiones"] = metricas_dimensiones(df, nombre)
    control["nulos"] = metricas_nulos(df, nombre)
    control["categorias"] = metricas_categorias(df, columnas_categoricas, nombre)
    control["columnas_constantes"] = metricas_columnas_constantes(df, nombre)

    return control

# ============================================
# 5) UNIVARIANTE BANK
# ============================================

def distribucion_tramos_numerica(df: pd.DataFrame,
                                 columna: str,
                                 bins: list,
                                 labels: list,
                                 nombre: str,
                                 titulo: str):
    serie = df[columna]
    tramos = pd.cut(serie, bins=bins, labels=labels, include_lowest=True)
    conteos = tramos.value_counts(dropna=False).sort_index()
    porcentajes = tramos.value_counts(normalize=True, dropna=False).sort_index() * 100

    print(f"[{nombre}] {titulo} ({columna})")
    resultado = {}
    for tramo, cnt in conteos.items():
        pct = float(f"{porcentajes[tramo]:.2f}")
        tramo_str = str(tramo)
        print(f"   - {tramo_str}: {cnt} registros ({pct:.2f}%)")
        resultado[tramo_str] = {"conteo": int(cnt), "porcentaje": pct}

    return resultado


def distribucion_categoricas(df: pd.DataFrame,
                             columnas: list,
                             nombre: str,
                             titulo: str):
    print(f"[{nombre}] {titulo}")
    resultado = {}

    for col in columnas:
        if col not in df.columns:
            continue

        vc = df[col].value_counts(dropna=False)
        vp = df[col].value_counts(normalize=True, dropna=False) * 100

        detalle = {}
        print(f"   - {col}:")
        for valor, cnt in vc.items():
            pct = float(f"{vp[valor]:.2f}")
            valor_str = str(valor)
            print(f"       {valor_str}: {cnt} registros ({pct:.2f}%)")
            detalle[valor_str] = {"conteo": int(cnt), "porcentaje": pct}

        resultado[col] = detalle

    return resultado


def analisis_univariante_bank(df: pd.DataFrame):
    control = {}

    # age por tramos
    bins_age = [0, 25, 35, 45, 55, 65, np.inf]
    labels_age = ['<=25', '26-35', '36-45', '46-55', '56-65', '65+']
    control["age_tramos"] = distribucion_tramos_numerica(
        df,
        columna="age",
        bins=bins_age,
        labels=labels_age,
        nombre="BANK",
        titulo="Distribución de age por tramos"
    )

    # duration por tramos (segundos)
    bins_dur = [0, 60, 180, 600, np.inf]
    labels_dur = ['<=60s', '61-180s', '181-600s', '>600s']
    control["duration_tramos"] = distribucion_tramos_numerica(
        df,
        columna="duration",
        bins=bins_dur,
        labels=labels_dur,
        nombre="BANK",
        titulo="Distribución de duration por tramos"
    )

    # frecuencias categóricas
    columnas_cat = [
        'job', 'marital', 'education', 'housing',
        'loan', 'contact', 'poutcome', 'y'
    ]
    control["frecuencias_categoricas"] = distribucion_categoricas(
        df,
        columnas=columnas_cat,
        nombre="BANK",
        titulo="Frecuencias de variables categóricas"
    )

    return control


# ============================================
# 6) UNIVARIANTE CUSTOMER
# ============================================

def distribucion_income_tramos(df: pd.DataFrame, nombre: str):
    serie = df["Income"].dropna()

    q1 = serie.quantile(1/3)
    q2 = serie.quantile(2/3)

    bins = [-np.inf, q1, q2, np.inf]
    labels = ['bajo', 'medio', 'alto']

    return distribucion_tramos_numerica(
        df,
        columna="Income",
        bins=bins,
        labels=labels,
        nombre=nombre,
        titulo="Distribución de Income por tramos (bajo/medio/alto)"
    )


def distribucion_numweb_tramos(df: pd.DataFrame, nombre: str):
    # baja: 0-3, media: 4-7, alta: 8+
    bins = [-1, 3, 7, np.inf]
    labels = ['baja', 'media', 'alta']

    return distribucion_tramos_numerica(
        df,
        columna="NumWebVisitsMonth",
        bins=bins,
        labels=labels,
        nombre=nombre,
        titulo="Distribución de NumWebVisitsMonth por tramos (baja/media/alta)"
    )


def distribucion_kid_teen(df: pd.DataFrame, columna: str, nombre: str):
    serie = df[columna].fillna(0)
    serie_tramos = serie.apply(lambda x: x if x in [0, 1, 2] else 3)

    mapa_labels = {0: '0', 1: '1', 2: '2', 3: '3+'}
    serie_labels = serie_tramos.map(mapa_labels)

    vc = serie_labels.value_counts(dropna=False)
    vp = serie_labels.value_counts(normalize=True, dropna=False) * 100

    print(f"[{nombre}] Distribución de {columna} (0,1,2,3+)")
    resultado = {}
    for valor, cnt in vc.items():
        pct = float(f"{vp[valor]:.2f}")
        print(f"   - {valor}: {cnt} registros ({pct:.2f}%)")
        resultado[valor] = {"conteo": int(cnt), "porcentaje": pct}

    return resultado


def analisis_univariante_customer(df: pd.DataFrame):
    control = {}

    control["income_tramos"] = distribucion_income_tramos(df, nombre="CUSTOMER")
    control["numweb_tramos"] = distribucion_numweb_tramos(df, nombre="CUSTOMER")

    control["kidhome_tramos"] = distribucion_kid_teen(
        df,
        columna="Kidhome",
        nombre="CUSTOMER"
    )

    control["teenhome_tramos"] = distribucion_kid_teen(
        df,
        columna="Teenhome",
        nombre="CUSTOMER"
    )

    return control

# ============================================
# 7) MÉTRICAS BIVARIANTES - HELPERS
# ============================================

def _tasa_conversion_por_grupo(df: pd.DataFrame,
                               columna_grupo: str,
                               nombre: str,
                               titulo: str):
    """
    Calcula tasa de conversión (y == 'yes') por grupo de columna_grupo.
    """
    if 'y' not in df.columns:
        print(f"[{nombre}] {titulo} - columna 'y' no encontrada, se omite.")
        return {}

    df_valid = df.dropna(subset=[columna_grupo])
    if df_valid.empty:
        print(f"[{nombre}] {titulo} - sin datos válidos para {columna_grupo}.")
        return {}

    conv = (df_valid['y'] == 'yes').astype(int)
    grp = df_valid.groupby(columna_grupo)

    print(f"[{nombre}] {titulo}")
    resultado = {}
    for g, sub in grp:
        n = len(sub)
        tasa = float(f"{conv.loc[sub.index].mean() * 100:.2f}")
        g_str = str(g)
        print(f"   - {g_str}: {n} registros, tasa conversión = {tasa:.2f}%")
        resultado[g_str] = {"n": int(n), "tasa_conversion": tasa}

    return resultado


# ============================================
# 8) MÉTRICAS BIVARIANTES - BANK
# ============================================

def analisis_bivariante_bank(df: pd.DataFrame):
    control = {}

    # 1) Tasa de conversión por tramos de age
    bins_age = [0, 25, 35, 45, 55, 65, np.inf]
    labels_age = ['<=25', '26-35', '36-45', '46-55', '56-65', '65+']
    age_tramos = pd.cut(df['age'], bins=bins_age, labels=labels_age, include_lowest=True)
    df_age = df.copy()
    df_age['age_tramo'] = age_tramos

    control["tasa_conv_age_tramos"] = _tasa_conversion_por_grupo(
        df_age,
        columna_grupo="age_tramo",
        nombre="BANK",
        titulo="Tasa de conversión por tramos de age"
    )

    # 2) Tasa de conversión por job
    control["tasa_conv_job"] = _tasa_conversion_por_grupo(
        df,
        columna_grupo="job",
        nombre="BANK",
        titulo="Tasa de conversión por job"
    )

    # 3) Tasa de conversión por contact
    control["tasa_conv_contact"] = _tasa_conversion_por_grupo(
        df,
        columna_grupo="contact",
        nombre="BANK",
        titulo="Tasa de conversión por contact"
    )

    # 3b) Tasa de conversión por tramos de duration
    bins_dur = [0, 60, 180, 600, np.inf]
    labels_dur = ['<=60s', '61-180s', '181-600s', '>600s']
    dur_tramos = pd.cut(df['duration'], bins=bins_dur, labels=labels_dur, include_lowest=True)
    df_dur = df.copy()
    df_dur['duration_tramo'] = dur_tramos

    control["tasa_conv_duration_tramos"] = _tasa_conversion_por_grupo(
        df_dur,
        columna_grupo="duration_tramo",
        nombre="BANK",
        titulo="Tasa de conversión por tramos de duration"
    )

    # 4) Tasa de conversión por campaign (pocas vs muchas llamadas)
    # Definimos: pocas = campaign <= 2, muchas = campaign > 2
    df_camp = df.copy()
    df_camp['campaign_grupo'] = np.where(df_camp['campaign'] <= 2, 'pocas', 'muchas')

    control["tasa_conv_campaign"] = _tasa_conversion_por_grupo(
        df_camp,
        columna_grupo="campaign_grupo",
        nombre="BANK",
        titulo="Tasa de conversión por campaign (pocas vs muchas llamadas)"
    )

    return control


# ============================================
# MÉTRICAS BIVARIANTES INTERNAS - CUSTOMER
# ============================================

def analisis_bivariante_interno_customer(df: pd.DataFrame):
    control = {}

    # --- Tramos Income ---
    serie_income = df["Income"].dropna()
    q1 = serie_income.quantile(1/3)
    q2 = serie_income.quantile(2/3)
    bins_inc = [-np.inf, q1, q2, np.inf]
    labels_inc = ['bajo', 'medio', 'alto']
    df["income_tramo"] = pd.cut(df["Income"], bins=bins_inc, labels=labels_inc, include_lowest=True)

    # --- Tramos NumWebVisitsMonth ---
    bins_web = [-1, 3, 7, np.inf]
    labels_web = ['baja', 'media', 'alta']
    df["numweb_tramo"] = pd.cut(df["NumWebVisitsMonth"], bins=bins_web, labels=labels_web, include_lowest=True)

    # ============================================================
    # 1) Income (tramos) vs NumWebVisitsMonth (tramos)
    # ============================================================
    print("[CUSTOMER] Income (tramos) vs NumWebVisitsMonth (tramos)")
    tabla1 = pd.crosstab(df["income_tramo"], df["numweb_tramo"], normalize="index") * 100
    resultado1 = {}
    for fila in tabla1.index:
        print(f"   - {fila}:")
        resultado1[str(fila)] = {}
        for col, val in tabla1.loc[fila].items():
            pct = float(f"{val:.2f}")
            print(f"       {col}: {pct:.2f}%")
            resultado1[str(fila)][str(col)] = pct
    control["income_vs_numweb"] = resultado1

    # ============================================================
    # 2) Income (tramos) vs Kidhome
    # ============================================================
    print("[CUSTOMER] Income (tramos) vs Kidhome")
    tabla2 = pd.crosstab(df["income_tramo"], df["Kidhome"], normalize="index") * 100
    resultado2 = {}
    for fila in tabla2.index:
        print(f"   - {fila}:")
        resultado2[str(fila)] = {}
        for col, val in tabla2.loc[fila].items():
            pct = float(f"{val:.2f}")
            print(f"       {col}: {pct:.2f}%")
            resultado2[str(fila)][str(col)] = pct
    control["income_vs_kidhome"] = resultado2

    # ============================================================
    # 3) NumWebVisitsMonth (tramos) vs Teenhome
    # ============================================================
    print("[CUSTOMER] NumWebVisitsMonth (tramos) vs Teenhome")
    tabla3 = pd.crosstab(df["numweb_tramo"], df["Teenhome"], normalize="index") * 100
    resultado3 = {}
    for fila in tabla3.index:
        print(f"   - {fila}:")
        resultado3[str(fila)] = {}
        for col, val in tabla3.loc[fila].items():
            pct = float(f"{val:.2f}")
            print(f"       {col}: {pct:.2f}%")
            resultado3[str(fila)][str(col)] = pct
    control["numweb_vs_teenhome"] = resultado3

    return control

