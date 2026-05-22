"""
Created on Mayo 2026
@author: kaliarroyo-sudo

Clase CuentaHija:
Hereda de Cuenta y añade un atributo extra (tipo de cuenta).
"""

from Cuenta import Cuenta

class CuentaHija(Cuenta):
    def __init__(self, valor, tipo):
        # llamar al constructor de la clase madre
        super().__init__(valor)
        self.__tipo = tipo

    def mostrarTipo(self):
        """
        Método propio de la clase hija.
        """
        print(f"Tipo de cuenta: {self.__tipo}")

    def __str__(self):
        """
        Sobreescribe __str__ para añadir el tipo de cuenta.
        """
        msg = super().__str__()
        msg += f" | Tipo: {self.__tipo}"
        return msg
