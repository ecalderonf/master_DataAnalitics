
'''39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente'''
def calificacion_texto(nota):
    if nota < 0 or nota > 100:
        return "Calificación no válida."

    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    else:
        return "excelente"

# Programa principal
try:
    nota_usuario = int(input("Introduce la calificación (0-100): "))
    print(calificacion_texto(nota_usuario))
except ValueError:
    print("Debes introducir un número entero.")
