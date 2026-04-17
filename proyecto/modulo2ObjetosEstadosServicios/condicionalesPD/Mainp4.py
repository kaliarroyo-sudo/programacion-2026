"""
Archivo principal (Main):
Demuestra el uso de condicionales en la Biblioteca Digital.
"""

from Libro import Libro
from Cliente import Cliente

class Main:
    pass

print("=== Pruebas con condicionales en la Biblioteca Digital ===")

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")

# Crear cliente
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25)

# --- Condicional: prestar libro ---
print("\n*** 1. Intento de préstamo ***")
cliente1.prestarLibro(libro1)   # se presta con éxito
cliente1.prestarLibro(libro1)   # ya está prestado, condicional evita duplicado

# --- Condicional: devolver libro ---
print("\n*** 2. Intento de devolución ***")
cliente1.devolverLibro(0)       # devuelve el libro
cliente1.devolverLibro(5)       # índice inválido, condicional evita error

# --- Condicional: mostrar detalles ---
print("\n*** 3. Mostrar detalles del cliente ***")
cliente1.mostrarDetalles()
