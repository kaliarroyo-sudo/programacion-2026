"""
Created on May, 2026
@author: lunysska

Clase Libro:
Clase base que define atributos y métodos comunes para todos los libros.
"""

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.estado = "Disponible"  # atributo común

    def prestar(self):
        if self.estado == "Disponible":
            self.estado = "Prestado"
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if self.estado == "Prestado":
            self.estado = "Disponible"
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

    def mostrarDetalles(self):
        print(f"Título: {self.titulo} | Autor: {self.autor} | Estado: {self.estado}")

    def __str__(self):
        return f"Clase Madre:: '{self.titulo}' de {self.autor} ({self.estado})"
