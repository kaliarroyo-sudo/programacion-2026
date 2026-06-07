"""
Created on 2026
@author: kaliarroyo-sudo
Clase Libro:
Clase madre con operaciones básicas.
"""

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
            return True
        else:
            print(f"El libro '{self.titulo}' no está disponible.")
            return False

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro: {self.titulo} | Autor: {self.autor} | Estado: {estado}"
