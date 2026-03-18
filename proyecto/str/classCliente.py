class Cliente:
    """
    Clase compuesta que representa un cliente de la biblioteca.
    Contiene un objeto de la clase Libro.
    Atributos:
        nombre (str): nombre del cliente
        direccion (str): dirección del cliente
        edad (int): edad del cliente
        libro (Libro): objeto de la clase Libro asociado al cliente
    """

    def __init__(self, nombre, direccion, edad, libro):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.libro = libro

    def mostrarDetalles(self):
        """Muestra los detalles del cliente y su libro asociado."""
        print("=== Detalles del cliente ===")
        print("Nombre:", self.nombre)
        print("Dirección:", self.direccion)
        print("Edad:", self.edad)
        print("Libro asociado:", self.libro)

    def __str__(self):
        """Representación legible del objeto Cliente."""
        return f"{self.nombre}, {self.edad} años, vive en {self.direccion}"
