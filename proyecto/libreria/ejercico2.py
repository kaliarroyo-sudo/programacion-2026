# === Clase Libro ===
class Libro:
    def __init__(self, titulo, autor, estado="Disponible"):
        self.titulo = titulo
        self.autor = autor
        self.estado = estado

    def imprimirDetalles(self):
        print("=== Detalles del libro ===")
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Estado:", self.estado)

    def prestar(self):
        if self.estado == "Disponible":
            self.estado = "Prestado"
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if self.estado == "Prestado":
            self.estado = "Disponible"
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")


# === Clase Menu ===
class Menu:
    def __init__(self):
        self.mensajeDeBienvenida = "Bienvenido a la Biblioteca Digital"

    def darBienvenida(self):
        print(self.mensajeDeBienvenida)

    def despliegaMenu(self):
        print("\n=== Menú de opciones ===")
        print("1. Consultar detalles del libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        return opcion

    def procesaOpcion(self, opcion, libro):
        if opcion == "1":
            libro.imprimirDetalles()
        elif opcion == "2":
            libro.prestar()
        elif opcion == "3":
            libro.devolver()
        elif opcion == "4":
            print("Gracias por usar la Biblioteca Digital. ¡Hasta pronto!")
        else:
            print("Opción inválida.")


# === Clase Main (vacía) ===
class Main:
    pass


# === Algoritmo principal ===
print("=== Algoritmo principal ===")

# 1. Crear dos objetos de la clase Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")

# 2. Crear un objeto de la clase Menu
menu = Menu()

# 3. Dar bienvenida al usuario
menu.darBienvenida()

# 4. Ciclo para ejecutar el menú con libro1
opcion = ""
while opcion != "4":
    opcion = menu.despliegaMenu()
    menu.procesaOpcion(opcion, libro1)

# 5. Mostrar que también podemos trabajar con el segundo libro
print("\n=== Probando con el segundo libro ===")
libro2.imprimirDetalles()
libro2.prestar()
libro2.devolver()
