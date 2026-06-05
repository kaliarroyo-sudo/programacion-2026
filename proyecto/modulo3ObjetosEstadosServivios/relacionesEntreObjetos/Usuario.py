"""
Clase Usuario:
Representa un usuario de la biblioteca digital.
"""

from Libro import Libro

class Usuario:
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.libros = []  # relación: lista de libros prestados

    def tomarPrestado(self, libro):
        """
        Servicio: tomar prestado un libro.
        """
        if libro.disponible:
            libro.prestar()
            self.libros.append(libro)
        else:
            print(f"{self.nombre} no puede tomar '{libro.titulo}', ya está prestado.")

    def devolverLibro(self, libro):
        """
        Servicio: devolver un libro.
        """
        if libro in self.libros:
            libro.devolver()
            self.libros.remove(libro)
        else:
            print(f"{self.nombre} no tiene el libro '{libro.titulo}'.")

    def mostrarDetalles(self):
        print(f"Usuario: {self.nombre}, {self.edad} años, Dirección: {self.direccion}")
        print(f"Libros prestados ({len(self.libros)}):")
        for libro in self.libros:
            print(" -", libro)

    def __str__(self):
        return f"Usuario: {self.nombre} ({self.edad} años)"
