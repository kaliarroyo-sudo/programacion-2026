"""
Created on November, 2018
@author: lunysska

Clase Cuenta:
Clase base para cuentas bancarias.
"""

class Cuenta:
    def __init__(self, valor):
        self.cantidad = valor

    def depositar(self, valor):
        if valor > 0:
            self.cantidad += valor
        else:
            print("El valor para depositar es erróneo.")

    def retirar(self, valor):
        if valor > 0 and valor <= self.cantidad:
            self.cantidad -= valor
        else:
            print("Fondos insuficientes o valor inválido.")

    def __str__(self):
        return f"Saldo actual: {self.cantidad}"
