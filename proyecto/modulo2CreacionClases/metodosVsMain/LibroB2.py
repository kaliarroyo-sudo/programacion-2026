"""
Created on Febrero, 2026
@author: kaliarroyo-sudo

Clase Libro:
Ejemplo de atributos y métodos vs acceso directo desde main.
"""

class Libro:
    def __init__(self, titulo, autor):
        # atributos públicos
        self.titulo = titulo
        self.autor = autor

    def imprimirDetalles(self):
        """
        Método que imprime los detalles del libro.
        """
        print("=== Desde el método ===")
        print("Título:", self.titulo)
        print("Autor:", self.autor)
