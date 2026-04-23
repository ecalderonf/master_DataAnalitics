'''37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada:
reemplazar_palabras, contar_palabras , eliminar_palabra .
Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función
Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto.
Tiene que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva.
Tiene que devolver el texto con el remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto.
Tiene que devolver el texto con la palabra eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
número de argumentos variable según la opción indicada'''
def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for p in palabras:
        if p in conteo:
            conteo[p] += 1
        else:
            conteo[p] = 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras = [p for p in palabras if p != palabra]
    return " ".join(palabras)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        if len(args) != 2:
            print("Se requieren: palabra_original y palabra_nueva.")
            return
        return reemplazar_palabras(texto, args[0], args[1])

    elif opcion == "eliminar":
        if len(args) != 1:
            print("Se requiere: palabra_a_eliminar.")
            return
        return eliminar_palabra(texto, args[0])

    else:
        return("Opción no válida. Usa: contar, reemplazar o eliminar.")


texto = "hola mundo hola bonito mundo"

resultado1 = procesar_texto(texto, "contar")
print(resultado1)


resultado2 = procesar_texto(texto, "reemplazar", "mundo", "Python")
print(resultado2)

resultado3 = procesar_texto(texto, "eliminar", "hola")
print(resultado3)
