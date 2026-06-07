"""
Created on Marzo, 2026
@author: kaliarroyo-sudo

Clase Menu:
Controla las opciones de interacción con los libros.
"""

from Libro import Libro

class Menu:
    def __init__(self, mensaje):
        self.mensajeDeBienvenida = mensaje
        self.cargaDatos()

    def cargaDatos(self):
        # Se crea un libro inicial
        self.libro = Libro("Cien años de soledad", "Gabriel García Márquez")

    def darBienvenida(self):
        print(self.mensajeDeBienvenida)

    def despliegaMenu(self):
        print("\n=== Menú de opciones ===")
        print("1. Prestar libro")
        print("2. Devolver libro")
        print("3. Mostrar detalles")
        print("4. Salir")
        opcion = input("Teclea la opción: ")
        return opcion

    def procesaOpcion(self, opcion):
        if opcion == "1":
            print("\n--- Opción: Prestar libro ---")
            if self.libro.prestar():
                print("El préstamo se realizó con éxito.")
            else:
                print("El libro no está disponible.")
        elif opcion == "2":
            print("\n--- Opción: Devolver libro ---")
            self.libro.devolver()
            print("El libro ha sido devuelto.")
        elif opcion == "3":
            print("\n--- Opción: Mostrar detalles ---")
            print(self.libro)
        elif opcion == "4":
            print("Gracias por usar la Biblioteca Digital.")
        else:
            print("Opción inválida.")
