"""
Created on mayo 
@author: kaliarroyo-sudo

Clase Cuenta:
Clase base para diferentes tipos de cuentas bancarias.
"""

class Cuenta:
    def __init__(self, valor):
        """
        Constructor de la clase Cuenta.
        Parámetros:
            valor (float): saldo inicial
        """
        self.cantidad = valor

    def depositar(self, valor):
        """
        Método para depositar dinero en la cuenta.
        """
        if valor > 0:
            self.cantidad += valor
        else:
            print("El valor para depositar es erróneo.")

    def retirar(self, valor):
        """
        Método para retirar dinero de la cuenta.
        """
        if valor > 0 and valor <= self.cantidad:
            self.cantidad -= valor
        else:
            print("Fondos insuficientes o valor inválido.")

    def __str__(self):
        """
        Representación legible del objeto Cuenta.
        """
        return f"Saldo actual: {self.cantidad}"
