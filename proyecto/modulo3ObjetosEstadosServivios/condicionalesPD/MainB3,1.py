"""
Created on 2026
@author: kaliarroyo-sudo

Archivo principal (Main):
Ejecuta el menú de la Biblioteca Digital con condicionales.
"""

from Menu import Menu

class Main:
    pass

menu = Menu("Bienvenidos a la Biblioteca Digital")
menu.darBienvenida()

opcion = ""
while opcion != "4":
    opcion = menu.despliegaMenu()
    menu.procesaOpcion(opcion)
