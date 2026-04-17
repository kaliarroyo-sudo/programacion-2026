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
        self.libros = []

    def prestarLibro(self, libro):
        """
        Intenta prestar un libro al cliente.
        """
        if libro.prestar():   # condicional: solo se agrega si el préstamo fue exitoso
            self.libros.append(libro)

    def devolverLibro(self, indice):
        """
        Devuelve un libro según su índice.
        """
        if 0 <= indice < len(self.libros):   # condicional: validar índice
            libro = self.libros.pop(indice)
            libro.devolver()
        else:
            print("Índice inválido. No se pudo devolver el libro.")

    def mostrarDetalles(self):
        print("\n=== Detalles del cliente ===")
        print("Nombre:", self.nombre)
        print("Dirección:", self.direccion)
        print("Edad:", self.edad)
        if len(self.libros) > 0:   # condicional: validar si tiene libros
            print("Libros prestados:")
            for libro in self.libros:
                print(" -", libro)
        else:
            print("No tiene libros prestados.")
