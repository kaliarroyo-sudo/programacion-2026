"""
Clase LibroFisico:
Hereda de Libro y añade atributo de ubicación física.
"""

from Libro import Libro

class LibroFisico(Libro):
    def __init__(self, titulo, autor, ubicacion):
        super().__init__(titulo, autor)
        self.ubicacion = ubicacion

    def __str__(self):
        msg = super().__str__()
        msg += f" | Ubicación: {self.ubicacion}"
        return msg
