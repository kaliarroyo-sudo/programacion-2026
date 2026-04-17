"""
Clase Libro:
Demuestra el uso de atributos privados en Python.
"""

class Libro:
    def __init__(self, titulo, autor):
        # atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__estado = "Disponible"

    # Métodos públicos para acceder/controlar atributos privados
    def prestar(self):
        if self.__estado == "Disponible":
            self.__estado = "Prestado"
            print(f"El libro '{self.__titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.__titulo}' ya está prestado.")

    def devolver(self):
        if self.__estado == "Prestado":
            self.__estado = "Disponible"
            print(f"El libro '{self.__titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.__titulo}' no estaba prestado.")

    def mostrarDetalles(self):
        print("=== Detalles del libro ===")
        print("Título:", self.__titulo)
        print("Autor:", self.__autor)
        print("Estado:", self.__estado)

    def __str__(self):
        return f"'{self.__titulo}' de {self.__autor} ({self.__estado})"
