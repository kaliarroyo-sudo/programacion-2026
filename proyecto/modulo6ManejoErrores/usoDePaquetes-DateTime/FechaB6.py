"""
2026
@author: kaliarroyo-sudo

Clase Fecha:
Ejemplo de uso de paquetes (datetime) y manejo de errores.
"""

from datetime import datetime

class Fecha:
    def __init__(self, fecha_str):
        # validamos la fecha al crear el objeto
        if self.__validarFecha(fecha_str):
            self.__fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
        else:
            self.__fecha = None

    def __validarFecha(self, fecha_str):
        """
        Método privado para validar que la fecha sea correcta.
        Maneja excepciones con try/except.
        """
        try:
            datetime.strptime(fecha_str, '%d/%m/%Y')
            return True
        except ValueError:
            print("Error: formato o valor de fecha inválido.")
            return False

    def mostrarFecha(self):
        """
        Muestra la fecha si fue creada correctamente.
        """
        if self.__fecha:
            print("Fecha válida:", self.__fecha.strftime('%d/%m/%Y'))
        else:
            print("No se pudo crear la fecha.")

    def __str__(self):
        if self.__fecha:
            return f"Objeto Fecha: {self.__fecha.strftime('%d/%m/%Y')}"
        else:
            return "Objeto Fecha inválido"
