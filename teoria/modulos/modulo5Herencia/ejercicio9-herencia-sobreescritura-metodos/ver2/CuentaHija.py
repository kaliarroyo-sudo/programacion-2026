"""
Created on 2026
@author: kaliarroyo-sudo

Clase CuentaHija:
Hereda de Cuenta y sobreescribe el método __str__.
"""

from Cuenta import Cuenta

class CuentaHija(Cuenta):
    def __init__(self, valor, tipo):
        super().__init__(valor)  # llamada al constructor de la madre
        self.__tipo = tipo       # atributo propio de la hija

    def __str__(self):
        """
        Sobreescribe __str__ para añadir el tipo de cuenta.
        """
        msg = super().__str__()  # reutiliza el método de la madre
        msg += f" | Tipo: {self.__tipo}"
        return msg
