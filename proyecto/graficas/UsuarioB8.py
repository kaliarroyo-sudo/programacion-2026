"""
Clase Usuario:
Representa un usuario de la biblioteca.
Sept, 2019
@author: lunysska
"""

class Usuario:
    def __init__(self, nombre, apellido, direccion, edad, librosPrestados):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.edad = int(edad)
        self.librosPrestados = int(librosPrestados)

    def __str__(self):
        return f"{self.nombre} {self.apellido} | Edad: {self.edad} | Libros prestados: {self.librosPrestados}"
