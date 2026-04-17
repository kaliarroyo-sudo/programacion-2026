"""
Created on Feb, 2026
@author: kaliarroyo-sudo

Clase Libro:
Representa un libro dentro de la biblioteca.
"""

class Libro:
    def __init__(self, titulo, autor, estado="Disponible"):
        self.titulo = titulo
        self.autor = autor
        self.estado = estado

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

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} ({self.estado})"
