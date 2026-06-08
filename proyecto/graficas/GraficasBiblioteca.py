"""
Temas extras del curso de Progra:
Gráficas de barras y nube de palabras adaptadas a la Biblioteca Digital.
kaliarroyo-sudo
@author: kaliarroyo-sudo
"""

from Usuario import Usuario
import csv
import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDS   # opcional para nube de palabras

# Listas para graficar
listaUsuarios = []
listaLibros = []

with open('data/usuarios.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)  # quitar encabezados

    for row in csv_reader:
        nombre, apellido, direccion, edad, librosPrestados, *_ = row
        listaUsuarios.append(nombre)  # eje X
        listaLibros.append(int(librosPrestados))  # eje Y
        usuarioTemp = Usuario(nombre, apellido, direccion, edad, librosPrestados)
        print("El objeto:", usuarioTemp)

# Gráfica de barras
plt.bar(listaUsuarios, listaLibros, color='b')
plt.title("Libros prestados por usuario")
plt.xlabel("Usuarios")
plt.ylabel("Cantidad de libros prestados")
plt.show()
