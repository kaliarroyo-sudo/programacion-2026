"""
Created on 2026
@author: kaliarroyo-sudo

Clase Cuenta:
Representa una cuenta bancaria con operaciones básicas.
"""

class Cuenta:
    def __init__(self, valor, tipo):
        self.cantidad = valor
        self.tipo = tipo

    def imprimirDetalles(self):
        print("=== Detalles de la cuenta ===")
        print("Saldo:", self.cantidad)
        print("Tipo:", self.tipo)

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print(f"Se retiraron {cantidad}. Nuevo saldo: {self.cantidad}")
            return True
        else:
            print("Fondos insuficientes o monto inválido.")
            return False

    def depositar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"Se depositaron {cantidad}. Nuevo saldo: {self.cantidad}")
            return True
        else:
            print("El monto debe ser positivo.")
            return False

    def __str__(self):
        return f"Saldo: {self.cantidad} | Tipo: {self.tipo}"
