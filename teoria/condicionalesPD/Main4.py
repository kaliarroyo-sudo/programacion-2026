"""
Created on Febrero, 2026
@author: kaliarroyo-sudo

Archivo principal (Main):
Se realizan pruebas de la relación entre objetos Menu y Cuenta.
"""

from Menu import Menu

class Main:
    pass  # Clase vacía, punto de entrada

print("=== Algoritmo principal ===")

# Crear menú y dar bienvenida
menu = Menu("Bienvenidos al Banco Pato")
menu.darBienvenida()

# Ciclo de menú hasta que el usuario decida salir
opcion = ""
while opcion != "4":
    opcion = menu.despliegaMenu()
    menu.procesaOpcion(opcion)
