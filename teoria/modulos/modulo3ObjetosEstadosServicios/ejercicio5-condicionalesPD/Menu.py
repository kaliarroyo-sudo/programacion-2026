"""
Created on Marzo, 2026
@author: kaliarroyo-sudo

Clase Menu:
Controla las opciones de interacción con la cuenta.
"""

from Cuenta import Cuenta

class Menu:
    def __init__(self, mensaje):
        self.mensajeDeBienvenida = mensaje
        self.cargaDatos()

    def cargaDatos(self):
        # Se crea una cuenta inicial
        self.cuenta = Cuenta(300, "Débito")

    def darBienvenida(self):
        print(self.mensajeDeBienvenida)

    def despliegaMenu(self):
        print("\n=== Menú de opciones ===")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Mostrar detalles")
        print("4. Salir")
        opcion = input("Teclea la opción: ")
        return opcion

    def procesaOpcion(self, opcion):
        if opcion == "1":
            print("\n--- Opción: Depositar ---")
            cantidad = float(input("Ingresa la cantidad a depositar: "))
            if self.cuenta.depositar(cantidad):
                print("El depósito se realizó con éxito.")
        elif opcion == "2":
            print("\n--- Opción: Retirar ---")
            cantidad = float(input("Ingresa la cantidad a retirar: "))
            if self.cuenta.retirar(cantidad):
                print("El retiro se realizó con éxito.")
        elif opcion == "3":
            print("\n--- Opción: Mostrar detalles ---")
            self.cuenta.imprimirDetalles()
        elif opcion == "4":
            print("Gracias por usar el Banco Pato. ¡Hasta pronto!")
        else:
            print("Opción inválida.")
