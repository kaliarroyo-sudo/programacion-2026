"""
Created on Feb, 2026
@author: kaliarroyo-sudo

Clase Cuenta:
Representa una cuenta bancaria con operaciones básicas.
"""

class Cuenta:
    def __init__(self, valor):
        self.cantidad = valor  # atributo público

    def depositar(self, valor):
        if valor > 0:
            self.cantidad += valor
            print(f"Se depositaron {valor}. Nuevo saldo: {self.cantidad}")
        else:
            print("El valor para depositar es erróneo.")

    def mostrarDetalles(self):
        print("Saldo actual de la cuenta:", self.cantidad)

    def __str__(self):
        return f"Cuenta | Saldo: {self.cantidad}"
