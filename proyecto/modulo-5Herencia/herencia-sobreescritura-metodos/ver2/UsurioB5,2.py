"""
Clase Usuario:
Representa un usuario que contiene un libro.
"""

class Usuario:
    def __init__(self, nombre, direccion, edad, libro):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.libro = libro

    def __str__(self):
        tmp = f"Nombre: {self.nombre}\n"
        tmp += f"Dirección: {self.direccion}\n"
        tmp += f"Edad: {self.edad}\n"
        tmp += f"Libro: {self.libro}"
        return tmp
