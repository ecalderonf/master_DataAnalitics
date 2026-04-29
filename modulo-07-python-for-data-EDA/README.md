# Proyecto EDA – Campaña de marketing bancario

Este proyecto realiza un **proceso completo de validación, copia, limpieza y análisis exploratorio de datos (EDA)** sobre dos fuentes:

- Un fichero **CSV** (`bank-additional.csv`)
- Un fichero **Excel** (`customer.xlsx` o equivalente)

El objetivo es dejar un flujo **reproducible**, con datos **limpios** y un **EDA automático** listo para revisión.

---

## Flujo general del proyecto

1. **Validación de entorno y ficheros**
   - Comprobación de carpetas requeridas.
   - Verificación de existencia de ficheros de entrada.
   - Comprobación de que no estén vacíos.
   - Verificación de que sean legibles.

2. **Copia de ficheros “raw” → “processed”**
   - Se copian los ficheros originales a una carpeta de trabajo (`processed`).
   - Los procesos de limpieza y EDA trabajan siempre sobre los ficheros `processed`.

3. **Limpieza y transformación**
   - Conversión de tipos (numéricos, fechas, categóricos).
   - Normalización de formatos (comas decimales, fechas en español, etc.).
   - Relleno de valores categóricos vacíos con `UNKNOWN`.
   - Conversión de variables binarias a 0/1.
   - Eliminación de duplicados por identificador.

4. **Generación del EDA**
   - Carga de los datos ya limpios.
   - Cálculo de estadísticas descriptivas.
   - Generación de gráficos y tablas resumen.
   - Guardado de resultados (tablas y figuras) en carpetas de `reports`.

---

## Estructura de carpetas

Estructura típica del proyecto:

```text
.
├── data
│   ├── raw
│   │   ├── bank-additional.csv
│   │   └── customer.xlsx
│   └── processed
│       ├── bank-additional-processed.csv
│       └── customer-processed.xlsx
├── reports
│   ├── img
│   │   ├── bank_*.png
│   │   └── customer_*.png
│   └── tables
│       ├── bank_describe.csv
│       └── customer_describe.csv
└── src
    ├── main.py
    ├── utils_validacion.py
    ├── utils_limpieza.py
    ├── utils_eda.py
    └── config.py


## 3. Ficheros y su objetivo

### src/main.py
Controla todo el flujo:
- Validaciones
- Copia de ficheros
- Limpieza
- EDA  
Es el punto de entrada del proyecto.

### src/utils_validacion.py
Funciones para:
- Validar carpetas
- Validar ficheros
- Comprobar tamaño
- Verificar legibilidad

### src/utils_limpieza.py
Incluye:
- Conversión de comas a float
- Conversión de tipos numéricos
- Conversión de fechas (Excel y español)
- Normalización de categorías
- Eliminación de duplicados
- Limpieza específica de BANK y CUSTOMER
- Generación de cifras de control

### src/utils_eda.py
Funciones para:
- Estadísticos descriptivos
- Histogramas
- Boxplots
- Gráficos categóricos
- Guardado de imágenes y tablas

### src/config.py
Define:
- Rutas de carpetas
- Nombres de ficheros
- Parámetros generales del flujo

---

## 4. Flujo del script que genera el EDA

1. Validaciones iniciales  
2. Copia de ficheros desde raw a processed  
3. Limpieza del dataset BANK  
4. Limpieza del dataset CUSTOMER  
5. Carga de los datos ya limpios  
6. Generación del EDA  
7. Exportación de resultados a reports/  

Los resultados se guardan en:
- reports/img/
- reports/tables/

---

## 5. Stack tecnológico

### Lenguaje
- Python 3.x

### Librerías necesarias
pandas
numpy
matplotlib
seaborn
openpyxl

### Uso de cada librería
- pandas → lectura, escritura, limpieza y análisis  
- numpy → manejo de NaN y operaciones numéricas  
- matplotlib → backend de gráficos  
- seaborn → gráficos estadísticos  
- openpyxl → lectura de Excel  

. Confirmar la generación del EDA cuando el script lo solicite.

Los resultados aparecerán en:
- reports/img/
- reports/tables/

---

## 7. Objetivo final

El proyecto garantiza un flujo estable, reproducible y trazable, desde los datos en bruto hasta un EDA completo, con limpieza documentada y resultados exportados de forma organizada.
