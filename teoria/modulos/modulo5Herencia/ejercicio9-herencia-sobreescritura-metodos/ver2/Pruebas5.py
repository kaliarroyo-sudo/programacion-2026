"""
Archivo de Pruebas:
Demuestra herencia y sobreescritura de métodos.
"""

from Cuenta import Cuenta
from CuentaHija import CuentaHija
from Cliente import Cliente

class Pruebas:
    pass

print("\n********* Clase Madre *********")
cuenta1 = Cuenta(300)
print(cuenta1)
cuenta1.depositar(400)
print(cuenta1)

print("\n********* Clase Hija *********")
cuenta2 = CuentaHija(200, "Débito")
print(cuenta2)
cuenta2.depositar(8000)
print(cuenta2)

print("\n********* Clase Cliente *********")
cliente = Cliente("Virginia", "Calle Falsa 123", 25, cuenta1)
print(cliente)
