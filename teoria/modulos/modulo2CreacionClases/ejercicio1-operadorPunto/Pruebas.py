"""
Created on Agosto, 2026
@author: kaliarroyo-sudo

Archivo de pruebas:
Demuestra el uso del operador punto para acceder a atributos.
"""

from Cuenta import Cuenta

class Pruebas:
    pass

print("=== Desde las pruebas ===")

# Crear un objeto de la clase Cuenta
cuenta1 = Cuenta(300)

# Acceder al atributo con el operador punto
print("Saldo inicial:", cuenta1.cantidad)
