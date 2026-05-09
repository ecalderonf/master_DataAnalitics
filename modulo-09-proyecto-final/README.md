# Proyecto final – Performance comercial

Este proyecto realiza un análisis exploratorio de datos (EDA) sobre siete fuentes:

    - distribution_centers.json
    - events.csv
    - inventory_items.csv
    - order_items.csv
    - orders.csv
    - products.json
    - users.xlsx


El objetivo es contar con una base sólida para construir un Dashboard de performance comercial, con datos limpios, relaciones correctas y un entendimiento claro de las áreas donde existen anomalías que deben considerarse en la interpretación.

---
## Stack tecnológico

### Lenguaje
- Python 3.x

### Librerías necesarias

**Sistema y utilidades**
- os → gestión de rutas y sistema de archivos  
- shutil → copia de ficheros  
- openpyxl → lectura de Excel
- json → lectura/escritura de estructuras JSON  
- webbrowser → apertura automática del informe HTML  

**Análisis y manipulación de datos**
- pandas → carga, limpieza, transformación y análisis  
- numpy → operaciones numéricas y manejo de NaN  
- typing (Any, Dict) → tipado estático para funciones  

**Visualización**
- matplotlib.pyplot → backend de gráficos  
- seaborn → gráficos estadísticos y estilizados 

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
│   │   ├── bank_metricas.png
│   │   └── customer_metricas.png
│   └── informe_EDA.html
└── src
    ├── ecalderonf_proyecto_final.ipynb


```

### Ficheros

#### src/ecalderonf_proyecto_final.ipynb
- Controla todo el flujo
- Es el punto de entrada del proyecto.

---
## 📊 Análisis descriptivo de los datos

El proceso de análisis descriptivo se apoyó en tres datasets clave —orders, order_items y products— tras una depuración profunda que eliminó tablas irrelevantes y columnas sin valor analítico. 
Cada dataset quedó estructurado para permitir una lectura clara del ciclo comercial: desde la creación del pedido, pasando por el detalle de cada ítem vendido, hasta las características del producto asociado. La validación inicial confirmó la ausencia total de duplicados y la inexistencia de columnas completamente nulas, aunque sí se identificó un volumen significativo de valores faltantes en fechas logísticas, especialmente en orders, coherente con la presencia de pedidos cancelados.

La conversión de tipos aseguró que fechas, identificadores y valores numéricos estuvieran correctamente tipados, permitiendo cálculos temporales y relaciones entre tablas sin inconsistencias. La integridad relacional fue sólida: todos los order_id y product_id en order_items existen en sus tablas padre, lo que garantiza un modelo de datos estable para análisis posteriores. La normalización de texto en columnas categóricas (status, gender, category, brand, department) eliminó variaciones de formato que podrían fragmentar categorías en el dashboard.

En cuanto a calidad de datos, se detectaron incoherencias relevantes entre el estado del pedido y sus fechas asociadas. Algunos pedidos marcados como Complete o Returned carecen de fechas de envío, entrega o devolución, lo que contradice la lógica operativa. Sin embargo, son menos de 10 registros y la coherencia temporal estricta fue perfecta: ninguna fecha ocurre antes de la que debería precederla, lo que indica que el problema está en el estado declarado, no en las fechas en sí.

El dataset products mostró buena calidad: sin precios negativos, sin duplicados y con categorías limpias. order_items también presentó consistencia en precios y fechas. En conjunto, los tres datasets ofrecen una base sólida para construir un Dashboard de performance comercial, con datos limpios, relaciones correctas y un entendimiento claro de las áreas donde existen anomalías que deben considerarse en la interpretación.

### 🟦 1. Estructura general de los datasets
orders (8 columnas)
Contiene información a nivel pedido: estado, fechas logísticas y cantidad de ítems.

order_items (9 columnas)
Contiene información a nivel línea de pedido: producto, precio de venta y fechas logísticas por ítem.

products (7 columnas)
Contiene información a nivel producto: coste, categoría, marca y precio retail.

### 🟧 2. Limpieza y transformaciones aplicadas
Columnas eliminadas
orders → user_id

order_items → user_id, inventory_item_id

products → sku, distribution_center_id

DataFrames eliminados
df_distribution_center

df_events

df_inventory_items

df_users

Normalización de texto
orders → status, gender

products → category, name, brand, department

order_items → no aplica

Conversión de tipos
Fechas → convertidas a datetime

IDs → convertidos a string

Categóricos → convertidos a string

Precios → float

Validación de nulos y duplicados
dataset	nulos	duplicados
orders	237,803	0
order_items	344,923	0
products	26	0


No existen columnas completamente nulas.

### 🟩 3. Calidad de datos validada
Coherencia de claves
Todos los order_id de order_items existen en orders ✔️

Todos los product_id de order_items existen en products ✔️

Valores inválidos
orders → estados inválidos detectados:

Complete

Shipped

order_items → sin precios negativos ✔️

products → sin precios negativos ✔️

### 🟥 4. Incoherencias detectadas (status vs fechas)
orders → incoherencias en Complete
Pedidos marcados como Complete pero sin fechas de envío ni entrega:

Código
order_id: 420, 1245, 1345, 1384, 1791
orders → incoherencias en Returned
Pedidos marcados como Returned pero sin fechas de envío, entrega ni devolución:

Código
order_id: 181, 1886, 2417, 2514, 2606
orders → incoherencias en Cancelled
Sin incoherencias ✔️

### 🟦 5. Coherencia temporal estricta
Reglas validadas:

created_at < shipped_at

shipped_at < delivered_at

delivered_at < returned_at

Resultado
✔️ 0 incoherencias temporales  
Las fechas siguen un orden lógico perfecto.

### 🟨 6. Descripción general de cada dataset
- orders
Contiene información del ciclo de vida del pedido.

Variables clave:
status → estado del pedido

gender → segmento del cliente

created_at → fecha de creación

shipped_at → fecha de envío

delivered_at → fecha de entrega

returned_at → fecha de devolución

num_of_item → cantidad de ítems por pedido

Observaciones:
Gran volumen de nulos en fechas (normal por pedidos cancelados).

Incoherencias en estados Complete y Returned.

Fechas temporalmente coherentes.

- order_items
Representa cada línea de pedido.

Variables clave:
product_id → referencia al producto

sale_price → precio de venta

status → estado de la línea

Fechas logísticas por ítem

Observaciones:
No hay precios negativos.

No hay duplicados.

Fechas correctamente ordenadas.

- products
Catálogo de productos.

Variables clave:
cost

retail_price

category

brand

department

Observaciones:
No hay precios negativos.

Categorías, marcas y departamentos normalizados.

No hay duplicados.

### 🟦 7. Estado final del dataset (resumen técnico)
- Integridad relacional → ✔️
- Tipos de datos correctos → ✔️
- Duplicados → 0
- Nulos esperados → ✔️
- Incoherencias de status → detectadas
- Coherencia temporal → perfecta
- Texto normalizado → ✔️

---
## Análisis estadístico de los datos.

El dataset **BANK** contiene **43.000 filas y 21 columnas**, con varios puntos relevantes a nivel estructural:

### Nulos relevantes
- **age** → 11,91%  
- **cons.price.idx** → 1,10%  
- **euribor3m** → 21,53%  
- **nr.employed** → 81,35%  
- **date** → 0,58%

### Variables categóricas y sus valores
A continuación se listan **todas las columnas categóricas**, su **número de categorías** y **los valores detectados**:

#### **job** (12 categorías)
`['UNKNOWN', 'admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed']`

#### **marital** (4 categorías)
`['DIVORCED', 'MARRIED', 'SINGLE', 'UNKNOWN']`

#### **education** (8 categorías)
`['UNKNOWN', 'basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'illiterate', 'professional.course', 'university.degree']`

#### **default** (3 categorías)
`['0', '1', 'UNKNOWN']`

#### **housing** (3 categorías)
`['0', '1', 'UNKNOWN']`

#### **loan** (3 categorías)
`['0', '1', 'UNKNOWN']`

#### **contact** (2 categorías)
`['cellular', 'telephone']`

#### **poutcome** (3 categorías)
`['FAILURE', 'NONEXISTENT', 'SUCCESS']`

#### **y** (2 categorías — variable objetivo)
`['no', 'yes']`

### Columnas constantes
No se detectan columnas constantes ni casi constantes.

---

En conjunto, BANK presenta una estructura **rica en variables categóricas**, con distribuciones amplias y bien definidas, y un volumen significativo de nulos en algunas columnas numéricas clave, lo que es habitual en datasets de campañas telefónicas masivas.

---
## Informe explicativo del análisis.
### Distribuciones numéricas
- **Edad (age)**: mayor concentración en 26–45 años (≈59%), con un 11,91% de valores nulos.
- **Duración de llamada (duration)**: el 81% de las llamadas dura entre 61 y 600 segundos.

### Distribuciones categóricas
- **job**: predominan `admin.` (25,29%), `blue-collar` (22,45%) y `technician` (16,34%).
- **marital**: `MARRIED` es el estado más frecuente (60,46%).
- **education**: destaca `university.degree` (29,59%).
- **contact**: `cellular` es el canal principal (63,71%).
- **y**: la conversión global es del **11,27%**.

---



