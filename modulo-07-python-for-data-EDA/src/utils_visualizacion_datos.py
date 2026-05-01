'''__resumen__ = "Funciones de visualización para los datasets BANK y CUSTOMER: generación de subplots, gráficos de barras, pie charts y heatmaps con paleta pastel para su inclusión en el informe EDA."
__author__ = "ecalderonf"
__copyright__ = "Copyright 2026, ecalderonf"
__version__ = "beta"
__email__ = "edu.calderon.es@gmail.com"
__status__ = "Prototype"
'''

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def _tramos_age(df):
    bins = [0, 25, 35, 45, 55, 65, np.inf]
    labels = ['<=25', '26-35', '36-45', '46-55', '56-65', '65+']
    return pd.cut(df["age"], bins=bins, labels=labels, include_lowest=True)


def _tramos_duration(df):
    bins = [0, 60, 180, 600, np.inf]
    labels = ['<=60s', '61-180s', '181-600s', '>600s']
    return pd.cut(df["duration"], bins=bins, labels=labels, include_lowest=True)


def visualizar_bank_subplots(df_bank: pd.DataFrame):
    """
    Muestra en UNA sola figura varias gráficas de BANK
    usando una rejilla 2x3 de subplots.
    """

    # Paleta pastel (naranjas/amarillos suaves)
    colores = [
        "#FFCC80",  # naranja pastel
        "#FFE0B2",  # crema pastel
        "#FFD180",  # naranja claro
        "#FFECB3",  # amarillo suave
        "#FFE082",  # amarillo pastel
        "#FFB74D"   # naranja medio pastel
    ]

    ruta_salida = os.path.join("reports", "img")
    os.makedirs(ruta_salida, exist_ok=True)

    fig, axes = plt.subplots(2, 3, figsize=(18, 8))
    fig.suptitle("BANK – Métricas", fontsize=14)

    # 1) age por tramos
    ax = axes[0, 0]
    age_tramos = _tramos_age(df_bank)
    vc_age = age_tramos.value_counts().sort_index()
    sns.barplot(x=vc_age.index.astype(str), y=vc_age.values, ax=ax, color=colores[0])
    ax.set_title("age por tramos")
    ax.set_xlabel("")
    ax.set_ylabel("conteo")
    ax.tick_params(axis='x', rotation=45)

    # 2) duration por tramos
    ax = axes[0, 1]
    dur_tramos = _tramos_duration(df_bank)
    vc_dur = dur_tramos.value_counts().sort_index()
    sns.barplot(x=vc_dur.index.astype(str), y=vc_dur.values, ax=ax, color=colores[1])
    ax.set_title("duration por tramos")
    ax.set_xlabel("")
    ax.set_ylabel("conteo")
    ax.tick_params(axis='x', rotation=45)

    # 3) job (top 10)
    ax = axes[0, 2]
    vc_job = df_bank["job"].value_counts().sort_values(ascending=False).head(10)
    sns.barplot(y=vc_job.index.astype(str), x=vc_job.values, ax=ax, color=colores[2])
    ax.set_title("job (top 10)")
    ax.set_xlabel("conteo")
    ax.set_ylabel("job")

    # 4) marital
    ax = axes[1, 0]
    vc_mar = df_bank["marital"].value_counts()
    sns.barplot(x=vc_mar.index.astype(str), y=vc_mar.values, ax=ax, color=colores[3])
    ax.set_title("marital")
    ax.set_xlabel("")
    ax.set_ylabel("conteo")
    ax.tick_params(axis='x', rotation=45)

    # 5) education
    ax = axes[1, 1]
    vc_edu = df_bank["education"].value_counts()
    sns.barplot(x=vc_edu.index.astype(str), y=vc_edu.values, ax=ax, color=colores[4])
    ax.set_title("education")
    ax.set_xlabel("")
    ax.set_ylabel("conteo")
    ax.tick_params(axis='x', rotation=90)

    # 6) y (respuesta) → PIE CHART
    ax = axes[1, 2]
    vc_y = df_bank["y"].value_counts()
    ax.pie(
        vc_y.values,
        labels=vc_y.index.astype(str),
        autopct="%1.1f%%",
        colors=[colores[5], colores[0]],
        startangle=90
    )
    ax.set_title("y (respuesta)")

    fig.savefig(os.path.join(ruta_salida, "bank_metricas.png"))

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()





def _tramos_income(df):
    serie = df["Income"].dropna()
    q1 = serie.quantile(1/3)
    q2 = serie.quantile(2/3)
    bins = [-np.inf, q1, q2, np.inf]
    labels = ['bajo', 'medio', 'alto']
    return pd.cut(df["Income"], bins=bins, labels=labels, include_lowest=True)


def _tramos_numweb(df):
    bins = [-1, 3, 7, np.inf]
    labels = ['baja', 'media', 'alta']
    return pd.cut(df["NumWebVisitsMonth"], bins=bins, labels=labels, include_lowest=True)


def visualizar_customer_subplots(df_cust: pd.DataFrame):
    """
    Muestra en UNA sola figura varias gráficas de CUSTOMER
    usando una rejilla 2x3 de subplots.
    """

    # Paleta pastel (idéntica a BANK)
    colores = [
        "#FFCC80",  # naranja pastel
        "#FFE0B2",  # crema pastel
        "#FFD180",  # naranja claro
        "#FFECB3",  # amarillo suave
        "#FFE082",  # amarillo pastel
        "#FFB74D"   # naranja medio pastel
    ]

    ruta_salida = os.path.join("reports", "img")
    os.makedirs(ruta_salida, exist_ok=True)

    fig, axes = plt.subplots(2, 3, figsize=(18, 8))
    fig.suptitle("CUSTOMER – Métricas", fontsize=14)

    # 1) Income por tramos → PIE
    ax = axes[0, 0]
    income_tramos = _tramos_income(df_cust)
    vc_inc = income_tramos.value_counts().sort_index()
    ax.pie(
        vc_inc.values,
        labels=vc_inc.index.astype(str),
        autopct="%1.1f%%",
        colors=[colores[0], colores[1], colores[2]],
        startangle=90
    )
    ax.set_title("Income por tramos")

    # 2) NumWebVisitsMonth por tramos → BARRAS (se mantiene)
    ax = axes[0, 1]
    web_tramos = _tramos_numweb(df_cust)
    vc_web = web_tramos.value_counts().sort_index()
    sns.barplot(x=vc_web.index.astype(str), y=vc_web.values, ax=ax, color=colores[3])
    ax.set_title("NumWebVisitsMonth por tramos")
    ax.set_xlabel("")
    ax.set_ylabel("conteo")
    ax.tick_params(axis='x', rotation=45)

    # 3) Kidhome → PIE
    ax = axes[0, 2]
    vc_kid = df_cust["Kidhome"].value_counts().sort_index()
    ax.pie(
        vc_kid.values,
        labels=vc_kid.index.astype(str),
        autopct="%1.1f%%",
        colors=[colores[4], colores[5], colores[0]],
        startangle=90
    )
    ax.set_title("Kidhome")

    # 4) Teenhome → PIE
    ax = axes[1, 0]
    vc_teen = df_cust["Teenhome"].value_counts().sort_index()
    ax.pie(
        vc_teen.values,
        labels=vc_teen.index.astype(str),
        autopct="%1.1f%%",
        colors=[colores[1], colores[2], colores[3]],
        startangle=90
    )
    ax.set_title("Teenhome")

    # 5) Income vs Kidhome → HEATMAP
    ax = axes[1, 1]
    tabla1 = pd.crosstab(income_tramos, df_cust["Kidhome"], normalize="index") * 100
    sns.heatmap(tabla1, annot=True, fmt=".1f", cmap="YlOrBr", ax=ax)
    ax.set_title("Income vs Kidhome")
    ax.set_xlabel("Kidhome")
    ax.set_ylabel("Income")

    # 6) NumWebVisitsMonth vs Teenhome → HEATMAP
    ax = axes[1, 2]
    tabla2 = pd.crosstab(web_tramos, df_cust["Teenhome"], normalize="index") * 100
    sns.heatmap(tabla2, annot=True, fmt=".1f", cmap="YlOrBr", ax=ax)
    ax.set_title("NumWebVisitsMonth vs Teenhome")
    ax.set_xlabel("Teenhome")
    ax.set_ylabel("NumWebVisitsMonth")

    fig.savefig(os.path.join(ruta_salida, "customer_metricas.png"))
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

