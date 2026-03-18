class Main:
    pass  # Clase vacía, punto de entrada del programa

# === Algoritmo principal ===
print("=== Algoritmo principal ===")

# Crear un libro (clase base)
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")

# Crear un cliente con ese libro (clase compuesta)
cliente1 = Cliente("Virginia", "Calle Falsa 123", 25, libro1)

# Pruebas con __str__
print("\n=== Pruebas con __str__ ===")
print(libro1)     # Muestra el libro en formato legible
print(cliente1)   # Muestra el cliente en formato legible

# Pruebas con métodos
print("\n=== Pruebas con métodos ===")
libro1.prestar()
libro1.devolver()

print("\n=== Detalles completos del cliente ===")
cliente1.mostrarDetalles()
