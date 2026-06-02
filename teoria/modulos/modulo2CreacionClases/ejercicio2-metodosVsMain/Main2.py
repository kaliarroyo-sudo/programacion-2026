"""
Created on Febrero, 2026
@author: kaliarroyo-sudo

Archivo principal (Main):
Demuestra la diferencia entre imprimir atributos directamente
y usar un método de la clase.
"""

from Cuenta import Cuenta

class Main:
    pass

print("*** 1. Imprimimos atributos desde el archivo principal (main) ***")

# Crear objeto de la clase Cuenta
cuenta1 = Cuenta(300, "Débito")

# Acceso directo con operador punto
print("Cantidad:", cuenta1.cantidad)
print("Tipo:", cuenta1.tipo)

print("\n*** 2. Imprimimos atributos usando el método de la clase ***")
cuenta1.imprimirDetalles()
