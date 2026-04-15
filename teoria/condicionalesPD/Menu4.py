"""
Created on March, 2026
@author: kaliarroyo-sudo

Clase Menu:
Controla la interacción con el usuario y ejecuta operaciones sobre la cuenta.
"""

from Cuenta import Cuenta

class Menu:
    def __init__(self, mensaje):
        """
        Constructor de la clase Menu.
        Parámetros:
            mensaje (str): mensaje de bienvenida
        """
        self.mensajeDeBienvenida = mensaje
        self.cargaDatos()

    def cargaDatos(self):
        """
        Inicializa una cuenta de prueba.
        """
        self.cuenta = Cuenta(300, "Débito")

    def darBienvenida(self):
        """
        Muestra el mensaje de bienvenida.
        """
        print(self.mensajeDeBienvenida)

    def despliegaMenu(self):
        """
        Muestra las opciones disponibles y pide al usuario una elección.
        """
        print("\n=== Menú de opciones ===")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Consultar detalles")
        print("4. Salir")
        opcion = input("Teclea la opción: ")
        return opcion

    def procesaOpcion(self, opcion):
        """
        Procesa la opción elegida y ejecuta el método correspondiente.
        """
        if opcion == "1":
            print("\n--- Opción: Depositar ---")
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            if self.cuenta.depositar(cantidad):
                print("Depósito realizado con éxito.")
        elif opcion == "2":
            print("\n--- Opción: Retirar ---")
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            if self.cuenta.retirar(cantidad):
                print("Retiro realizado con éxito.")
        elif opcion == "3":
            print("\n--- Opción: Consultar detalles ---")
            self.cuenta.imprimirDetalles()
        elif opcion == "4":
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
        else:
            print("\nOpción inválida. Intente de nuevo.")
