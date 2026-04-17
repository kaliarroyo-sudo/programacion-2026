"""
Clase Cliente:
Representa un cliente que puede tener múltiples libros prestados.
"""

from Libro import Libro

class Cliente:
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.libros = []  # lista de objetos Libro

    def prestarLibro(self, libro):
        libro.prestar()
        if "'Prestado'" in str(libro):  # condicional usando __str__
            self.libros.append(libro)

    def mostrarDetalles(self):
        print("\n=== Detalles del cliente ===")
        print("Nombre:", self.nombre)
        print("Dirección:", self.direccion)
        print("Edad:", self.edad)
        print("Libros prestados:")
        for libro in self.libros:
            print(" -", libro)
