"""
Archivo principal (Main):
Demuestra herencia, métodos y atributos en cuentas bancarias.
"""

from CuentaHija import CuentaHija
from Cliente import Cliente

class Main:
    pass

print("=== Pruebas de herencia, métodos y atributos ===")

# Crear cuenta hija
cuenta_hija = CuentaHija(500, "Ahorro")
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25, cuenta_hija)

# Mostrar detalles del cliente y su cuenta
print("\n--- Cliente con cuenta hija ---")
print(cliente1)

# Usar métodos heredados y propios
cuenta_hija.depositar(200)   # método heredado
cuenta_hija.mostrarTipo()    # método propio de la hija
print(cuenta_hija)
