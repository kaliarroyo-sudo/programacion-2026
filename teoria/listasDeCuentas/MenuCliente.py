"""
Created on Abril, 2026
@author: kaliarroyo-sudo

Clase MenuCliente:
Controla la interacción con el usuario para gestionar cuentas de un cliente.
"""

from Cuenta import Cuenta
from Cliente import Cliente

class MenuCliente:
    def __init__(self):
        """
        Constructor de la clase MenuCliente.
        Inicializa un cliente de prueba.
        """
        self.__bienvenida = "Menú del Usuario"
        self.__cliente = Cliente(
            "Marco",
            "Calle de Arboledas No. 45, Col. Granjas México, CDMX",
            38
        )

    def menuCuentas(self):
        """
        Muestra el menú de opciones para gestionar cuentas.
        """
        print("\n*********** Menú Cuenta ***********")
        print("1. Agregar una Cuenta")
        print("2. Eliminar una Cuenta")
        print("3. Mostrar todas las Cuentas")
        print("4. Salir")

        opcion = input("Teclee la opción deseada: ")
        print("Elegiste:", opcion)

        if opcion == "1":
            self.__agregarCuenta()
        elif opcion == "2":
            indice = int(input("Ingrese el índice de la cuenta a eliminar: ")) - 1
            self.__cliente.eliminarCuenta(indice)
        elif opcion == "3":
            self.__cliente.infoCuentas()
        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
        else:
            print("Esa opción no existe.")

    def __agregarCuenta(self):
        """
        Método privado para agregar una nueva cuenta al cliente.
        """
        print("\nEligió la opción: Agregar una Cuenta")
        saldoInicial = float(input("Ingrese el saldo inicial: "))
        cuenta = Cuenta(saldoInicial)
        self.__cliente.agregarCuenta(cuenta)
        print("La cuenta se agregó con éxito.")
        self.__cliente.infoCuentas()
