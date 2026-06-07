"""
Archivo de Pruebas:
Demuestra herencia, métodos y atributos en la Biblioteca Digital.
"""

from Libro import Libro
from LibroDigital import LibroDigital
from LibroFisico import LibroFisico
from Usuario import Usuario

class Pruebas:
    pass

print("\n********* Clase Madre (Libro) *********")
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry")
print(libro1)
libro1.prestar()
print(libro1)

print("\n********* Clase Hija (LibroDigital) *********")
libro2 = LibroDigital("Cien años de soledad", "Gabriel García Márquez", "PDF")
print(libro2)

print("\n********* Clase Hija (LibroFisico) *********")
libro3 = LibroFisico("Pedro Páramo", "Juan Rulfo", "Estante A3")
print(libro3)

print("\n********* Clase Usuario *********")
usuario1 = Usuario("Virginia", "Calle Falsa 123", 25, libro1)
print(usuario1)
