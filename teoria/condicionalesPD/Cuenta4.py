"""
Created on Mar, 2026
@author: kaliarroyo-sudo

Clase Cuenta:
Representa una cuenta bancaria con operaciones básicas.
Incluye condicionales en los métodos para validar operaciones.
"""

class Cuenta:
    def __init__(self, valor, tipo):
        """
        Constructor de la clase Cuenta.
        Parámetros:
            valor (float): saldo inicial
            tipo (str): tipo de cuenta (ej. 'Débito', 'Crédito')
        """
        self.cantidad = valor
        self.tipo = tipo

    def imprimirDetalles(self):
        """
        Muestra los detalles de la cuenta.
        """
        print("=== Detalles de la cuenta ===")
        print("Saldo actual:", self.cantidad)
        print("Tipo de cuenta:", self.tipo)

    def retirar(self, cantidad):
        """
        Retira dinero de la cuenta si hay saldo suficiente.
        """
        if cantidad > 0 and cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print(f"Se retiraron {cantidad}. Nuevo saldo: {self.cantidad}")
            return True
        else:
            print("Fondos insuficientes o cantidad inválida.")
            return False

    def depositar(self, cantidad):
        """
        Deposita dinero en la cuenta si la cantidad es positiva.
        """
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"Se depositaron {cantidad}. Nuevo saldo: {self.cantidad}")
            return True
        else:
            print("El monto debe ser positivo.")
            return False

    def __str__(self):
        """
        Representación legible del objeto Cuenta.
        """
        return f"Saldo: {self.cantidad} | Tipo: {self.tipo}"
