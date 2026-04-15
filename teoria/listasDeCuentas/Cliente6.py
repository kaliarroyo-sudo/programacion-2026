"""
Created on Abril, 2026
@author: kaliarroyo-sudo

Clase Cliente:
Representa un cliente del banco que puede tener múltiples cuentas.
Se demuestra la relación entre objetos: un Cliente contiene una lista de Cuentas.
"""

from Cuenta import Cuenta

class Cliente:
    def __init__(self, nombre, direccion, edad):
        """
        Constructor de la clase Cliente.
        Parámetros:
            nombre (str): nombre del cliente
            direccion (str): dirección del cliente
            edad (int): edad del cliente
        """
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.__cuentas = []  # lista vacía de cuentas

    def agregarCuenta(self, cuenta):
        """
        Agrega una cuenta a la lista de cuentas del cliente.
        """
        self.__cuentas.append(cuenta)

    def eliminarCuenta(self, indice):
        """
        Elimina una cuenta de la lista según su índice.
        """
        if 0 <= indice < len(self.__cuentas):
            cuenta_eliminada = self.__cuentas.pop(indice)
            print(f"Se eliminó la cuenta con saldo: {cuenta_eliminada.cantidad}")
        else:
            print("Índice inválido. No se pudo eliminar la cuenta.")

    def infoCuentas(self):
        """
        Muestra información de todas las cuentas del cliente.
        """
        print(f"\n--- {self.__nombre} tiene {len(self.__cuentas)} cuenta(s) ---")
        for i, cta in enumerate(self.__cuentas):
            print(f"Cuenta {i+1}: {cta}")

    def __str__(self):
        """
        Representación legible del objeto Cliente.
        """
        return (
            f"Nombre: {self.__nombre}\n"
            f"Dirección: {self.__direccion}\n"
            f"Edad: {self.__edad}"
        )
