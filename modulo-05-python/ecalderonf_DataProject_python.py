import random
from functools import reduce

# PROYECTO LÓGICA: Katas de Python

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

texto = 'DataAnalitics DataAnalitics DataAnalitics' #= input("Introduce una cadena de texto: ")
print(frecuencias_letras(texto))

''' 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. 
Usa la función map() '''

numeros = [random.randint(1, 10) for _ in range(5)]

dobles = list(map(lambda x: x * 2, numeros))

print(f'Números: {numeros} , dobles: {dobles}')

''' 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo. '''
def filtrar_palabras(lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra]

palabras = ["educación", "reducir", "seducción", "edificio", "medusa", "quedarse"]
objetivo = "edu"
resultado = filtrar_palabras(palabras, objetivo)
print(resultado)

'''4. Genera una función que calcule la diferencia entre los valores de dos listas.
 Usa la función map() '''

def diferencias(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

lst1 = [random.randint(10, 20) for _ in range(5)]
lst2 = [random.randint(1, 10) for _ in range(5)]

resultado = diferencias(lst1, lst2)

print(f'lista1: {lst1} , lista2: {lst2} , RESULTADO: {resultado}')

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

lst3 = [random.randint(1, 10) for _ in range(5)]
mi_nota = calcular_nota(lst3)
print(f'lst3: {lst3} .La nota es: {mi_nota}')

'''6. Escribe una función que calcule el factorial de un número de manera recursiva.'''
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

mi_num = random.randint(1, 10)
result = factorial(mi_num)
print(f'El factorial de {mi_num} es {result}')

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

lista_datos = [(7, 'data'), ('hola', 'python'), (True, 'Power')]
resultado = convertir_tuplas_a_strings(lista_datos)
print(f'lista_datos: {lista_datos} resultado: {resultado}')

'''8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico 
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
indicando si la división fue exitosa o no.'''

def dividir_numeros():
    try:
        dividendo = float(input("Ingresa el primer número: "))
        divisor= float(input("Ingresa el segundo número: "))

        resultado = dividendo / divisor
        print(f"La división fue exitosa. Resultado: {resultado}")

    except ValueError:
        print("Error: Debes ingresar valores numéricos.")

    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

# ToDo dividir_numeros()

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


mascotas = ["Perro", "Gato", "Mapache", "Tortuga", "Cocodrilo", "Peces"]
resultado = filtrar_mascotas(mascotas)
print(resultado)

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

lst4 = [random.randint(1, 10) for _ in range(5)]
print(calcular_promedio(lst4))   # 6.0
print(calcular_promedio([]))          # Error: La lista está vacía.


''' 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones 
adecuadamente. '''

try:
    # ToDo edad = input("Introduce tu edad: ")
    # ToDo edad = int(edad)

    edad = random.randint(0, 150)

    if edad < 0 or edad > 120:
        raise Exception("La edad está fuera del rango permitido.")

    print("Edad válida:", edad)

except ValueError:
    print("Error: Debes introducir un número entero.")

except Exception as error:
    print("Error:", error)


'''12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map() '''

def obtener_len_palabras(frase):
    palabras = frase.split()
    longitudes = map(len, palabras)
    return list(longitudes)

mi_frase = 'Katas de Python'
result = obtener_len_palabras(mi_frase)
print(f' Frase: {mi_frase} , len: {result}')


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


print(mayus_minus_sin_repetir('Katas de Python'))


'''14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()'''

def buscar_letra_en_palabra(lista_palabras, letra):
    palabras_filtradas = filter(lambda p: p.startswith(letra), lista_palabras)
    return list(palabras_filtradas)

palabras = ['analitics', 'power', 'calculo', 'dataset', 'dashboard']
print(buscar_letra_en_palabra(palabras, 'd'))


'''15. Crea una función lambda que  sume 3 a cada número de una lista dada.'''
sumar_tres = lambda numeros: list(map(lambda n: n + 3, numeros))

lst5 = [random.randint(1, 10) for _ in range(5)]
result = sumar_tres(lst5)
print(f'lst5: {lst5} . resultado: {result}')


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

texto = "Escribe una función que tome una cadena de texto"
print(obtener_palabras_mas_largas(texto, 5))


'''17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo: 5,7,2
corresponde al número quinientos setenta y dos 572. Usa la función reduce()'''
def lista_a_numero(digitos):
    return reduce(lambda acumulado, d: acumulado * 10 + d, digitos)


lst6 = [random.randint(1, 10) for _ in range(4)]
result = lista_a_numero(lst6)
print(f'lst6: {lst6} . resultado: {result}')

'''18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 
90. Usa la función filter()'''

mis_estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 71},
    {"nombre": "Marta", "edad": 19, "calificacion": 91},
    {"nombre": "Carlos", "edad": 21, "calificacion": 73},
    {"nombre": "Elena", "edad": 23, "calificacion": 89}
]

def es_sobresaliente(estudiante):
    return estudiante["calificacion"] >= 90

estudiantes_filtrados = list(filter(es_sobresaliente, mis_estudiantes))

print(estudiantes_filtrados)


'''19. Crea una función lambda que filtre los números impares de una lista dada. '''
filtrar_impares = lambda numeros: list(filter(lambda n: n % 2 != 0, numeros))

lst7 = [random.randint(1, 100) for _ in range(10)]
result = filtrar_impares(lst7)
print(f'lst7: {lst7} . resultado: {result}')


'''20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()'''
def es_entero(valor):
    return type(valor) is int

def solo_enteros(lista):
    return list(filter(es_entero, lista))

mis_datos = [10, "hola", 25, "3", 7, "python", 0]
print(solo_enteros(mis_datos))


'''21. Crea una función que calcule el cubo de un número dado mediante una función lambda'''
cubo = lambda x: x ** 3

mi_num = random.randint(1, 10)
result = cubo(mi_num)
print(f'mi_num:{mi_num} ,cubo: {result}')


'''22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() '''
def producto_lista(numeros):
    return reduce(lambda a, b: a * b, numeros)

lst8 = [random.randint(1, 10) for _ in range(5)]
result = producto_lista(lst8)
print(f'lst8: {lst8} . resultado: {result}')


'''23. Concatena una lista de palabras.Usa la función reduce()'''
def concatenar_palabras(palabras):
    return reduce(lambda a, b: a + b, palabras)

print(concatenar_palabras(["Hola", " ", "mundo"]))


'''24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() '''
def calcular_diferencia_total(numeros):
    return reduce(lambda a, b: a - b, numeros)

lst9 = [random.randint(1, 20) for _ in range(3)]
result = calcular_diferencia_total(lst9)
print(f'lst9: {lst9} . resultado: {result}')



'''25. Crea una función que cuente el número de caracteres en una cadena de texto dada.'''
def contar_caracteres(texto):
    return len(texto)

texto1 = 'Hola mundo'
result = contar_caracteres(texto1)
print(f'texto1: {texto1} . resultado: {result}')



'''26. Crea una función lambda que calcule el resto de la división entre dos números dados.'''
resto = lambda a, b: a % b

dividendo1 = random.randint(10, 100)
divisor1 = random.randint(1, 10)
result = resto(dividendo1, divisor1)
print(f'dividendo1: {dividendo1} , divisor: {divisor1}. resto: {result}')



'''27. Crea una función que calcule el promedio de una lista de números.'''
def obtener_promedio(numeros):
    return sum(numeros) / len(numeros)

lst10 = [random.randint(1, 100) for _ in range(5)]
result = obtener_promedio(lst10)
print(f'lst10: {lst10} . promedio: {result}')


'''28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada'''
def obtener_primer_duplicado(lista):
    vistos = set()

    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)

    return None

lst11 = [random.randint(1, 5) for _ in range(10)]
result = obtener_primer_duplicado(lst11)
print(f'lst11: {lst11} . resultado: {result}')


'''29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el 
carácter '#', excepto los últimos cuatro.'''
def enmascarar_texto(valor):
    texto = str(valor)
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]

mi_num2 = random.randint(10000000, 9999999999)
result = enmascarar_texto(mi_num2)
print(f'mi_num2: {mi_num2} . resultado: {result}')


'''30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras 
pero en diferente orden.'''
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

palabra1 = 'toro'
palabra2 = 'otro'
result = son_anagramas(palabra1, palabra2)
print(f'palabra1: {palabra1}, palabra2: {palabra2} . es anagrama: {result}')


'''31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en 
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se 
lanza una excepción.'''
def buscar_nombre():
    try:
        lista = input("Introduce una lista de nombres separados por comas: ")
        nombres = [n.strip() for n in lista.split(",")]

        nombre_buscar = input("Introduce el nombre a buscar: ")

        if nombre_buscar in nombres:
            print(f"El nombre '{nombre_buscar}' fue encontrado.")
        else:
            raise Exception(f"El nombre '{nombre_buscar}' no está en la lista.")

    except Exception as e:
        print(e)

# ToDo buscar_nombre()


'''32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
no trabaja aquí.'''
def obtener_puesto(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return f"{nombre_completo} no trabaja aquí."

empleados = [
    {"nombre": 'Ricky Rubio', 'puesto': 'Analista'},
    {"nombre": 'Willy Hernangómez', 'puesto': 'Desarrollador'},
    {"nombre": 'Juancho Hernangómez', 'puesto': 'Gerente'}
]

print(obtener_puesto('Ricky Rubio', empleados))


'''33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.'''
sumar_listas = lambda a, b: [x + y for x, y in zip(a, b)]

lst12 = [random.randint(1, 20) for _ in range(5)]
lst13 = [random.randint(1, 20) for _ in range(5)]
result = sumar_listas(lst12, lst13)
print(f'lst12: {lst12}, lst13: {lst13} . resultado: {result}')


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
    # ToDo hora_usuario = int(input("Introduce la hora (0-23): "))
    mi_num2 = random.randint(0, 24)
    result = momento_del_dia(mi_num2)
    print(f'Hora: {mi_num2} , por lo tanto {result}')
except ValueError:
    print("Debes introducir un número entero.")


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

print(calcular_area("rectangulo", (5, 3)))

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

