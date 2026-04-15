"""
Created on March, 2026
@author: kaliarroyo-sudo

Ejemplo de integración:
Se demuestra cómo una clase base (Cuenta) y una clase compuesta (Menu)
trabajan juntas en el archivo principal.
"""

# === Clase base: Cuenta ===
class Cuenta:
    def __init__(self, cantidad, tipo):
        """
        Constructor de la clase Cuenta.
        Parámetros:
            cantidad (float): saldo inicial
            tipo (str): tipo de cuenta (ej. 'Débito', 'Crédito')
        """
        self.cantidad = cantidad
        self.tipo = tipo

    def depositar(self, monto):
        """Método para depositar dinero en la cuenta."""
        if monto > 0:
            self.cantidad += monto
            print(f"Se depositaron {monto}. Nuevo saldo: {self.cantidad}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        """Método para retirar dinero de la cuenta."""
        if monto <= self.cantidad:
            self.cantidad -= monto
            print(f"Se retiraron {monto}. Nuevo saldo: {self.cantidad}")
        else:
            print("Fondos insuficientes.")

    def imprimirDetalles(self):
        """Imprime los detalles de la cuenta."""
        print("=== Detalles de la cuenta ===")
        print("Saldo actual:", self.cantidad)
        print("Tipo de cuenta:", self.tipo)


# === Clase compuesta: Menu ===
class Menu:
    def __init__(self, mensaje):
        """
        Constructor de la clase Menu.
        Parámetros:
            mensaje (str): mensaje de bienvenida
        """
        self.mensajeDeBienvenida = mensaje

    def darBienvenida(self):
        """Imprime el mensaje de bienvenida."""
        print(self.mensajeDeBienvenida)

    def despliegaMenu(self):
        """Muestra las opciones disponibles y pide al usuario una elección."""
        print("\n=== Menú de opciones ===")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Consultar detalles")
        print("4. Salir")
        opcion = input("Teclea