import random

import ecalderonf_DataProject_python

print("\n============================================")
print(" PRUEBAS DEL PROYECTO PYTHON – MÓDULO 05")
print(" PROYECTO LÓGICA: Katas de Python ")
print(" por : Eduardo Calderón Flores ")
print("============================================")

''' 0. Formatea y muestra el resultado de una prueba. '''
def mostrar_resultado(nombre_funcion: str, parametros: dict, resultado):
    '''
    nombre_funcion: str → nombre de la función probada
    parametros: dict → diccionario {nombre_parametro: valor}
    resultado: cualquier tipo → resultado devuelto por la función
    '''
    print('\n--------------------------------------------')
    print(f' {nombre_funcion}')
    print('--------------------------------------------')

    if parametros:
        print(' Parámetros:')
        for nombre, valor in parametros.items():
            print(f'   - {nombre}: {valor}')

    print('\n Resultado:')
    print(f'   {resultado}')
    #print('--------------------------------------------')


''' 1. Escribe una función que reciba una cadena de texto como parámetro
y devuelva un diccionario con las frecuencias
de cada letra en la cadena. Los espacios no deben ser considerados.'''

texto = 'DataAnalitics DataAnalitics DataAnalitics' #= input("Introduce una cadena de texto: ")
result = ecalderonf_DataProject_python.frecuencias_letras(texto)

params = {"cadena": texto}
mostrar_resultado('EJERCICIO 01. frecuencias_letras',params, result)


''' 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. 
Usa la función map() '''

# Ver programa ecalderonf_numero_doble.py

''' 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo. '''

palabras = ["educación", "reducir", "seducción", "edificio", "medusa", "quedarse"]
objetivo = "edu"
result = ecalderonf_DataProject_python.filtrar_palabras(palabras, objetivo)

params = {"palabras": palabras, "objetivo": objetivo}
mostrar_resultado('EJERCICIO 03. filtrar_palabras',params, result)


'''4. Genera una función que calcule la diferencia entre los valores de dos listas.
 Usa la función map() '''

lst1 = [random.randint(10, 20) for _ in range(5)]
lst2 = [random.randint(1, 10) for _ in range(5)]
result = ecalderonf_DataProject_python.diferencias(lst1, lst2)

params = {"lst1": lst1,"lst2": lst2}
mostrar_resultado('EJERCICIO 04. diferencias',params, result)


''' 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual 
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver 
una tupla que contenga la media y el estado. '''

lst3 = [random.randint(1, 10) for _ in range(5)]
result = ecalderonf_DataProject_python.calcular_nota(lst3)

params = {"lst3": lst3}
mostrar_resultado('EJERCICIO 05. calcular_nota',params, result)


'''6. Escribe una función que calcule el factorial de un número de manera recursiva.'''

mi_num = random.randint(1, 10)
result = ecalderonf_DataProject_python.factorial(mi_num)

params = {"mi_num": mi_num}
mostrar_resultado('EJERCICIO 06. factorial',params, result)


'''7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()'''

lst_datos = [(7, 'data'), ('hola', 'python corregido'), (True, 'Power')]
result = ecalderonf_DataProject_python.convertir_tuplas_a_strings(lst_datos)

params = {"lst_datos": lst_datos}
mostrar_resultado('EJERCICIO 07. convertir_tuplas_a_strings (corregido)',params, result)


'''8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no.'''

# Ver programa ecalderonf_dividir_numeros.py

'''9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", 
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()'''

mascotas = ["Perro", "Gato", "Mapache", "Tortuga", "Cocodrilo", "Peces"]
result = ecalderonf_DataProject_python.filtrar_mascotas(mascotas)

params = {"mascotas": mascotas}
mostrar_resultado('EJERCICIO 09. filtrar_mascotas',params, result)


'''10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una 
excepción personalizada y maneja el error adecuadamente.'''

lst4 = [random.randint(1, 10) for _ in range(5)]
result = ecalderonf_DataProject_python.calcular_promedio(lst4)

params = {"lst4": lst4}
mostrar_resultado('EJERCICIO 10. calcular_promedio (corregido)',params, result)


''' 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones 
adecuadamente. '''

# Ver programa ecalderonf_validar_edad.py


'''12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map() '''

mi_frase = 'Katas de Python'
result = ecalderonf_DataProject_python.obtener_len_palabras(mi_frase)

params = {"mi_frase": mi_frase}
mostrar_resultado('EJERCICIO 12. obtener_len_palabras',params, result)


'''13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en 
mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map() '''

mi_frase = 'Katas de Python'
result = ecalderonf_DataProject_python.mayus_minus_sin_repetir(mi_frase)

params = {"mi_frase": mi_frase}
mostrar_resultado('EJERCICIO 13. mayus_minus_sin_repetir',params, result)


'''14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()'''

palabras = ['analitics', 'power', 'calculo', 'dataset', 'dashboard']
letra = 'd'
result = ecalderonf_DataProject_python.buscar_letra_en_palabra(palabras, letra)

params = {"palabras": palabras,'letra': letra}
mostrar_resultado('EJERCICIO 14. buscar_letra_en_palabra',params, result)


'''15. Crea una función lambda que  sume 3 a cada número de una lista dada.'''

lst5 = [random.randint(1, 10) for _ in range(5)]
result = ecalderonf_DataProject_python.sumar_tres(lst5)
print(f'lst5: {lst5} . resultado: {result}')

params = {"lst5": lst5}
mostrar_resultado('EJERCICIO 15. sumar_tres',params, result)


'''16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de 
todas las palabras que sean más largas que n. Usa la función filter() '''

mi_texto = "Escribe una función que tome una cadena de texto"
num = 5
result = ecalderonf_DataProject_python.obtener_palabras_mas_largas(mi_texto, num)

params = {"mi_texto": mi_texto, "num": num}
mostrar_resultado('EJERCICIO 16. obtener_palabras_mas_largas (corregido)',params, result)


'''17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo: 5,7,2
corresponde al número quinientos setenta y dos 572. Usa la función reduce()'''

lst6 = [random.randint(1, 10) for _ in range(4)]
result = ecalderonf_DataProject_python.lista_a_numero(lst6)

params = {"lst6": lst6}
mostrar_resultado('EJERCICIO 17. lista_a_numero',params, result)


'''18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
90. Usa la función filter()'''

# Ver programa ecalderonf_calificar_estudiantes.py


'''19. Crea una función lambda que filtre los números impares de una lista dada. '''

lst7 = [random.randint(1, 100) for _ in range(10)]
result = ecalderonf_DataProject_python.filtrar_impares(lst7)

params = {"lst7": lst7}
mostrar_resultado('EJERCICIO 19. filtrar_impares',params, result)


'''20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()'''

mis_datos = [10, "hola", 25, "3", 7, "python", 0]
result = ecalderonf_DataProject_python.solo_enteros(mis_datos)

params = {"mis_datos": mis_datos}
mostrar_resultado('EJERCICIO 20. solo_enteros',params, result)


'''21. Crea una función que calcule el cubo de un número dado mediante una función lambda'''

mi_num = random.randint(1, 10)
result = ecalderonf_DataProject_python.cubo(mi_num)

params = {"mi_num": mi_num}
mostrar_resultado('EJERCICIO 21. cubo',params, result)


'''22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() '''

lst8 = [random.randint(1, 10) for _ in range(5)]
result = ecalderonf_DataProject_python.producto_lista(lst8)

params = {"lst8": lst8}
mostrar_resultado('EJERCICIO 22. producto_lista',params, result)


'''23. Concatena una lista de palabras.Usa la función reduce()'''

lst14 = ["Hola", " ", "mundo"]
result = ecalderonf_DataProject_python.concatenar_palabras(lst14)

params = {"lst14": lst14}
mostrar_resultado('EJERCICIO 23. concatenar_palabras',params, result)


'''24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() '''

lst9 = [random.randint(1, 20) for _ in range(3)]
result = ecalderonf_DataProject_python.calcular_diferencia_total(lst9)

params = {"lst9": lst9}
mostrar_resultado('EJERCICIO 24. calcular_diferencia_total',params, result)


'''25. Crea una función que cuente el número de caracteres en una cadena de texto dada.'''

texto1 = 'Hola mundo'
result = ecalderonf_DataProject_python.contar_caracteres(texto1)

params = {"texto1": texto1}
mostrar_resultado('EJERCICIO 25. contar_caracteres',params, result)


'''26. Crea una función lambda que calcule el resto de la división entre dos números dados.'''

dividendo1 = random.randint(10, 100)
divisor1 = random.randint(1, 10)
result = ecalderonf_DataProject_python.resto(dividendo1, divisor1)

params = {"dividendo1": dividendo1, "divisor1": divisor1}
mostrar_resultado('EJERCICIO 26. resto',params, result)


'''27. Crea una función que calcule el promedio de una lista de números.'''

lst10 = [random.randint(1, 100) for _ in range(5)]
result = ecalderonf_DataProject_python.obtener_promedio(lst10)

params = {"lst10": lst10}
mostrar_resultado('EJERCICIO 27. obtener_promedio',params, result)



'''28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada'''

lst11 = [random.randint(1, 5) for _ in range(10)]
result = ecalderonf_DataProject_python.obtener_primer_duplicado(lst11)

params = {"lst11": lst11}
mostrar_resultado('EJERCICIO 28. obtener_primer_duplicado',params, result)


'''29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el 
carácter '#', excepto los últimos cuatro.'''

mi_num2 = random.randint(10000000, 9999999999)
result = ecalderonf_DataProject_python.enmascarar_texto(mi_num2)

params = {"mi_num2": mi_num2}
mostrar_resultado('EJERCICIO 29. enmascarar_texto',params, result)


'''30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras 
pero en diferente orden.'''

palabra1 = 'toro'
palabra2 = 'otro'
result = ecalderonf_DataProject_python.son_anagramas(palabra1, palabra2)

params = {"palabra1": palabra1, "palabra2": palabra2}
mostrar_resultado('EJERCICIO 30. son_anagramas',params, result)


'''31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en 
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se 
lanza una excepción.'''

lista_nombres = 'Pedro,Juan,Mateo,Santiago,Jonas'
nombre_buscar = 'Jonas'
result = ecalderonf_DataProject_python.buscar_nombre(lista_nombres, nombre_buscar)

params = {"lista_nombres ": lista_nombres , "nombre_buscar": nombre_buscar}
mostrar_resultado('EJERCICIO 31. buscar_nombre (corregido)',params, result)

'''32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
no trabaja aquí.'''

empleados = [
    {"nombre": 'Ricky Rubio', 'puesto': 'Analista'},
    {"nombre": 'Willy Hernangómez', 'puesto': 'Desarrollador'},
    {"nombre": 'Juancho Hernangómez', 'puesto': 'Gerente'}
]
nombre_completo = 'Ricky Rubio'
result = ecalderonf_DataProject_python.obtener_puesto(nombre_completo, empleados)

params = {"nombre_completo":nombre_completo,"empleados": empleados}
mostrar_resultado('EJERCICIO 32. obtener_puesto',params, result)


'''33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.'''

lst12 = [random.randint(1, 20) for _ in range(5)]
lst13 = [random.randint(1, 20) for _ in range(5)]
result = ecalderonf_DataProject_python.sumar_listas(lst12, lst13)

params = {"lst12":lst12,"lst13": lst13}
mostrar_resultado('EJERCICIO 33. sumar_listas',params, result)


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

mi_figura = "rectangulo"
mis_datos = (5, 3)
result = ecalderonf_DataProject_python.calcular_area(mi_figura, mis_datos)

params = {"mi_figura":mi_figura,"mis_datos": mis_datos}
mostrar_resultado('EJERCICIO 40. calcular_area',params, result)


'''41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento.'''

# Ver programa ecalderonf_precio_final.py

