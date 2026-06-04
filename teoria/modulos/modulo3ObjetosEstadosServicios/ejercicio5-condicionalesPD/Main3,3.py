"""
Created on Febrero, 2019
@author: lunysska

Archivo principal (Main):
Ejecuta el menú bancario con condicionales.
"""

from Menu import Menu

class Main:
    pass

menu = Menu("Bienvenidos al Banco Pato")
menu.darBienvenida()

opcion = ""
while opcion != "4":
    opcion = menu.despliegaMenu()
    menu.procesaOpcion(opcion)
