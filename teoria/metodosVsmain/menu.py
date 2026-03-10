# Clase Cuenta
class Cuenta:
    def __init__(self, cantidad, tipo, titular):
        self.cantidad = cantidad
        self.tipo = tipo
        self.titular = titular

    def imprimirDetalles(self):
        print("=== Detalles de la cuenta ===")
        print("Titular:", self.titular)
        print("Tipo:", self.tipo)
        print("Saldo:", self.cantidad)

    def retirar(self, monto):
        if monto <= self.cantidad:
            self.cantidad -= monto
            print(f"Se retiraron {monto}. Nuevo saldo: {self.cantidad}")
        else:
            print("Fondos insuficientes.")

    def depositar(self, monto):
        self.cantidad += monto
        print(f"Se depositaron {monto}. Nuevo saldo: {self.cantidad}")


# Clase Menu
class Menu:
    def __init__(self):
        self.mensajeDeBienvenida = "Bienvenido al Banco Digital"

    def darBienvenida(self):
        print(self.mensajeDeBienvenida)

    def despliegaMenu(self):
        print("\n=== Menú de opciones ===")
        print("1. Consultar detalles de la cuenta")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        return opcion

    def procesaOpcion(self, opcion, cuenta):
        if opcion == "1":
            cuenta.imprimirDetalles()
        elif opcion == "2":
            monto = float(input("Ingrese monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == "3":
            monto = float(input("Ingrese monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == "4":
            print("Gracias por usar el Banco Digital. ¡Hasta pronto!")
        else:
            print("Opción inválida.")


# Clase Main (vacía)
class Main:
    pass

# === Algoritmo principal ===
print("=== Algoritmo principal ===")

cuenta1 = Cuenta(1000, "Débito", "Maria Hernandez")
menu = Menu()
menu.darBienvenida()

opcion = ""
while opcion != "4":
    opcion = menu.despliegaMenu()
    menu.procesaOpcion(opcion, cuenta1)
