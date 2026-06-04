"""
Created on 2026
@author: kaliarroyo-sudo

Clase Cuenta:
Ejemplo de atributo privado vs público.
"""

class Cuenta:
    def __init__(self, valor):
        # atributo privado: no accesible directamente desde fuera
        self.__cantidad = valor

    def depositar(self, valor):
        if valor > 0:
            self.__cantidad += valor
        else:
            print("El valor para depositar es erróneo.")

    def mostrarDetalles(self):
        print("Saldo actual:", self.__cantidad)

    def __str__(self):
        return f"Cuenta | Saldo: {self.__cantidad}"
