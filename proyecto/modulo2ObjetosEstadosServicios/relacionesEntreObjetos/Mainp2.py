"""
Archivo principal (Main):
Demuestra las relaciones entre objetos en la Biblioteca Digital.
"""

from Libro import Libro
from Cliente import Cliente
from Biblioteca import Biblioteca

class Main:
    pass

print("=== Relaciones entre objetos en la Biblioteca Digital ===")

# Crear biblioteca
biblioteca = Biblioteca("Biblioteca Central")

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")

# Agregar libros a la biblioteca
biblioteca.agregarLibro(libro1)
biblioteca.agregarLibro(libro2)

# Crear cliente
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25)

# Registrar cliente en la biblioteca
biblioteca.registrarCliente(cliente1)

# Cliente presta un libro
cliente1.prestarLibro(libro1)

# Mostrar inventario y clientes
biblioteca.mostrarInventario()
biblioteca.mostrarClientes()

# Mostrar detalles del cliente
cliente1.mostrarDetalles()
