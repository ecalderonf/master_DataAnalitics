import random

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

dividir_numeros()

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
