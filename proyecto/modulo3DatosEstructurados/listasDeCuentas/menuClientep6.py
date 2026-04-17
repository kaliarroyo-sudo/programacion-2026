"""
Clase MenuCliente:
Controla la interacción con el usuario para gestionar libros prestados.
"""

from Cliente import Cliente
from Libro import Libro

class MenuCliente:
    def __init__(self):
        self.__bienvenida = "Menú de la Biblioteca"
        self.__cliente = Cliente("Virginia", "Calle Falsa 123", 25)

    def menuLibros(self):
        print("\n*********** Menú Libros ***********")
        print("1. Prestar un Libro")
        print("2. Devolver un Libro")
        print("3. Mostrar Libros del Cliente")
        print("4. Salir")

        opcion = input("Teclee la opción deseada: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            libro = Libro(titulo, autor)
            self.__cliente.agregarLibro(libro)
        elif opcion == "2":
            indice = int(input("Ingrese el índice del libro a devolver: ")) - 1
            self.__cliente.devolverLibro(indice)
        elif opcion == "3":
            self.__cliente.infoLibros()
        elif opcion == "4":
            print("Gracias por usar la Biblioteca Digital. ¡Hasta pronto!")
        else:
            print("Opción inválida.")
        return opcion
