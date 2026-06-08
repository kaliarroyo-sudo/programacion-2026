''' 
Created on Junio,2026 
@author: kaliarroyo-sudo
'''

from Persistencia import Persistencia

# Cargar estudiantes desde archivo CSV
estudiantes = Persistencia.cargar_estudiantes()

print(" Estudiantes cargados desde data/datosEstudiantes.csv:\n")
for e in estudiantes:
    print(e.mostrar())

# Guardar nuevamente (ejemplo de persistencia)
Persistencia.guardar_estudiantes(estudiantes)
print("\n Archivo actualizado en directorio data/")
