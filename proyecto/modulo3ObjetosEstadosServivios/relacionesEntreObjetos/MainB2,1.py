"""
Archivo Principal:
Demuestra objetos, estados, servicios y relaciones entre objetos
en el proyecto Biblioteca Digital.
"""

from Libro import Libro
from Usuario import Usuario

class Main:
    pass

print("=== Pruebas de Biblioteca Digital ===")

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("Pedro Páramo", "Juan Rulfo")

# Mostrar estado inicial
libro1.mostrarDetalles()
libro2.mostrarDetalles()

# Crear usuario
usuario1 = Usuario("Virginia", "Calle Falsa 123", 25)
usuario1.mostrarDetalles()

# Relación: usuario toma prestado un libro
print("\n--- Virginia toma prestado un libro ---")
usuario1.tomarPrestado(libro1)
usuario1.mostrarDetalles()

# Intentar prestar el mismo libro otra vez
print("\n--- Intento de prestar libro ya prestado ---")
usuario1.tomarPrestado(libro1)

# Devolver libro
print("\n--- Virginia devuelve el libro ---")
usuario1.devolverLibro(libro1)
usuario1.mostrarDetalles()

# Estado final de los libros
print("\n=== Estado final de los libros ===")
libro1.mostrarDetalles()
libro2.mostrarDetalles()
