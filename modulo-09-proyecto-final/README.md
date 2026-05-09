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
## Análisis descriptivo de los datos

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

### 1. Métricas de ventas — rendimiento comercial

Los datos muestran un negocio con **volumen alto de pedidos** (125k) pero con **ventas por unidad relativamente bajas**, típico de un catálogo amplio y muy fragmentado.

- **Ingreso total:** 10.8M  
- **Pedidos totales:** 125k  
- **Ticket promedio:** 86.46  
- **Unidades vendidas:** 181k  

#### Análisis
- El ticket promedio es **estable** y coincide con el ingreso promedio por pedido, lo que indica **coherencia interna** entre orders y order_items.  
- La relación *unidades vendidas / pedidos* ≈ **1.45 unidades por pedido**, lo que sugiere compras pequeñas, propias de moda.  
- El ingreso total está bien distribuido: no hay dependencia extrema de un solo segmento.

---

### 2. Métricas por categoría / marca / departamento

#### Categorías (Top 10 por ingreso)
Las categorías con mayor ingreso son prendas de precio medio-alto:

- outerwear & coats — 1.30M  
- jeans — 1.25M  
- sweaters — 0.84M  
- suits & sport coats — 0.66M  
- fashion hoodies & sweatshirts — 0.64M  
- swim — 0.64M  
- sleep & lounge — 0.53M  
- shorts — 0.51M  
- tops & tees — 0.49M  
- dresses — 0.46M  

#### Análisis
- El top está dominado por **categorías de invierno y prendas premium**, lo que eleva el ingreso.  
- Las categorías de menor precio (tees, shorts) aparecen por volumen, no por ticket.  
- La distribución es **equilibrada**, sin una categoría que concentre más del 15% del total.

---

#### Marcas (Top 10 por ingreso)

- calvin klein — 208k  
- diesel — 199k  
- 7 for all mankind — 188k  
- carhartt — 183k  
- true religion — 180k  
- tommy hilfiger — 126k  
- volcom — 106k  
- quiksilver — 105k  
- columbia — 103k  
- the north face — 101k  

#### Análisis
- Las marcas premium de denim y moda casual lideran el ingreso.  
- No hay una marca dominante: el top 10 está muy repartido.  
- La presencia de marcas técnicas (Columbia, The North Face) indica variedad de catálogo.

---

#### Departamentos

- men — 5.73M  
- women — 5.09M  

#### Análisis
- El reparto es casi 50/50, lo que indica un catálogo equilibrado.  
- El ligero liderazgo de **men** coincide con las categorías top (coats, jeans, sweaters).

---

### 3. Métricas de estado del pedido — flujo operativo

- Cancelados: 14.86%  
- Devueltos: 10.01%  
- Completados: 25.04%  
- Enviados: 30.01%  
- Procesando: 20.09%  

#### Análisis
- La tasa de cancelación es **alta**, típica de datasets sintéticos.  
- La tasa de devolución del 10% es **realista** para moda.  
- Solo 1 de cada 4 pedidos llega a *complete*, lo que confirma que el dataset simula un flujo operativo parcial.  
- La distribución de estados es coherente con un pipeline de datos no finalizado.

---

### 4. Métricas temporales

- Envío promedio: 1 día  
- Entrega promedio: 2 días  

#### Análisis
- Los tiempos son **demasiado buenos** para ser reales → refuerza que el dataset es sintético.  
- La relación envío/entrega es consistente: 1 día para procesar + 1 día adicional para entregar.

---

### 5. Productos destacados — insights comerciales

| product_id | unidades_vendidas | name |
|-----------:|-------------------:|------|
| 21842 | 19 | haggar men's tonal stria pleat front cuff dress pant |
| 18795 | 18 | life is good men's king of the grill short sleeve tee |
| 17045 | 17 | bayside apparel adult usa-made long-sleeve pocket t-shirt. 8100 |
| 25209 | 16 | thorlo men's lt walking mini crew sock |
| 23873 | 16 | the newport collection pack-n-go pullover jacket from charles river apparel |
| 22473 | 16 | wrinkle-free cotton poplin comfort-waist pants / plain sage |
| 23675 | 16 | wrangler rugged wear men's unlined denim jacket antique navy |
| 24502 | 16 | wigwam men's at work 3-pack socks |
| 25547 | 16 | michael kors men's 3 pack brief |
| 25204 | 16 | timberland men's crew socks |

#### Análisis
- Las unidades vendidas son **bajas** porque el dataset es sintético y distribuye ventas de forma plana.  
- El top está dominado por **ropa masculina**, coherente con las métricas por departamento.  
- No hay un producto estrella: todos están entre 16 y 19 unidades, lo que confirma la naturaleza generada del dataset.

---

### Conclusión general

- El dataset es **coherente internamente**, pero claramente **sintético**.  
- Las ventas están bien distribuidas entre categorías, marcas y departamentos.  
- Los estados del pedido y los tiempos logísticos confirman que no es un dataset real.  
- Las unidades por producto son bajas y muy homogéneas, lo que refuerza la estructura sintética.  
- Aun así, las métricas permiten construir un dashboard comercial funcional y consistente.

---
## Informe explicativo del análisis.

---