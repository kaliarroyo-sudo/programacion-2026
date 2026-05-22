"""
Clase Cliente:
Representa un cliente que contiene una Cuenta.
"""

from Cuenta import Cuenta

class Cliente:
    def __init__(self, nombre, direccion, edad, cuenta):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.cuenta = cuenta

    def mostrarDetalles(self):
        print("Nombre::", self.nombre)
        print("Dirección::", self.direccion)
        print("Edad::", self.edad)
        self.cuenta.mostrarDetalles()
