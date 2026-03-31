import random

''' 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. 
Usa la función map() '''

numeros = [random.randint(1, 10) for _ in range(5)]

dobles = list(map(lambda x: x * 2, numeros))
print(f'Números: {numeros} , dobles: {dobles}')
