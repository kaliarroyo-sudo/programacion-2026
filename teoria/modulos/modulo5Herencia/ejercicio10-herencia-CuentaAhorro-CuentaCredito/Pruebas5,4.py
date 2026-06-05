"""
Archivo de Pruebas:
Demuestra herencia con CuentaAhorro y CuentaCredito.
"""

from Cuenta import Cuenta
from CuentaAhorro import CuentaAhorro
from CuentaCredito import CuentaCredito
from Cliente import Cliente

class Pruebas:
    pass

print("\n********* Cuenta base *********")
cuenta1 = Cuenta(300)
print(cuenta1)
cuenta1.depositar(400)
print(cuenta1)

print("\n********* Cuenta de Ahorro *********")
cuenta2 = CuentaAhorro(200, 0.2)
print(cuenta2)
cuenta2.depositar(8000)
cuenta2.aplicarInteres()
print(cuenta2)

print("\n********* Cuenta de Crédito *********")
cuenta3 = CuentaCredito(200, 100)
print(cuenta3)
cuenta3.depositar(8000)
print(cuenta3)
cuenta3.retirar(8250)  # usa sobregiro
print(cuenta3)
cuenta3.retirar(150)   # prueba de sobregiro insuficiente
print(cuenta3)

print("\n********* Cliente con cuenta *********")
cliente = Cliente("Virginia", "Calle Falsa 123", 25, cuenta2)
print(cliente)
