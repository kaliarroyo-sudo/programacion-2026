"""
Clase MenuUsuario:
Permite gestionar libros de un usuario mediante un menú.
"""

from Usuario import Usuario
from LibroDigital import LibroDigital
from LibroFisico import LibroFisico

class MenuUsuario:
    def __init__(self):
        self.bienvenida = "Menú del Usuario"
        self.usuario = Usuario("Virginia", "Calle Falsa 123", 32)

    def menuLibros(self):
        print("\n*********** Menú de Libros ***********")
        print("1. Agregar un Libro")
        print("2. Eliminar un Libro")
        print("3. Mostrar Libros")
        print("4. Salir")

        opcion = input("Teclee la opción deseada: ")
        print("Elegiste:", opcion)

        if opcion == "1":
            self.__agregarLibro()
        elif opcion == "2":
            if self.usuario.libros:
                libro = self.usuario.libros[0]
                self.usuario.eliminarLibro(libro)
                print("Libro eliminado.")
            else:
                print("No hay libros para eliminar.")
        elif opcion == "3":
            self.usuario.infoLibros()
        elif opcion == "4":
            print("Gracias por usar la Biblioteca Digital.")
        else:
            print("Opción inválida.")

    def __agregarLibro(self):
        print("\n--- Tipos de Libro ---")
        print("1. Libro Digital")
        print("2. Libro Físico")
        opcion = input("Elija el tipo de libro: ")

        if opcion == "1":
            libro = LibroDigital("Cien años de soledad", "Gabriel García Márquez", "PDF")
            self.usuario.agregarLibro(libro)
            print("Libro Digital agregado.")
        elif opcion == "2":
            libro = LibroFisico("Pedro Páramo", "Juan Rulfo", "Estante A3")
            self.usuario.agregarLibro(libro)
            print("Libro Físico agregado.")
        else:
            print("Opción inválida.")
