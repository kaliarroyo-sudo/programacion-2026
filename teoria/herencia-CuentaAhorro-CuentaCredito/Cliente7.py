"""
Created on mayo
@author: kaliarroyo-sudo

Clase Cliente:
Representa un cliente que puede tener diferentes tipos de cuentas.
"""

class Cliente:
    def __init__(self, nombre, direccion, edad, cuenta):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.cuenta = cuenta

    def __str__(self):
        tmp = f"Nombre: {self.nombre}\n"
        tmp += f"Dirección: {self.direccion}\n"
        tmp += f"Edad: {self.edad}\n"
        tmp += f"{self.cuenta}"  # usa __str__ de la cuenta
        return tmp
