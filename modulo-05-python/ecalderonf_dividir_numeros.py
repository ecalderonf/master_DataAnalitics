
'''8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no.'''

try:
    dividendo = float(input("Ingresa el primer número: "))
    divisor= float(input("Ingresa el segundo número: "))

    resultado = dividendo / divisor
    print(f"La división fue exitosa. Resultado: {resultado}")

except ValueError:
    print("Error: Debes ingresar valores numéricos.")

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

