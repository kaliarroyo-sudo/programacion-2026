"""
GestorUsuarios:
Carga datos persistentes desde CSV y los muestra en tabla y gráficas.
"""

import csv
import pandas as pd
from Usuario import Usuario

class GestorUsuarios:
    def __init__(self, archivo_csv):
        self.usuarios = []
        self.archivo_csv = archivo_csv
        self.cargarDatos()

    def cargarDatos(self):
        with open(self.archivo_csv, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                usuario = Usuario(row['nombre'], row['apellido'], row['direccion'], row['edad'], row['librosPrestados'])
                self.usuarios.append(usuario)

    def mostrarTabla(self):
        df = pd.DataFrame([vars(u) for u in self.usuarios])
        print("\n=== Tabla de Usuarios de la Biblioteca ===")
        print(df)

    def graficarLibrosPrestados(self):
        df = pd.DataFrame([vars(u) for u in self.usuarios])
        df.plot(x="nombre", y="librosPrestados", kind="bar", title="Libros prestados por usuario")
