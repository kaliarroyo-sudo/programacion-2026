"""
Archivo principal (Main):
Demuestra el uso de atributos públicos vs privados en la Biblioteca Digital.
"""

from Libro import Libro
from Cliente import Cliente

class Main:
    pass

print("=== Pruebas de público vs privado en la Biblioteca Digital ===")

# Crear libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")

# Usar métodos públicos
libro1.mostrarDetalles()
libro1.prestar()
libro1.mostrarDetalles()

# Intento de acceder directamente a atributo privado (esto dará error)
print("\nIntentamos acceder directamente al atributo privado:")
try:
    print(libro1.__titulo)  # acceso directo prohibido
except AttributeError as e:
    print("Error:", e)

# Crear cliente y prestar libro
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25)
cliente1.prestarLibro(libro1)
cliente1.mostrarDetalles()
