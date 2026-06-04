"""
Archivo de Pruebas:
Demuestra el uso de cuentas y clientes.
"""

from Cuenta import Cuenta
from CuentaAhorro import CuentaAhorro
from CuentaCredito import CuentaCredito
from Cliente import Cliente

class Pruebas:
    pass

print("\n--- Objeto Cuenta ---")
cuenta1 = Cuenta(300)
print(cuenta1)
cuenta1.depositar(400)
print(cuenta1)

print("\n--- Cuenta de Ahorro ---")
cuenta2 = CuentaAhorro(200, 0.2)
print(cuenta2)
cuenta2.depositar(8000)
print(cuenta2)

print("\n--- Cuenta de Crédito ---")
cuenta3 = CuentaCredito(200, 100)
print(cuenta3)
cuenta3.depositar(8000)
print(cuenta3)
cuenta3.retirar(8250)
print(cuenta3)
cuenta3.retirar(150)
print(cuenta3)

print("\n--- Cliente sin cuentas ---")
cliente1 = Cliente("Alejandro", "Calle Flores No.25", 56)
print(cliente1)
cliente1.infoCuentas()

print("\n--- Agregando cuentas ---")
cliente1.agregarCuenta(cuenta1)
cliente1.agregarCuenta(cuenta2)
cliente1.agregarCuenta(cuenta3)
cliente1.infoCuentas()

print("\n--- Eliminando cuentas ---")
cliente1.eliminarCuenta(cuenta1)
cliente1.infoCuentas()
