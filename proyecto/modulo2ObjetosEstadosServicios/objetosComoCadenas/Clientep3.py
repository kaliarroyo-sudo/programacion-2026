"""
Clase Cliente:
Representa un cliente de la biblioteca que puede tener múltiples libros prestados.
"""

from Libro import Libro

class Cliente:
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.libros = []

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
        """
        Representación legible del objeto Cliente.
        """
        return (
            f"Cliente: {self.nombre}, {self.edad} años\n"
            f"Dirección: {self.direccion}\n"
            f"Libros prestados: {len(self.libros)}"
        )
