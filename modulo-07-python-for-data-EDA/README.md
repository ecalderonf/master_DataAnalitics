# Proyecto EDA – Campaña de marketing bancario

Este proyecto realiza un análisis exploratorio de datos (EDA) sobre dos fuentes:

- Un fichero **CSV** (`bank-additional.csv`)
- Un fichero **Excel** (`customer.xlsx` o equivalente)

El objetivo es contar con un flujo **reproducible**, con datos **limpios** y un **EDA automático** listo para revisión.

El script de python proporciona un flujo estable, reproducible y trazable, desde los datos en bruto hasta un EDA completo, 
con limpieza documentada, análisis descriptivo, visión de datos y un informe explicativo.

---
## Stack tecnológico

### Lenguaje
- Python 3.x

### Librerías necesarias
- pandas → lectura, escritura, limpieza y análisis  
- numpy → manejo de NaN y operaciones numéricas  
- openpyxl → lectura de Excel 
- matplotlib → backend de gráficos  
- seaborn → gráficos estadísticos  

---

## Flujo general del proyecto

0. **Ejecutar script main.py**
   - El script pregunta al usuario: ¿Generar EDA? (s/n)?:
   - Para ejecutar el proceso, escribir **s** y pulsar [Enter].
   - Para salir, escribir **n**  y pulsar [Enter].
   - Cualquier otra opción devuelve mensaje de error: Opción inválida y vuelve a preguntar hasta obtener una respuesta válida s/n.

1. **Opción s (Ejecuta el proceso)**
   - Se valida que existan las carpetas y ficheros de entrada.
   - Comprobación de que los ficheros no estén vacíos y sean legibles.
   - Se copian los ficheros originales a una carpeta de trabajo (`processed`).
   - Los procesos de limpieza, transformación  y EDA trabajan siempre sobre los ficheros `processed`.
   - Limpieza y transformación de datos de ambos ficheros
   - Análisis descriptivo
   - Visualización de datos (gráficos y tablas resumen)
   - Generar informe explicativo del análisis.

---
## Estructura del proyecto

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
    ├── utils_ficheros.py
    ├── utils_limpieza.py
    ├── utils_eda.py

```

## Ficheros

### src/main.py
- Controla todo el flujo
- Es el punto de entrada del proyecto.

### src/utils_ficheros.py
Funciones para:
- Validar carpetas
- Validar ficheros
- Comprobar tamaño
- Verificar legibilidad

### src/utils_limpieza.py
IncluyeFunciones para:
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

