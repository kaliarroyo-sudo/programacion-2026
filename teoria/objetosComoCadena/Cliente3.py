"""
Created on Mar, 2026
@author: kaliarroyo-sudo

Clase Cliente:
Representa un cliente del banco que está asociado a una cuenta.
Se demuestra la relación entre objetos: un Cliente contiene un objeto Cuenta.
"""

from Cuenta import Cuenta

class Cliente:
    def __init__(self, nombre, direccion, edad, cuenta):
        """
        Constructor de la clase Cliente.
        Parámetros:
            nombre (str): nombre del cliente
            direccion (str): dirección del cliente
            edad (int): edad del cliente
            cuenta (Cuenta): objeto de la clase Cuenta asociado al cliente
        """
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.cuenta = cuenta

    def __str__(self):
        """
        Representación legible del objeto Cliente.
        """
        return (
            f"Nombre: {self.nombre}\n"
            f"Dirección: {self.direccion}\n"
            f"Edad: {self.edad}\n"
            f"{self.cuenta}"  # relación: imprime el objeto Cuenta con su __str__
        )
