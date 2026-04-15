"""
Created on March, 2026
@author: kaliarroyo-sudo

Clase Cuenta:
Representa una cuenta bancaria con operaciones básicas.
"""

class Cuenta:
    def __init__(self, cantidad):
        """
        Constructor de la clase Cuenta.
        Parámetros:
            cantidad (float): saldo inicial de la cuenta
        """
        self.cantidad = cantidad

    def depositar(self, valor):
        """
        Método para depositar dinero en la cuenta.
        """
        if valor > 0:
            self.cantidad += valor
            print(f"Se depositaron {valor}. Nuevo saldo: {self.cantidad}")
        else:
            print("El valor para depositar es erróneo.")

    def mostrarDetalles(self):
        """
        Muestra el saldo actual de la cuenta.
        """
        print("=== Detalles de la cuenta ===")
        print("Saldo actual:", self.cantidad)
