"""
Clase MenuUsuario:
Permite gestionar la lista de libros de un usuario mediante un menú.
"""

from Usuario import Usuario
from Libro import Libro

class MenuUsuario:
    def __init__(self):
        self.__bienvenida = "Menú del Usuario"
        self.__usuario = Usuario("Marco", "Calle de Arboledas No. 45, CDMX", 38)

    def menuLibros(self):
        opciones = "\n*********** Menú de Libros ***********\n"
        opciones += "1. Agregar un Libro\n"
        opciones += "2. Eliminar un Libro\n"
        opciones += "3. Mostrar Libros\n"
        opciones += "4. Salir\n"

        print(opciones)
        opcion = input("Teclee la opción deseada: ")
        print("Elegiste:", opcion)

        if opcion == "1":
            self.__agregarLibro()
        elif opcion == "2":
            if self.__usuario._Usuario__libros:
                libro = self.__usuario._Usuario__libros[0]
                self.__usuario.eliminarLibro(libro)
                print("Libro eliminado.")
            else:
                print("No hay libros para eliminar.")
        elif opcion == "3":
            self.__usuario.infoLibros()
        elif opcion == "4":
            print("Gracias por usar la Biblioteca Digital.")
        else:
            print("Opción inválida.")

    def __agregarLibro(self):
        print("\n--- Agregar un Libro ---")
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        libro = Libro(titulo, autor)
        self.__usuario.agregarLibro(libro)
        print("El libro se agregó con éxito.")
        self.__usuario.infoLibros()
