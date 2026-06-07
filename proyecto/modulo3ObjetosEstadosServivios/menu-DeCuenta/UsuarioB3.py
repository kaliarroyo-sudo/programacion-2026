"""
Clase Usuario:
Representa un usuario de la biblioteca digital.
"""

class Usuario:
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.libros = []  # relación: lista de libros prestados

    def agregarLibro(self, libro):
        self.libros.append(libro)

    def eliminarLibro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)

    def infoLibros(self):
        print(f"--- Cantidad de libros prestados: {len(self.libros)} ---")
        for libro in self.libros:
            print(libro)

    def __str__(self):
        return f"Usuario: {self.nombre}, {self.edad} años, Dirección: {self.direccion}"
