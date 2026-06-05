"""
Created on 2026
@author: kaliarroyo-sudo

Clase Libro:
Representa un libro en la biblioteca digital.
"""

class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = disponible

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
        else:
            print(f"El libro '{self.__titulo}' ya está prestado.")

    def devolver(self):
        self.__disponible = True

    def __str__(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"Libro: {self.__titulo} | Autor: {self.__autor} | Estado: {estado}"
