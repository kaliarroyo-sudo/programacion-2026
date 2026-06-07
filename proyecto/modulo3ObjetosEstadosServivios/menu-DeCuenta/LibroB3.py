"""
Created on 2026
@author: kaliarroyo-sudo

Clase Libro:
Clase base para representar un libro en la biblioteca.
"""

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # estado inicial

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro: {self.titulo} | Autor: {self.autor} | Estado: {estado}"
