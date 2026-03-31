import random

''' 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones 
adecuadamente. '''

try:
    edad = int(input("Introduce tu edad: "))
    #edad = random.randint(0, 150)

    if edad < 0 or edad > 120:
        raise Exception("La edad está fuera del rango permitido.")

    print("Edad válida:", edad)

except ValueError:
    print("Error: Debes introducir un número entero.")

except Exception as error:
    print("Error:", error)
