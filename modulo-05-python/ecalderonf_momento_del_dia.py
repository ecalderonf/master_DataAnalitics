import random

'''38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.'''
def momento_del_dia(hora):
    if hora < 0 or hora > 23:
        return "Hora no válida."

    if hora >= 6 and hora < 12:
        return "Es de mañana."
    elif hora >= 12 and hora < 20:
        return "Es de tarde."
    else:
        return "Es de noche."

# Programa principal
try:
    mi_num2 = int(input("Introduce la hora (0-23): "))
    #mi_num2 = random.randint(0, 24)
    result = momento_del_dia(mi_num2)
    print(f'Hora: {mi_num2} , por lo tanto {result}')
except ValueError:
    print("Debes introducir un número entero.")

