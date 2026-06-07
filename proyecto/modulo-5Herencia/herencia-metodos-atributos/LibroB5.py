"""
Created on 2026
@author: kaliarroyo-sudo

Clase Libro:
Clase madre con atributos básicos.
"""

class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            print(f"El libro '{self.__titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.__titulo}' no está disponible.")

    def devolver(self):
        self.__disponible = True
        print(f"El libro '{self.__titulo}' ha sido devuelto.")

    def __str__(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"Libro: {self.__titulo} | Autor: {self.__autor} | Estado: {estado}"
