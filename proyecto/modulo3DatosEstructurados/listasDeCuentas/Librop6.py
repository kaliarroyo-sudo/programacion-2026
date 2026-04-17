"""
Clase Libro:
Representa un libro dentro de la biblioteca.
"""

class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__estado = "Disponible"

    def prestar(self):
        if self.__estado == "Disponible":
            self.__estado = "Prestado"
            return True
        return False

    def devolver(self):
        if self.__estado == "Prestado":
            self.__estado = "Disponible"
            return True
        return False

    def __str__(self):
        return f"'{self.__titulo}' de {self.__autor} ({self.__estado})"
