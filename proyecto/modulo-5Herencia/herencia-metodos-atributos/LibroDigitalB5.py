"""
Clase LibroDigital:
Hereda de Libro y añade atributo de formato.
"""

from Libro import Libro

class LibroDigital(Libro):
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.__formato = formato

    def __str__(self):
        msg = super().__str__()
        msg += f" | Formato: {self.__formato}"
        return msg
