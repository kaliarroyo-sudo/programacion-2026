"""
Clase Cliente:
Representa un cliente que puede tener diferentes tipos de libros.
"""

class Cliente:
    def __init__(self, nombre, direccion, edad, libro):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.libro = libro

    def mostrarDetalles(self):
        print("Nombre:", self.nombre)
        print("Dirección:", self.direccion)
        print("Edad:", self.edad)
        self.libro.mostrarDetalles()

    def __str__(self):
        return (
            f"Cliente: {self.nombre}\n"
            f"Dirección: {self.direccion}\n"
            f"Edad: {self.edad}\n"
            f"{self.libro}"
        )
