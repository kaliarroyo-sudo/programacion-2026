"""
Created on March, 2026
@author: kaliarroyo-sudo

Clase Cliente:
Representa un cliente con múltiples cuentas.
"""

from Cuenta import Cuenta

class Cliente:
    def __init__(self, nombre, direccion, edad):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.__cuentas = []  # lista vacía de cuentas

    def agregarCuenta(self, cuenta):
        self.__cuentas.append(cuenta)

    def eliminarCuenta(self, cuenta):
        if cuenta in self.__cuentas:
            self.__cuentas.remove(cuenta)

    def infoCuentas(self):
        print(f"--- Cantidad de cuentas: {len(self.__cuentas)} ---")
        for cta in self.__cuentas:
            print(cta)

    def __str__(self):
        return f"Cliente: {self.__nombre}, {self.__edad} años, Dirección: {self.__direccion}"
