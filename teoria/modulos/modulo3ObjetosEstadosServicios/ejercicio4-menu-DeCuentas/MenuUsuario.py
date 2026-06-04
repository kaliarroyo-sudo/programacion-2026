"""
Clase MenuUsuario:
Permite gestionar cuentas de un cliente mediante un menú.
"""

from Cliente import Cliente
from CuentaAhorro import CuentaAhorro
from CuentaCredito import CuentaCredito

class MenuUsuario:
    def __init__(self):
        self.bienvenida = "Menú del Usuario"

    def menuCuenta(self):
        cte = Cliente("Virginia", "Calle Falsa 123", 32)

        print("\n=== Menú de Cuentas ===")
        print("1. Agregar una Cuenta")
        print("2. Eliminar una Cuenta")
        print("3. Mostrar Cuentas")
        print("4. Salir")

        opcion = input("Teclee la opción deseada: ")

        if opcion == "1":
            self.agregarCuenta(cte)
        elif opcion == "2":
            if cte.cuentas:
                cte.eliminarCuenta(cte.cuentas[0])  # ejemplo simple
                print("Cuenta eliminada.")
            else:
                print("No hay cuentas para eliminar.")
        elif opcion == "3":
            cte.infoCuentas()
        elif opcion == "4":
            print("Gracias por usar el sistema.")
        else:
            print("Opción inválida.")

    def agregarCuenta(self, cte):
        print("\n--- Tipos de Cuenta ---")
        print("1. Cuenta de Ahorro")
        print("2. Cuenta de Crédito")
        opcion = input("Elija el tipo de cuenta: ")

        if opcion == "1":
            cta = CuentaAhorro(2000, 0.05)
            cte.agregarCuenta(cta)
            print("Cuenta de Ahorro agregada.")
        elif opcion == "2":
            cta = CuentaCredito(1000, 500)
            cte.agregarCuenta(cta)
            print("Cuenta de Crédito agregada.")
        else:
            print("Opción inválida.")
