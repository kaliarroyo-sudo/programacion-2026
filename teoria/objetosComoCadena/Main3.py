"""
Created on Mar, 2026
@author: kaliarroyo-sudo

Archivo principal (Main):
Se realizan pruebas de la relación entre objetos Cliente y Cuenta.
Se demuestra el uso del método __str__ para imprimir objetos de manera legible.
"""

from Cuenta import Cuenta
from Cliente import Cliente

class Main:
    pass  # Clase vacía, punto de entrada

print("=== Pruebas de relación entre objetos ===")

# Crear una cuenta
cuenta1 = Cuenta(300)
print("\n*** Estado inicial de la cuenta ***")
print(cuenta1)

# Operaciones sobre la cuenta
cuenta1.depositar(400)
print("\n*** Estado después de depositar ***")
print(cuenta1)

# Crear un cliente asociado a la cuenta
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25, cuenta1)

# Imprimir el objeto cliente (usa __str__)
print("\n*** Estado del cliente y su cuenta ***")
print(cliente1)
