"""
Archivo de Pruebas:
Demuestra objetos persistentes en la Biblioteca Digital.
"""

from GestorUsuarios import GestorUsuarios

gestor = GestorUsuarios("data/usuarios.csv")
gestor.mostrarTabla()
gestor.graficarLibrosPrestados()
