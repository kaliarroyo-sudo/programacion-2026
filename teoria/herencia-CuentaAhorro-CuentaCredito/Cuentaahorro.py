"""
Created on mayo
@author: kaliarroyo-sudo

Clase CuentaAhorro:
Subclase de Cuenta que añade tasa de interés.
"""

from Cuenta import Cuenta

class CuentaAhorro(Cuenta):
    def __init__(self, saldoInicial, tasaInteres):
        super().__init__(saldoInicial)
        self.tasaInteres = tasaInteres

    def aplicarInteres(self):
        """
        Aplica la tasa de interés al saldo.
        """
        interes = self.cantidad * self.tasaInteres
        self.cantidad += interes
        print(f"Se aplicó interés de {interes}. Nuevo saldo: {self.cantidad}")

    def __str__(self):
        msg = super().__str__()
        msg += f" | Tasa de interés: {self.tasaInteres}"
        return msg
