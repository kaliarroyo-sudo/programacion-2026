"""
Created on Mar, 2026
@author: lunysska

Clase Cuenta:
Demuestra el uso de atributos privados en Python.
El atributo __cantidad es privado y solo puede ser accedido
mediante métodos públicos.
"""

class Cuenta:
    def __init__(self, valor):
        """
        Constructor de la clase Cuenta.
        Parámetros:
            valor (float): saldo inicial de la cuenta
        """
        self.__cantidad = valor  # atributo privado

    def depositar(self, valor):
        """
        Método público para depositar dinero en la cuenta.
        """
        if valor > 0:
            self.__cantidad += valor
            print(f"Se depositaron {valor}. Nuevo saldo: {self.__cantidad}")
        else:
            print("El valor para depositar es erróneo.")

    def mostrarDetalles(self):
        """
        Método público para mostrar el saldo actual.
        """
        print("=== Detalles de la cuenta ===")
        print("Saldo actual:", self.__cantidad)

    def __str__(self):
        """
        Representación legible del objeto Cuenta.
        """
        return f"Saldo actual: {self.__cantidad}"
