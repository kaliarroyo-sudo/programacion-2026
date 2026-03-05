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
