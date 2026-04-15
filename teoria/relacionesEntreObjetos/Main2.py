"""
Created on March, 2026
@author: kaliarroyo-sudo

Archivo principal (Main):
Se realizan pruebas de la relación entre objetos Cliente y Cuenta.
"""

from Cuenta import Cuenta
from Cliente import Cliente

class Main:
    pass  # Clase vacía, punto de entrada

print("=== Pruebas de relación entre objetos ===")

# Crear una cuenta
cuenta1 = Cuenta(300)

# Mostrar detalles iniciales
cuenta1.mostrarDetalles()

# Operaciones sobre la cuenta
cuenta1.depositar(400)
cuenta1.mostrarDetalles()

# Crear un cliente asociado a la cuenta
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25, cuenta1)

# Mostrar detalles del cliente y su cuenta
cliente1.mostrarDetalles()
