"""
Created on March, 2026
@author: kaliarroyo-sudo

Clase Cuenta:
Representa una cuenta bancaria simple.
"""

class Cuenta:
    def __init__(self, valor):
        self.__cantidad = valor  # atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__cantidad += valor
            return True
        else:
            print("El valor para depositar es erróneo.")
            return False

    def retirar(self, valor):
        if valor > 0 and valor <= self.__cantidad:
            self.__cantidad -= valor
            return True
        else:
            print("Fondos insuficientes o monto inválido.")
            return False

    def mostrarDetalles(self):
        print("Saldo actual:", self.__cantidad)

    def __str__(self):
        return f"Cuenta | Saldo: {self.__cantidad}"
