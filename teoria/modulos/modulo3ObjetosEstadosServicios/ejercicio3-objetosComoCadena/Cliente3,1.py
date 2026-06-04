"""
Created on Feb
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
        self.cuenta = cuenta

    def __str__(self):
        """
        Representación legible del objeto Cliente.
        """
        tmp = f"Nombre: {self.nombre}\n"
        tmp += f"Dirección: {self.direccion}\n"
        tmp += f"Edad: {self.edad}\n"
        tmp += f"La cuenta: {self.cuenta}"  # usa __str__ de Cuenta
        return tmp
