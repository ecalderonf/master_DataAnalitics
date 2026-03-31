
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

