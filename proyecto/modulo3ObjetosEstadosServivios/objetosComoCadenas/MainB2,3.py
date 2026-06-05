"""
Archivo Principal:
Demuestra cómo los objetos se imprimen como cadenas con __str__.
"""

from Libro import Libro
from Usuario import Usuario

class Main:
    pass

print("=== Pruebas de objetos como cadenas ===")

# Crear libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
print("\n--- Libro inicial ---")
print(libro1)

# Prestar libro
libro1.prestar()
print("\n--- Libro después de prestar ---")
print(libro1)

# Crear usuario con libro
usuario1 = Usuario("Virginia", "Calle Falsa 123", 25, libro1)
print("\n--- Usuario con libro ---")
print(usuario1)
