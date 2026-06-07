"""
Created on 2026
@author: kaliarroyo-sudo

Clase Libro:
Ejemplo de atributos públicos vs privados.
"""

class Libro:
    def __init__(self, titulo, autor, disponible=True):
        # atributo privado: no accesible directamente desde fuera
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = disponible

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            print(f"El libro '{self.__titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.__titulo}' no está disponible.")

    def devolver(self):
        self.__disponible = True
        print(f"El libro '{self.__titulo}' ha sido devuelto.")

    def mostrarDetalles(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        print(f"Título: {self.__titulo} | Autor: {self.__autor} | Estado: {estado}")

    def __str__(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"Libro: {self.__titulo} ({self.__autor}) - {estado}"
