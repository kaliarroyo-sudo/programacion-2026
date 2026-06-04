"""
Created on Febrero, 2026
@author: kaliarroyo-sudo

Clase Cliente:
Representa un cliente que contiene una Cuenta.
"""

from Cuenta import Cuenta

class Cliente:
    def __init__(self, nombre, direccion, edad, cuenta):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.cuenta = cuenta  # relación: Cliente contiene una Cuenta

    def mostrarDetalles(self):
        print("=== Detalles del cliente ===")
        print("Nombre:", self.nombre)
        print("Dirección:", self.direccion)
        print("Edad:", self.edad)
        # relación: se llama al método de la cuenta
        self.cuenta.mostrarDetalles()

    def __str__(self):
        return f"Cliente: {self.nombre}, {self.edad} años, Dirección: {self.direccion}\n{self.cuenta}"
