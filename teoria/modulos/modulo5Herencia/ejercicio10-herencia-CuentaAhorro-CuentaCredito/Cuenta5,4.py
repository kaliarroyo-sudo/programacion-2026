"""
Created on 2026
@author: kaliarroyo-sudo

Clase Cuenta:
Clase madre con operaciones básicas.
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
            print("Fondos insuficientes o monto inválido.")

    def __str__(self):
        return f"Saldo actual: {self.cantidad}"
