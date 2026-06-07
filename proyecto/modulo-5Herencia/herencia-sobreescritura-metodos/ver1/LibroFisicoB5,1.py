"""
Clase LibroFisico:
Hereda de Libro y sobreescribe __str__ para añadir ubicación.
"""

from Libro import Libro

class LibroFisico(Libro):
    def __init__(self, titulo, autor, ubicacion):
        super().__init__(titulo, autor)
        self.__ubicacion = ubicacion

    """
    Este método se sobreescribe
    """
    def __str__(self):
        msg = super().__str__()
        msg += f" | Ubicación: {self.__ubicacion}"
        return msg
