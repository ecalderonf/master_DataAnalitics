from functools import reduce

# ============================================
# PROYECTO LÓGICA: Katas de Python
# por : Eduardo Calderón Flores
# para probar podeis ejecutar run_tests.py
# ============================================

''' 1. Escribe una función que reciba una cadena de texto como parámetro
y devuelva un diccionario con las frecuencias
de cada letra en la cadena. Los espacios no deben ser considerados.'''
def frecuencias_letras(cadena: str) -> dict:
    cadena = cadena.lower()
    frecuencias = {}

    for letra in cadena:
        if letra != " " :
            frecuencias[letra] = frecuencias.get(letra, 0) + 1

    return frecuencias


''' 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. 
Usa la función map() '''

# Ver programa ecalderonf_numero_doble.py

''' 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo. '''
def filtrar_palabras(lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra]


'''4. Genera una función que calcule la diferencia entre los valores de dos listas.
 Usa la función map() '''
def diferencias(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))


''' 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual 
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver 
una tupla que contenga la media y el estado. '''
def calcular_nota(numeros, nota_aprobado=5):
    media = sum(numeros) / len(numeros)
    estado = "suspenso"
    if media >= nota_aprobado:
        estado = "aprobado"

    return (media, estado)


'''6. Escribe una función que calcule el factorial de un número de manera recursiva.'''
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


'''7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()'''
def convertir_tuplas_a_strings(lista_tuplas):
    def convertir(tupla):
        return list(map(str, tupla))

    # Aplicamos map() → obtenemos listas internas
    listas = list(map(convertir, lista_tuplas))

    # Aplanamos el resultado
    resultado = []
    for sublista in listas:
        resultado.extend(sublista)

    return resultado


'''8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no.'''

# Ver programa ecalderonf_dividir_numeros.py

'''9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", 
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()'''
def filtrar_mascotas(lista_mascotas):
    lista_mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    def es_permitida(mascota):
        # Si NO está en la lista de prohibidas devuelve True
        return mascota not in lista_mascotas_prohibidas

    mascotas_filtradas = filter(es_permitida, lista_mascotas)

    resultado = list(mascotas_filtradas)

    return resultado


'''10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una 
excepción personalizada y maneja el error adecuadamente.'''
def calcular_promedio(numeros):
    len_numeros = len(numeros)
    try:
        if len_numeros == 0:
            raise Exception("La lista está vacía.")

        promedio = sum(numeros) / len_numeros
        print("Cálculo exitoso.")
        return promedio

    except Exception as error:
        return f"Error: {error}"


''' 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones 
adecuadamente. '''

# Ver programa ecalderonf_validar_edad.py


'''12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map() '''
def obtener_len_palabras(frase):
    palabras = frase.split()
    longitudes = map(len, palabras)
    return list(longitudes)


'''13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en 
mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map() '''
def mayus_minus_sin_repetir(caracteres):
    caracteres_unicos = []
    for c in caracteres:
        if c != ' ' and c not in caracteres_unicos:
            caracteres_unicos.append(c)

    resultado = map(str.upper, caracteres_unicos)
    mayusculas = list(resultado)

    resultado2 = map(str.lower, caracteres_unicos)
    minusculas = list(resultado2)

    tuplas = []
    for i in range(len(caracteres_unicos)):
        tuplas.append((mayusculas[i], minusculas[i]))

    return tuplas


'''14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()'''
def buscar_letra_en_palabra(lista_palabras, letra):
    palabras_filtradas = filter(lambda p: p.startswith(letra), lista_palabras)
    return list(palabras_filtradas)


'''15. Crea una función lambda que  sume 3 a cada número de una lista dada.'''
sumar_tres = lambda numeros: list(map(lambda n: n + 3, numeros))


'''16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de 
todas las palabras que sean más largas que n. Usa la función filter() '''

def obtener_palabras_mas_largas(frase, n):
    palabras = frase.split()
    palabras_filtradas = filter(str.isalpha, palabras)  # no afecta al resultado, pero permite usar filter
    resultado = []

    for palabra in palabras_filtradas:
        if len(palabra) > n:
            resultado.append(palabra)

    return resultado


'''17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo: 5,7,2
corresponde al número quinientos setenta y dos 572. Usa la función reduce()'''
def lista_a_numero(digitos):
    return reduce(lambda acumulado, d: acumulado * 10 + d, digitos)


'''18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
90. Usa la función filter()'''

# Ver programa ecalderonf_calificar_estudiantes.py


'''19. Crea una función lambda que filtre los números impares de una lista dada. '''
filtrar_impares = lambda numeros: list(filter(lambda n: n % 2 != 0, numeros))


'''20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()'''
def es_entero(valor):
    return type(valor) is int

def solo_enteros(lista):
    return list(filter(es_entero, lista))


'''21. Crea una función que calcule el cubo de un número dado mediante una función lambda'''
cubo = lambda x: x ** 3


'''22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() '''
def producto_lista(numeros):
    return reduce(lambda a, b: a * b, numeros)


'''23. Concatena una lista de palabras.Usa la función reduce()'''
def concatenar_palabras(palabras):
    return reduce(lambda a, b: a + b, palabras)


'''24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() '''
def calcular_diferencia_total(numeros):
    return reduce(lambda a, b: a - b, numeros)


'''25. Crea una función que cuente el número de caracteres en una cadena de texto dada.'''
def contar_caracteres(texto):
    return len(texto)


'''26. Crea una función lambda que calcule el resto de la división entre dos números dados.'''
resto = lambda a, b: a % b


'''27. Crea una función que calcule el promedio de una lista de números.'''
def obtener_promedio(numeros):
    return sum(numeros) / len(numeros)


'''28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada'''
def obtener_primer_duplicado(lista):
    vistos = set()

    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)

    return None


'''29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el 
carácter '#', excepto los últimos cuatro.'''
def enmascarar_texto(valor):
    texto = str(valor)
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]


'''30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras 
pero en diferente orden.'''
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)


'''31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en 
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se 
lanza una excepción.'''
def buscar_nombre(lista_nombres=None,nombre_buscar=None):
    try:
        if lista_nombres is None or  len(lista_nombres) == 0:
            lista_nombres = input("Introduce una lista de nombres separados por comas: ")
        nombres = [n.strip() for n in lista_nombres.split(",")]

        if nombre_buscar is None or not isinstance(nombre_buscar, str) or nombre_buscar.strip() == "":
            nombre_buscar = input("Introduce el nombre a buscar: ")

        if nombre_buscar in nombres:
            result = 'El nombre fue encontrado.'
        else:
            result = 'El nombre no está en la lista.'

    except Exception as e:
        result = e.message

    return result


'''32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
no trabaja aquí.'''
def obtener_puesto(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return f"{nombre_completo} no trabaja aquí."


'''33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.'''
sumar_listas = lambda a, b: [x + y for x, y in zip(a, b)]


'''34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos.'''

# Ver programa ecalderonf_arbol.py


'''35. NO existe el ejercicio en el fichero EnunciadoDataProjectPython.pdf '''


'''36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. '''

# Ver programa ecalderonf_usuario_banco.py


'''37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada'''

# Ver programa ecalderonf_procesar_texto.py


'''38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.'''

# Ver programa ecalderonf_momento_del_dia.py


'''39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.'''
# Ver programa ecalderonf_convertir_calificacion.py


'''40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y 
datos (una tupla con los datos necesarios para calcular el área de la figura).'''
def calcular_area(figura, datos):
    if figura == "rectangulo":
        if len(datos) != 2:
            print("Para un rectángulo se necesitan base y altura.")
            return
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        if len(datos) != 1:
            print("Para un círculo se necesita el radio.")
            return
        radio = datos[0]
        return 3.14159 * (radio ** 2)

    elif figura == "triangulo":
        if len(datos) != 2:
            print("Para un triángulo se necesitan base y altura.")
            return
        base, altura = datos
        return (base * altura) / 2

    else:
        print("Figura no reconocida. Usa: rectangulo, circulo o triangulo.")


'''41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento.'''

# Ver programa ecalderonf_precio_final.py


# ------------------------------------------------------------------------ FIN DE KATA ------------------------------------------------------------------------------ #
if __name__ == "__main__":
    import subprocess
    import sys
    import os

    ruta = os.path.join(os.path.dirname(__file__), "run_tests.py")
    subprocess.run([sys.executable, ruta])
