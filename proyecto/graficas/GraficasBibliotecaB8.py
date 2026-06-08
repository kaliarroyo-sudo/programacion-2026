"""
Gráfica de la Biblioteca Digital
Visualiza la relación entre edad y libros prestados.
@author: kaliarroyo-sudo
@update: Junio, 2026
"""

from Usuario import Usuario
import csv
import matplotlib.pyplot as plt

# Listas para graficar
listaUsuarios = []
listaEdades = []
listaLibros = []

with open('data/usuarios.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)  # quitar encabezados

    for row in csv_reader:
        nombre, apellido, direccion, edad, librosPrestados, *_ = row
        listaUsuarios.append(nombre)
        listaEdades.append(int(edad))
        listaLibros.append(int(librosPrestados))
        usuarioTemp = Usuario(nombre, apellido, direccion, edad, librosPrestados)
        print("El objeto:", usuarioTemp)

# Gráfica de barras
plt.bar(listaUsuarios, listaLibros, color='royalblue')
plt.title("Libros prestados por usuario en la Biblioteca Digital")
plt.xlabel("Usuarios")
plt.ylabel("Cantidad de libros prestados")

# Guardar la gráfica como imagen dentro del proyecto
plt.savefig("data/grafica_biblioteca.png")

# Mostrar la gráfica localmente (opcional)
plt.show()
