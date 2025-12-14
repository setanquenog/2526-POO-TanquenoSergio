# ClaseClima.py
# ABSTRACCIÓN y ENCAPSULAMIENTO

class Clima:
    """
    Clase que representa información general del clima.
    """

    def __init__(self):
        self._temperaturas = []

    def ingresar_temperatura(self, dia, valor):
        self._temperaturas.append((dia, valor))

    def calcular_promedio(self):
        suma = sum(temp for _, temp in self._temperaturas)
        return suma / len(self._temperaturas)