"""
Created on Mayo 2026
@author: kaliarroyo-sudo

Clase Cuenta:
Clase base que define atributos y métodos comunes.
"""

class Cuenta:
    def __init__(self, valor):
        # atributo privado para proteger el saldo
        self.__cantidad = valor

    def depositar(self, valor):
        """
        Método para depositar dinero en la cuenta.
        """
        if valor > 0:
            self.__cantidad += valor
            print(f"Se depositaron {valor}. Nuevo saldo: {self.__cantidad}")
        else:
            print("El valor para depositar es erróneo.")

    def retirar(self, valor):
        """
        Método para retirar dinero de la cuenta.
        """
        if valor > 0 and valor <= self.__cantidad:
            self.__cantidad -= valor
            print(f"Se retiraron {valor}. Nuevo saldo: {self.__cantidad}")
        else:
            print("Fondos insuficientes o valor inválido.")

    def mostrarDetalles(self):
        """
        Método heredado: muestra el saldo actual.
        """
        print("Saldo actual:", self.__cantidad)

    def __str__(self):
        """
        Representación legible del objeto Cuenta.
        """
        return f"Clase Madre:: Saldo: {self.__cantidad}"
