from utils_ficheros import (
    validar_todas_las_carpetas,
    validar_todos_los_ficheros,
    validar_ficheros_no_vacios,
    validar_ficheros_legibles,
    copiar_lista_ficheros
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
    'data/processed/bank-additional.csv',
    'data/processed/customer-details.xlsx'
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

# ============================
# FUNCIÓN DE FLUJO PRINCIPAL
# ============================

def ejecutar_EDA() -> bool:
    if not ejecutar_validaciones():
        return False

    if not ejecutar_copia_ficheros():
        return False

    return True



# ============================
# PREGUNTA INICIAL
# ============================

while True:
    respuesta = input('¿Generamos el EDA? (s/n): ').strip().lower()

    if respuesta == 's':
        print('Iniciamos proceso ...')
        if not ejecutar_EDA():
                exit()
        print('Proceso finalizado.')
        break
    elif respuesta == 'n':
        print('game over')
        exit()
    else:
        print('Opción no válida')
