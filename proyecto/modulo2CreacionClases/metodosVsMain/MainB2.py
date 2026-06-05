"""
Created on Febrero, 2026
@author: kaliarroyo-sudo

Archivo principal (Main):
Demuestra la diferencia entre imprimir atributos directamente
y usar un método de la clase.
"""

from Libro import Libro

class Main:
    pass

print("*** 1. Imprimimos atributos desde el archivo principal (main) ***")

# Crear objeto de la clase Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")

# Acceso directo con operador punto
print("Título:", libro1.titulo)
print("Autor:", libro1.autor)

print("\n*** 2. Imprimimos atributos usando el método de la clase ***")
libro1.imprimirDetalles()
