"""
Clase CuentaAhorro:
Hereda de Cuenta y añade tasa de interés.
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
        self.cantidad += self.cantidad * self.tasaInteres

    def __str__(self):
        msg = super().__str__()
        msg += f" | Tasa de interés: {self.tasaInteres}"
        return msg
