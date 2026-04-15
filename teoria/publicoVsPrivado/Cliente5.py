"""
Created on Mar, 2026
@author: lunysska

Clase Cliente:
Representa un cliente del banco que está asociado a una cuenta.
Se demuestra la relación entre objetos: un Cliente contiene una Cuenta.
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

    def mostrarDetalles(self):
        """
        Muestra los detalles del cliente y de su cuenta asociada.
        """
        print("\n=== Detalles del cliente ===")
        print("Nombre:", self.nombre)
        print("Dirección:", self.direccion)
        print("Edad:", self.edad)
        # Relación entre objetos: Cliente accede a Cuenta mediante método público
        self.cuenta.mostrarDetalles()
