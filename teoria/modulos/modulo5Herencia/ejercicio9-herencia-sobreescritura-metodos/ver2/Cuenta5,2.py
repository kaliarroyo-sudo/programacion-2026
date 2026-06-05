"""
Created on 2026
kaliarroyo-sudo

Clase Cuenta:
Clase madre con atributo privado y métodos básicos.
"""

class Cuenta:
    def __init__(self, valor):
        self.__cantidad = valor

    def depositar(self, valor):
        if valor > 0:
            self.__cantidad += valor
        else:
            print("El valor para depositar es erróneo.")

    def __str__(self):
        return f"Clase Madre:: Saldo: {self.__cantidad}"
