"""
Archivo de Pruebas:
Demuestra el uso del operador punto en la Biblioteca Digital.
"""

from Libro import Libro

class Pruebas:
    pass

print("=== Desde las pruebas ===")

# Crear objeto de la clase Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")

# Acceder a atributos con el operador punto
print("Título:", libro1.titulo)
print("Autor:", libro1.autor)
