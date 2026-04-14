"""
Created on Feb, 2026
@author: kaliarroyo-sudo

Archivo principal (Main):
Aquí se realizan las pruebas de la clase Cuenta.
Se demuestra el uso del operador punto para acceder
a atributos y métodos de un objeto.
"""

from Cuenta import Cuenta

class Main:
    pass  # Clase vacía, punto de entrada del programa

# === Pruebas con operador punto ===
print("*** 1. Acceso directo a atributos desde el archivo principal")

# Crear un objeto de la clase Cuenta
# Nota: el constructor recibe dos argumentos: cantidad y tipo
cuenta1 = Cuenta(300, "Débito")

# Acceder a los atributos directamente con el operador punto
print("Saldo inicial:", cuenta1.cantidad)   # atributo cantidad
print("Tipo de cuenta:", cuenta1.tipo)      # atributo tipo

# === Pruebas con método imprimirDetalles ===
print("\n*** 2. Acceso a atributos mediante un método de la clase")
cuenta1.imprimirDetalles()
