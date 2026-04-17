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
        self.libros = []  # relación: lista de objetos Libro

    def prestarLibro(self, libro):
        libro.prestar()
        if libro.estado == "Prestado":
            self.libros.append(libro)

    def devolverLibro(self, indice):
        if 0 <= indice < len(self.libros):
            libro = self.libros.pop(indice)
            libro.devolver()

    def mostrarDetalles(self):
        print("\n=== Detalles del cliente ===")
        print("Nombre:", self.nombre)
        print("Dirección:", self.direccion)
        print("Edad:", self.edad)
        print("Libros prestados:")
        for libro in self.libros:
            print(" -", libro)

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, vive en {self.direccion}"
