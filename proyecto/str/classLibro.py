class Libro:
    """
    Clase base que representa un libro en la biblioteca.
    Atributos:
        titulo (str): título del libro
        autor (str): autor del libro
        estado (str): estado del libro (Disponible o Prestado)
    """

    def __init__(self, titulo, autor, estado="Disponible"):
        self.titulo = titulo
        self.autor = autor
        self.estado = estado

    def prestar(self):
        """Marca el libro como prestado si está disponible."""
        if self.estado == "Disponible":
            self.estado = "Prestado"
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        """Marca el libro como disponible si estaba prestado."""
        if self.estado == "Prestado":
            self.estado = "Disponible"
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

    def __str__(self):
        """Representación legible del objeto Libro."""
        return f"'{self.titulo}' de {self.autor} ({self.estado})"
