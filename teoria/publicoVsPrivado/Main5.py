"""
Created on Mar, 2026
@author: lunysska

Archivo principal (Main):
Se realizan pruebas de atributos públicos vs privados.
"""

from Cuenta import Cuenta
from Cliente import Cliente

class Main:
    pass  # Clase vacía, punto de entrada

print("=== Pruebas de público vs privado ===")

# Crear una cuenta
cuenta1 = Cuenta(300)

# Usar métodos públicos
cuenta1.mostrarDetalles()
cuenta1.depositar(400)
cuenta1.mostrarDetalles()

# Intento de acceder directamente al atributo privado (esto dará error)
print("\nIntentamos acceder directamente al atributo privado:")
try:
    print("El valor de la cuenta es:", cuenta1.__cantidad)
except AttributeError as e:
    print("Error:", e)

# Crear un cliente asociado a la cuenta
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25, cuenta1)
cliente1.mostrarDetalles()
