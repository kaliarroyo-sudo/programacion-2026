"""
Clase Cliente:
Representa un cliente que puede tener múltiples libros prestados.
Se usa una lista para almacenar los objetos Libro.
"""

from Libro import Libro

class Cliente:
    def __init__(self, nombre, direccion, edad):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.__libros = []  # lista vacía de libros prestados

    def agregarLibro(self, libro):
        """
        Agrega un libro a la lista si se pudo prestar.
        """
        if libro.prestar():
            self.__libros.append(libro)
            print(f"El cliente {self.__nombre} ha prestado {libro}")
        else:
            print(f"No se pudo prestar {libro}")

    def devolverLibro(self, indice):
        """
        Devuelve un libro según su índice en la lista.
        """
        if 0 <= indice < len(self.__libros):
            libro = self.__libros.pop(indice)
            libro.devolver()
            print(f"El cliente {self.__nombre} devolvió {libro}")
        else:
            print("Índice inválido. No se pudo devolver el libro.")

    def infoLibros(self):
        """
        Muestra información de todos los libros prestados.
        """
        print(f"\n--- {self.__nombre} tiene {len(self.__libros)} libro(s) ---")
        for i, libro in enumerate(self.__libros):
            print(f"Libro {i+1}: {libro}")

    def __str__(self):
        return f"Cliente: {self.__nombre}, {self.__edad} años, Dirección: {self.__direccion}"
