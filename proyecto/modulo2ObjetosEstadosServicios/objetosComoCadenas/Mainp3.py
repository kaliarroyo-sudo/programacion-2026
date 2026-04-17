"""
Archivo principal (Main):
Se demuestra cómo los objetos se convierten en cadenas con __str__.
"""

from Libro import Libro
from Cliente import Cliente

class Main:
    pass

print("=== Pruebas de objetos como cadenas ===")

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")

# Crear cliente
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25)

# Agregar libros al cliente
cliente1.agregarLibro(libro1)
cliente1.agregarLibro(libro2)

# --- Uso directo de print con objetos ---
print("\n*** 1. Imprimir objetos Libro directamente ***")
print(libro1)   # gracias a __str__
print(libro2)

print("\n*** 2. Imprimir objeto Cliente directamente ***")
print(cliente1)

print("\n*** 3. Usar métodos para mostrar detalles ***")
cliente1.mostrarDetalles()
