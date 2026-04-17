"""
Clase Libro:
Representa un libro dentro de la biblioteca.
Incluye condicionales para validar préstamos y devoluciones.
"""

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.estado = "Disponible"

    def prestar(self):
        """
        Presta el libro si está disponible.
        """
        if self.estado == "Disponible":   # condicional
            self.estado = "Prestado"
            print(f"El libro '{self.titulo}' ha sido prestado.")
            return True
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")
            return False

    def devolver(self):
        """
        Devuelve el libro si estaba prestado.
        """
        if self.estado == "Prestado":     # condicional
            self.estado = "Disponible"
            print(f"El libro '{self.titulo}' ha sido devuelto.")
            return True
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")
            return False

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} ({self.estado})"
