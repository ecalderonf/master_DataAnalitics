import pandas as pd
from utils_ficheros import (
    validar_todas_las_carpetas,
    validar_todos_los_ficheros,
    validar_ficheros_no_vacios,
    validar_ficheros_legibles,
    copiar_lista_ficheros
)
from utils_limpieza import (
    cargar_csv,
    cargar_excel,
    limpiar_bank_data,
    limpiar_customer_data,
    guardar_df
)

# ============================
# CONSTANTES DEL PROYECTO
# ============================

CARPETAS = [
    'data/raw',
    'data/processed',
    'reports',
    'reports/img'
]

FICHEROS_ORIGEN = [
    'data/raw/bank-additional.csv',
    'data/raw/customer-details.xlsx'
]

FICHEROS_DESTINO = [
    'data/processed/bank-additional-processed.csv',
    'data/processed/customer-details-processed.xlsx'
]

# ============================
# FUNCIÓN DE VALIDACIÓN
# ============================

def ejecutar_validaciones():
    print('Validando carpetas...')
    if validar_todas_las_carpetas(CARPETAS):
        print('Carpetas OK')
    else:
        print('Error: No se pudieron validar o crear las carpetas necesarias.')
        return False

    print('Validando existencia de ficheros...')
    if validar_todos_los_ficheros(FICHEROS_ORIGEN):
        print('Ficheros OK')
    else:
        print('Error: No se encontraron los ficheros necesarios.')
        return False

    print('Validando que los ficheros no estén vacíos...')
    if validar_ficheros_no_vacios(FICHEROS_ORIGEN):
        print('Ficheros no vacíos OK')
    else:
        print('Error: Algún fichero está vacío.')
        return False

    print('Validando que los ficheros sean legibles...')
    try:
        if validar_ficheros_legibles(FICHEROS_ORIGEN):
            print('Ficheros legibles OK')
    except Exception as e:
        print(f'Error: Algún fichero no se puede leer. Detalle: {e}')
        return False

    print('Validaciones completadas correctamente.')
    return True

# ============================
# FUNCIÓN DE COPIAR FICHERO
# ============================

def ejecutar_copia_ficheros() -> bool:
    print('Copiando ficheros...')
    if not copiar_lista_ficheros(FICHEROS_ORIGEN, FICHEROS_DESTINO):
        print('Error al copiar los ficheros.')
        return False
    print('Ficheros copiados OK')
    return True

# ====================================
# FUNCIÓN DE LIMPIEZA Y TRANSFORMACIÓN
# ====================================

def ejecutar_limpieza() -> bool:
    print('Iniciando limpieza y transformación...')

    # === BANK CSV ===
    df_bank = cargar_csv(FICHEROS_DESTINO[0])
    if df_bank is None:
        print('Error cargando bank CSV.')
        return False

    df_bank, control_bank = limpiar_bank_data(df_bank)

    if not guardar_df(df_bank, FICHEROS_DESTINO[0]):
        print('Error guardando bank CSV limpio.')
        return False

    print('--- CONTROL BANK ---')
    for k, v in control_bank.items():
        print(k, v)

    # === CUSTOMER EXCEL ===
    # Cargar todas las hojas
    dict_cust = cargar_excel(FICHEROS_DESTINO[1])
    if dict_cust is None:
        print('Error cargando customer Excel.')
        return False

    # Unir todas las hojas en un único DataFrame
    df_cust = pd.concat(dict_cust.values(), ignore_index=True)

    # Limpiar el DataFrame combinado
    df_cust, control_cust = limpiar_customer_data(df_cust)

    # Guardar como una sola hoja
    if not guardar_df(df_cust, FICHEROS_DESTINO[1]):
        print('Error guardando customer Excel limpio.')
        return False

    print('--- CONTROL CUSTOMER ---')
    for k, v in control_cust.items():
        print(k, v)

    print('Limpieza completada.')
    return True

# ============================
# FUNCIÓN DE FLUJO PRINCIPAL
# ============================

def ejecutar_EDA() -> bool:
    if not ejecutar_validaciones():
        return False

    if not ejecutar_copia_ficheros():
        return False
    
    if not ejecutar_limpieza():
        return False

    return True


# ============================
# PREGUNTA INICIAL
# ============================

while True:
    respuesta = input('¿Generar EDA? (s/n): ').strip().lower()

    if respuesta == 's':
        print('Iniciar proceso ...')
        if not ejecutar_EDA():
                exit()
        print('Finalizar proceso.')
        print('¡SUCESS!')
        break
    elif respuesta == 'n':
        print('¡GAME OVER!')
        exit()
    else:
        print('Opción no válida')
