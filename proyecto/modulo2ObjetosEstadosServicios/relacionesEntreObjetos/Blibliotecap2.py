"""
Clase Biblioteca:
Representa la biblioteca que contiene libros y clientes.
"""

from Cliente import Cliente
from Libro import Libro

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []    # relación: lista de objetos Libro
        self.clientes = []  # relación: lista de objetos Cliente

    def agregarLibro(self, libro):
        self.libros.append(libro)

    def registrarCliente(self, cliente):
        self.clientes.append(cliente)

    def mostrarInventario(self):
        print(f"\n=== Inventario de {self.nombre} ===")
        for libro in self.libros:
            print(" -", libro)

    def mostrarClientes(self):
        print(f"\n=== Clientes registrados en {self.nombre} ===")
        for cliente in self.clientes:
            print(" -", cliente)
