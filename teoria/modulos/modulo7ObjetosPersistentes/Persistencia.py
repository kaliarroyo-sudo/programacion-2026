''' 
Created on Junio,2026 
@author: kaliarroyo-sudo
'''

import csv
from Estudiante import Estudiante

class Persistencia:
    @staticmethod
    def cargar_estudiantes():
        estudiantes = []
        with open('data/datosEstudiantes.csv') as file:
            csv_reader = csv.reader(file, delimiter=',')
            next(csv_reader)  # quitar encabezados
            for row in csv_reader:
                nombre, apellido, carrera, edad, noMateriasIns = row
                estudiante = Estudiante(nombre, apellido, carrera, edad, noMateriasIns)
                estudiantes.append(estudiante)
        return estudiantes

    @staticmethod
    def guardar_estudiantes(estudiantes):
        with open('data/datosEstudiantes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["nombre", "apellido", "carrera", "edad", "noMateriasIns"])
            for e in estudiantes:
                writer.writerow([e.nombre, e.apellido, e.carrera, e.edad, e.noMateriasIns])
