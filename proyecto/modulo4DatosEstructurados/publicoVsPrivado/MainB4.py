"""
Archivo Principal:
Demuestra atributos públicos vs privados en la Biblioteca Digital.
"""

from Libro import Libro
from Usuario import Usuario

class Main:
    pass

print("=== Pruebas público vs privado ===")

# Crear libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro1.mostrarDetalles()
libro1.prestar()
libro1.mostrarDetalles()

print("\n--- Intento de imprimir objeto ---")
print("va::", libro1)

"""
Si los atributos fueran PÚBLICOS:
podríamos acceder directamente y modificar sin control.
Esto genera errores semánticos.
"""
# Ejemplo (comentado porque no existe):
# print("Título directo:", libro1.titulo)

"""
Con los atributos PRIVADOS (__titulo, __autor, __disponible):
el acceso directo genera error y protege la información.
"""
try:
    print("Intentamos acceder directamente:", libro1.__titulo)
except AttributeError as e:
    print("Error al acceder directamente:", e)

# Relación Usuario-Libro
usuario1 = Usuario("Virginia", "Calle Falsa 123", 25, libro1)
print("\n--- Usuario con libro asociado ---")
usuario1.mostrarDetalles()
