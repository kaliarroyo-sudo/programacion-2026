"""
Created on Feb, 2026
@author: kaliarroyo-sudo

Clase Cuenta:
Ejemplo de atributos y métodos vs acceso directo desde main.
"""

class Cuenta:
    def __init__(self, ctd, t):
        # atributos públicos
        self.cantidad = ctd
        self.tipo = t

    def imprimirDetalles(self):
        """
        Método que imprime los detalles de la cuenta.
        """
        print("=== Desde el método ===")
        print("Cantidad:", self.cantidad)
        print("Tipo:", self.tipo)
