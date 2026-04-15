"""
Created on Mar, 2026
@author: kaliarroyo-sudo

Clase Cuenta:
Representa una cuenta bancaria con operaciones básicas.
Se utiliza el método especial __str__ para mostrar el estado de la cuenta.
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
        Método para depositar dinero en la cuenta.
        """
        if valor > 0:
            self.__cantidad += valor
            print(f"Se depositaron {valor}. Nuevo saldo: {self.__cantidad}")
        else:
            print("El valor para depositar es erróneo.")

    def __str__(self):
        """
        Representación legible del objeto Cuenta.
        """
        return f"La cantidad de la cuenta: {self.__cantidad}"
