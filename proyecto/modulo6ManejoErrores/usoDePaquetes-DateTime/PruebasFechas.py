"""
Archivo de Pruebas:
Demuestra manejo de errores y uso de paquetes con datetime.
"""

from Fecha import Fecha

print("\n=== Pruebas de fechas ===")

# Fecha válida
fecha1 = Fecha("23/12/2020")
print(fecha1)
fecha1.mostrarFecha()

# Fecha inválida (año 0000 no existe en datetime)
fecha2 = Fecha("23/12/0000")
print(fecha2)
fecha2.mostrarFecha()

# Fecha inválida (formato incorrecto)
fecha3 = Fecha("2020-12-23")
print(fecha3)
fecha3.mostrarFecha()
