"""
Clase LibroFisico:
Hereda de Libro y añade atributo de ubicación física.
"""

from Libro import Libro

class LibroFisico(Libro):
    def __init__(self, titulo, autor, estante):
        super().__init__(titulo, autor)
        self.estante = estante  # atributo propio

    def mostrarUbicacion(self):
        print(f"Ubicación física: Estante {self.estante}")

    def __str__(self):
        msg = super().__str__()
        msg += f" | Ubicación: Estante {self.estante}"
        return msg
