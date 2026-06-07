"""
Clase LibroDigital:
Hereda de Libro y sobreescribe métodos.
"""

from Libro import Libro

class LibroDigital(Libro):
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.__formato = formato

    """
    Este método se sobreescribe
    """
    def prestar(self):
        print(f"Descargando el libro digital en formato {self.__formato}...")
        super().prestar()

    def __str__(self):
        msg = super().__str__()
        msg += f" | Formato: {self.__formato}"
        return msg
