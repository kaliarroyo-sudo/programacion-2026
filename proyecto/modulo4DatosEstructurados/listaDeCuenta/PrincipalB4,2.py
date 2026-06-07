"""
Archivo Principal:
Ejecuta el menú de usuario para la Biblioteca Digital.
"""

from MenuUsuario import MenuUsuario

class Principal:
    pass

menu = MenuUsuario()
opcion = ""
while opcion != "4":
    opcion = menu.menuLibros()
