"""
Created on Abril, 2026
@author: kaliarroyo-sudo

Archivo principal (Main):
Se realizan pruebas de la relación entre objetos Cliente y Cuenta
mediante un menú interactivo.
"""

from MenuCliente import MenuCliente

class Principal:
    pass  # Clase vacía, punto de entrada

print("=== Algoritmo principal ===")

menu = MenuCliente()
opcion = ""
while opcion != "4":
    opcion = menu.menuCuentas()
