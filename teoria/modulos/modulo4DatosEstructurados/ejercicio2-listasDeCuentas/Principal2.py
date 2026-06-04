"""
Archivo Principal:
Ejecuta el menú de cuentas.
"""

from MenuCliente import MenuCliente

class Principal:
    pass

menu = MenuCliente()
opcion = ""
while opcion != "4":
    opcion = menu.menuCuentas()
