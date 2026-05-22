"""
Clase LibroDigital:
Hereda de Libro y añade atributo de acceso en línea.
"""

from Libro import Libro

class LibroDigital(Libro):
    def __init__(self, titulo, autor, url):
        super().__init__(titulo, autor)
        self.url = url  # atributo propio

    def mostrarAcceso(self):
        print(f"Acceso digital: {self.url}")

    def __str__(self):
        msg = super().__str__()
        msg += f" | Acceso en línea: {self.url}"
        return msg
