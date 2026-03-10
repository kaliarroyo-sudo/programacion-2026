from Libro import Libro
from Menu import Menu

class Main:
    pass  # Clase vacía, como pide el ejercicio

# === Algoritmo principal ===
print("=== Algoritmo principal ===")

# 1. Crear un objeto de la clase Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")

# 2. Crear un objeto de la clase Menu
menu = Menu()

# 3. Dar bienvenida al usuario
menu.darBienvenida()

# 4. Ciclo para ejecutar el menú hasta que el usuario decida salir
opcion = ""
while opcion != "4":
    opcion = menu.despliegaMenu()
    menu.procesaOpcion(opcion, libro1)
