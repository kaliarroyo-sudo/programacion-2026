"""
Archivo principal (Main):
Demuestra herencia, métodos y atributos en la Biblioteca Digital.
"""

from LibroFisico import LibroFisico
from LibroDigital import LibroDigital
from Cliente import Cliente

class Main:
    pass

print("=== Pruebas de herencia en la Biblioteca Digital ===")

# Cliente con libro físico
libro_fisico = LibroFisico("Cien años de soledad", "Gabriel García Márquez", "A3")
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25, libro_fisico)
print("\n--- Cliente con libro físico ---")
print(cliente1)
libro_fisico.mostrarUbicacion()

# Cliente con libro digital
libro_digital = LibroDigital("Don Quijote de la Mancha", "Miguel de Cervantes", "http://biblioteca.com/quijote")
cliente2 = Cliente("Marco", "Av. Reforma 456", 40, libro_digital)
print("\n--- Cliente con libro digital ---")
print(cliente2)
libro_digital.mostrarAcceso()
