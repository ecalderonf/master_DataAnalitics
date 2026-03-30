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
