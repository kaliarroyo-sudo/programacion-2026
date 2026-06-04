"""
Clase Cliente:
Representa un cliente con múltiples cuentas.
"""

class Cliente:
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.cuentas = []

    def agregarCuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def eliminarCuenta(self, cuenta):
        if cuenta in self.cuentas:
            self.cuentas.remove(cuenta)

    def infoCuentas(self):
        print(f"--- Cantidad de cuentas: {len(self.cuentas)} ---")
        for cta in self.cuentas:
            print(cta)

    def __str__(self):
        return f"Cliente: {self.nombre}, {self.edad} años, Dirección: {self.direccion}"
