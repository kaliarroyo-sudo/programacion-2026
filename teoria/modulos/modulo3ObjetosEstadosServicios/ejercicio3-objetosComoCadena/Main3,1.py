"""
Created on September, 2026
@author: kaliarroyo-sudo

Archivo principal (Main):
Demuestra cómo los objetos se imprimen como cadenas con __str__.
"""

from Cuenta import Cuenta
from Cliente import Cliente

class Main:
    pass

print("=== Pruebas de objetos como cadenas ===")

# Crear cuenta
cuenta1 = Cuenta(300)
print("\n--- Cuenta inicial ---")
print(cuenta1)   # usa __str__

cuenta1.depositar(400)
print("\n--- Cuenta después de depósito ---")
print(cuenta1)

# Crear cliente con esa cuenta
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25, cuenta1)
print("\n--- Cliente con cuenta asociada ---")
print(cliente1)
