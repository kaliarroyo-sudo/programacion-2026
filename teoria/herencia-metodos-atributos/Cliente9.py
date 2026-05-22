"""
Clase Cliente:
Representa un cliente que contiene una Cuenta (madre o hija).
"""

class Cliente:
    def __init__(self, nombre, direccion, edad, cuenta):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.cuenta = cuenta

    def mostrarDetalles(self):
        print("Nombre:", self.nombre)
        print("Dirección:", self.direccion)
        print("Edad:", self.edad)
        self.cuenta.mostrarDetalles()

    def __str__(self):
        return (
            f"Cliente: {self.nombre}\n"
            f"Dirección: {self.direccion}\n"
            f"Edad: {self.edad}\n"
            f"{self.cuenta}"
        )
