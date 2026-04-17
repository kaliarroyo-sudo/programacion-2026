"""
Created on Feb, 2026
@author: kaliarroyo-sudo

Clase Cliente:
Representa un cliente de la biblioteca que puede tener múltiples libros prestados.
"""

from Libro import Libro

class Cliente:
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.libros = []  # lista de libros prestados

    def agregarLibro(self, libro):
        self.libros.append(libro)

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
