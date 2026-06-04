"""
Archivo principal (Main):
Demuestra el uso de atributos públicos vs privados.
"""

from Cuenta import Cuenta
from Cliente import Cliente

class Main:
    pass

print("=== Pruebas público vs privado ===")

# Crear cuenta
cuenta1 = Cuenta(300)
cuenta1.mostrarDetalles()
cuenta1.depositar(400)
cuenta1.mostrarDetalles()

print("\n--- Intento de imprimir objeto ---")
print("va::", cuenta1)

"""
Si el atributo cantidad fuera PÚBLICO:
podríamos acceder directamente y modificarlo sin control.
Esto genera errores semánticos.
"""
# Ejemplo (comentado porque no existe):
# print("Saldo directo:", cuenta1.cantidad)

"""
Con el atributo PRIVADO (__cantidad):
el acceso directo genera error y protege la información.
"""
try:
    print("Intentamos acceder directamente:", cuenta1.__cantidad)
except AttributeError as e:
    print("Error al acceder directamente:", e)

# Relación Cliente-Cuenta
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25, cuenta1)
print("\n--- Cliente con cuenta asociada ---")
cliente1.mostrarDetalles()
