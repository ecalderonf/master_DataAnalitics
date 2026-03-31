'''41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
a cero). Por ejemplo, descuento de 15€.
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
programa de Python.'''

# 1. Solicitar precio original
try:
    precio = float(input("Introduce el precio original del artículo: "))
except ValueError:
    print("Debes introducir un número válido.")
    precio = 0

# 2. Preguntar si tiene cupón
tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").lower()

# 3. Si tiene cupón, pedir valor
descuento = 0
if tiene_cupon == "sí" or tiene_cupon == "si":
    try:
        descuento = float(input("Introduce el valor del cupón: "))
    except ValueError:
        print("Valor de cupón no válido.")
        descuento = 0

# 4. Aplicar descuento si es válido
if descuento > 0:
    precio_final = precio - descuento
else:
    precio_final = precio

# 5. Mostrar precio final
print("El precio final de la compra es:", precio_final)
