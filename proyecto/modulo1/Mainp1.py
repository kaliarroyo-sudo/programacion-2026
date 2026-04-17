"""
Created on Feb, 2026
@author: kaliarroyo-sudo

Archivo principal (Main):
Se realizan pruebas de la relación entre objetos Cliente y Libro.
Se demuestra el uso del operador punto y la diferencia entre métodos y main.
"""

from Libro import Libro
from Cliente import Cliente

class Main:
    pass  # Clase vacía, punto de entrada

print("=== Pruebas con operador punto y métodos vs main ===")

# Crear objetos de la clase Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")

# Crear objeto Cliente
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25)

# --- Uso del operador punto en el MAIN ---
print("\n*** 1. Acceso directo a atributos con operador punto ***")
print("Título del libro:", libro1.titulo)   # operador punto sobre atributo
print("Autor del libro:", libro1.autor)

# --- Uso de métodos con operador punto ---
print("\n*** 2. Uso de métodos con operador punto ***")
libro1.prestar()        # operador punto sobre método
libro1.devolver()

# --- Relación entre objetos ---
print("\n*** 3. Relación Cliente-Libro ***")
cliente1.agregarLibro(libro1)
cliente1.agregarLibro(libro2)

# Mostrar detalles del cliente (usa método)
cliente1.mostrarDetalles()

# Usar __str__ para imprimir objetos
print("\n*** 4. Representación en cadena (__str__) ***")
print(cliente1)
