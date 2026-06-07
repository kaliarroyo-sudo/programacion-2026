"""
Archivo de Pruebas:
Demuestra herencia y relaciones en la Biblioteca Digital.
"""

from Libro import Libro
from LibroDigital import LibroDigital
from LibroFisico import LibroFisico
from Usuario import Usuario

class Pruebas:
    pass

print("\n********* Libro base *********")
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry")
print(libro1)

print("\n********* Libro Digital *********")
libro2 = LibroDigital("Cien años de soledad", "Gabriel García Márquez", "EPUB")
print(libro2)

print("\n********* Libro Físico *********")
libro3 = LibroFisico("Pedro Páramo", "Juan Rulfo", "Estante B2")
print(libro3)

print("\n********* Usuario *********")
usuario1 = Usuario("Alejandro", "Calle Flores No.25", 56)
print(usuario1)
usuario1.infoLibros()

print("\n--- Agregando libros ---")
usuario1.agregarLibro(libro1)
usuario1.agregarLibro(libro2)
usuario1.agregarLibro(libro3)
usuario1.infoLibros()

print("\n--- Eliminando un libro ---")
usuario1.eliminarLibro(libro1)
usuario1.infoLibros()
