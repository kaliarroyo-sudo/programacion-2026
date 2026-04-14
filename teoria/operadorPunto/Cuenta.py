"""
Created on Feb, 2026
@author: kaliarroyo-sudo

Clase Cuenta:
Representa una cuenta bancaria con atributos básicos y métodos
para mostrar detalles y manipular el saldo.
"""

class Cuenta:
    def __init__(self, cantidad, tipo):
        """
        Constructor de la clase.
        Parámetros:
            cantidad (float): saldo inicial de la cuenta
            tipo (str): tipo de cuenta (ej. 'Débito', 'Crédito')
        """
        self.cantidad = cantidad   # atributo que guarda el saldo
        self.tipo = tipo           # atributo que guarda el tipo de cuenta

    def imprimirDetalles(self):
        """
        Método que imprime los detalles de la cuenta.
        Se accede a los atributos usando el operador punto.
        """
        print("=== Detalles de la cuenta ===")
        print("Saldo actual:", self.cantidad)   # uso de self.cantidad
        print("Tipo de cuenta:", self.tipo)     # uso de self.tipo

