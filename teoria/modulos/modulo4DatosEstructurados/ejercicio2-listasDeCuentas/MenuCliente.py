"""
Created on March, 2026
@author: kaliarroyo-sudo

Clase MenuCliente:
Permite gestionar las cuentas de un cliente mediante un menú.
"""

from Cuenta import Cuenta
from Cliente import Cliente

class MenuCliente:
    def __init__(self):
        self.__bienvenida = "Menú del Usuario"
        self.__cliente = Cliente("Marco", "Calle de Arboledas No. 45, Col. Granjas México. CDMX", 38)

    def menuCuentas(self):
        print("\n*********** Menú de Cuentas ***********")
        print("1. Agregar una Cuenta")
        print("2. Eliminar una Cuenta")
        print("3. Mostrar Cuentas")
        print("4. Salir")

        opcion = input("Teclee la opción deseada: ")
        print("Elegiste:", opcion)

        if opcion == "1":
            self.__agregarCuenta()
        elif opcion == "2":
            if self.__cliente._Cliente__cuentas:  # accedemos a la lista privada
                cuenta = self.__cliente._Cliente__cuentas[0]
                self.__cliente.eliminarCuenta(cuenta)
                print("Cuenta eliminada.")
            else:
                print("No hay cuentas para eliminar.")
        elif opcion == "3":
            self.__cliente.infoCuentas()
        elif opcion == "4":
            print("Gracias por usar el sistema.")
        else:
            print("Opción inválida.")

    def __agregarCuenta(self):
        print("\n--- Agregar una Cuenta ---")
        saldoInicial = float(input("Ingrese el saldo inicial: "))
        cuenta = Cuenta(saldoInicial)
        self.__cliente.agregarCuenta(cuenta)
        print("La cuenta se agregó con éxito.")
        self.__cliente.infoCuentas()
