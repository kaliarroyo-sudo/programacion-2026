"""
Created on 2026
@author: kaliarroyo-sudo

Clase Libro:
Representa un libro dentro de la biblioteca digital.
"""

class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible  # estado del libro

    def prestar(self):
        """
        Servicio: prestar un libro si está disponible.
        """
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        """
        Servicio: devolver un libro.
        """
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

    def mostrarDetalles(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"Título: {self.titulo} | Autor: {self.autor} | Estado: {estado}")

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro: {self.titulo} ({self.autor}) - {estado}"
