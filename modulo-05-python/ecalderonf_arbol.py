'''34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos.
Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol .
El objetivo es implementar estos métodos para manipular la estructura del árbol.
Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método
crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método
nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método
crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método
quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método
info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
mismas.'''
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición inválida. No se puede quitar la rama.")

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# 1. Crear un árbol
arbol = Arbol()

# 2. Hacer crecer el tronco del árbol una unidad
arbol.crecer_tronco()

# 3. Añadir una nueva rama al árbol
arbol.nueva_rama()

# 4. Hacer crecer todas las ramas del árbol una unidad
arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas al árbol
arbol.nueva_rama()
arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2
arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol
print(arbol.info_arbol())


