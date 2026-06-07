"""
Clase Usuario:
Representa un usuario que contiene un libro.
"""

from Libro import Libro

class Usuario:
    def __init__(self, nombre, direccion, edad, libro):
        # atributos públicos
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.libro = libro

    def mostrarDetalles(self):
        print("=== Detalles del usuario ===")
        print("Nombre:", self.nombre)
        print("Dirección:", self.direccion)
        print("Edad:", self.edad)
        self.libro.mostrarDetalles()
