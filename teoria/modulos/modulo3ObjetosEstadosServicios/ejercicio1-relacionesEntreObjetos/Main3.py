"""
Created on Febrero, 2026
@author: lunysska

Archivo principal (Main):
Demuestra la relación entre Cliente y Cuenta.
"""

from Cuenta import Cuenta
from Cliente import Cliente

class Main:
    pass

print("=== Pruebas de relaciones entre objetos ===")

# Crear cuenta
cuenta1 = Cuenta(300)
cuenta1.mostrarDetalles()
cuenta1.depositar(400)
cuenta1.mostrarDetalles()

# Crear cliente con esa cuenta
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25, cuenta1)
print("\n--- Cliente con cuenta asociada ---")
cliente1.mostrarDetalles()

# Usar __str__ para imprimir directamente
print("\n--- Usando __str__ ---")
print(cliente1)
