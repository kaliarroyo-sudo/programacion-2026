"""
Archivo principal (Main):
Demuestra el uso de herencia en cuentas bancarias.
"""

from CuentaAhorro import CuentaAhorro
from CuentaCredito import CuentaCredito
from Cliente import Cliente

class Main:
    pass

print("=== Pruebas de herencia en cuentas bancarias ===")

# Cliente con cuenta de ahorro
cuenta_ahorro = CuentaAhorro(1000, 0.05)
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25, cuenta_ahorro)
print("\n--- Cliente con cuenta de ahorro ---")
print(cliente1)
cuenta_ahorro.aplicarInteres()

# Cliente con cuenta de crédito
cuenta_credito = CuentaCredito(500, 1000)
cliente2 = Cliente("Marco", "Av. Reforma 456", 40, cuenta_credito)
print("\n--- Cliente con cuenta de crédito ---")
print(cliente2)
cuenta_credito.retirar(1200)  # usa el sobregiro
print(cliente2)
