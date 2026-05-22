"""
Created on Mayo 2026
@author: kaliarroyo-sudo

Clase Cuenta:
Demuestra el uso de atributos públicos vs privados.
"""

class Cuenta:
    def __init__(self, valor):
        # PRIMERA VERSIÓN: atributo público
        # self.cantidad = valor

        # VERSIÓN FINAL: atributo privado
        self.__cantidad = valor

    def depositar(self, valor):
        if valor > 0:
            self.__cantidad += valor
        else:
            print("El valor para depositar es erróneo.")

    def mostrarDetalles(self):
        print("La cantidad de la cuenta::", self.__cantidad)

    def __str__(self):
        return f"Saldo actual: {self.__cantidad}"
