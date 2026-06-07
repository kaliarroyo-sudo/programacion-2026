"""
Clase Usuario:
Representa un usuario con una lista de libros.
"""

from Libro import Libro

class Usuario:
    def __init__(self, nombre, direccion, edad):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.__libros = []  # lista vacía de libros

    def agregarLibro(self, libro):
        self.__libros.append(libro)

    def eliminarLibro(self, libro):
        if libro in self.__libros:
            self.__libros.remove(libro)

    def infoLibros(self):
        print(f"--- Cantidad de libros: {len(self.__libros)} ---")
        for libro in self.__libros:
            print(libro)

    def __str__(self):
        return f"Usuario: {self.__nombre}, {self.__edad} años, Dirección: {self.__direccion}"
