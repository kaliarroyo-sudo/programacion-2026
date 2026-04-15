"""
Created on Abril, 2026
@author: kaliarroyo-sudo

Clase Cuenta:
Representa una cuenta bancaria con operaciones básicas.
"""

class Cuenta:
    def __init__(self, valor):
        """
        Constructor de la clase Cuenta.
        Parámetros:
            valor (float): saldo inicial de la cuenta
        """
        self.cantidad = valor

    def depositar(self, valor):
        """
        Método para depositar dinero en la cuenta.
        """
        if valor > 0:
            self.cantidad += valor
            return True
        else:
            print("El valor para depositar es erróneo.")
            return False

    def retirar(self, valor):
        """
        Método para retirar dinero de la cuenta.
        """
        if valor > 0 and valor <= self.cantidad:
            self.cantidad -= valor
            return True
        else:
            print("Fondos insuficientes o valor inválido.")
            return False

    def __str__(self):
        """
        Representación legible del objeto Cuenta.
        """
        return f"Saldo de la cuenta: {self.cantidad}"
