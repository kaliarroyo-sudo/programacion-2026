"""
Clase CuentaCredito:
Hereda de Cuenta y añade sobregiro.
"""

from Cuenta import Cuenta

class CuentaCredito(Cuenta):
    def __init__(self, saldoInicial, montoSobregiro):
        super().__init__(saldoInicial)
        self.montoSobregiro = montoSobregiro

    def retirar(self, valor):
        if valor <= self.cantidad:
            self.cantidad -= valor
        else:
            sobregiroNecesario = valor - self.cantidad
            if sobregiroNecesario <= self.montoSobregiro:
                self.cantidad = 0.0
                self.montoSobregiro -= sobregiroNecesario
            else:
                print("No se pudo retirar: sobregiro insuficiente.")
                return False
        return True

    def __str__(self):
        msg = super().__str__()
        msg += f" | Sobregiro disponible: {self.montoSobregiro}"
        return msg
