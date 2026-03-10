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
