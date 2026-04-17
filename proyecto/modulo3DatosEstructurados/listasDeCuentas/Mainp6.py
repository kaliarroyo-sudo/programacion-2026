"""
Archivo principal (Main):
Demuestra el uso de listas de objetos (Libros) dentro de Cliente.
"""

from MenuCliente import MenuCliente

class Principal:
    pass

print("=== Algoritmo principal ===")

menu = MenuCliente()
opcion = ""
while opcion != "4":
    opcion = menu.menuLibros()
