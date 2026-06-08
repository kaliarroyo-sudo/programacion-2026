''' 
Created on Junio,2026 
@author: kaliarroyo-sudo
'''

class Estudiante:
    def __init__(self, nombre, apellido, carrera, edad, noMateriasIns):
        self.nombre = nombre
        self.apellido = apellido
        self.carrera = carrera
        self.edad = int(edad)
        self.noMateriasIns = int(noMateriasIns)

    def mostrar(self):
        return f"{self.nombre} {self.apellido} | {self.carrera} | Edad: {self.edad} | Materias: {self.noMateriasIns}"
