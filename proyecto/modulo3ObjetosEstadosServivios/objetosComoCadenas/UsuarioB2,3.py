"""
Clase Usuario:
Representa un usuario de la biblioteca digital.
"""

from Libro import Libro

class Usuario:
    def __init__(self, nombre, direccion, edad, libro=None):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.__libro = libro  # relación: un usuario puede tener un libro

    def __str__(self):
        tmp = f"Nombre: {self.__nombre}\n"
        tmp += f"Dirección: {self.__direccion}\n"
        tmp += f"Edad: {self.__edad}\n"
        tmp += f"Libro: {self.__libro}" if self.__libro else "Libro: Ninguno"
        return tmp
