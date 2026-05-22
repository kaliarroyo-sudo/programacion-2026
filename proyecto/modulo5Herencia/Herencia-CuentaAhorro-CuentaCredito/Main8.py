"""
Archivo principal (Main):
Demuestra los riesgos de atributos públicos vs privados.
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
# print("El valor de la cuenta es::", cuenta1.cantidad)   # <- público, peligroso

"""
Con el atributo PRIVADO (__cantidad):
el acceso directo genera error y protege la información.
"""
try:
    print("El valor de la cuenta es::", cuenta1.__cantidad)
except AttributeError as e:
    print("Error al acceder directamente:", e)

# Relación Cliente-Cuenta
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25, cuenta1)
cliente1.mostrarDetalles()
