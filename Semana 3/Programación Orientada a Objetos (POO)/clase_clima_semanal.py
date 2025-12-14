# ClaseClimaSemanal.py
# HERENCIA y POLIMORFISMO

from clase_clima import Clima

class ClimaSemanal(Clima):
    """
    Clase que hereda de Clima y gestiona temperaturas semanales.
    """

    def __init__(self):
        super().__init__()
        self.dias = [
            "Lunes", "Martes", "Miércoles",
            "Jueves", "Viernes", "Sábado", "Domingo"
        ]

    def ingresar_datos(self):
        for dia in self.dias:
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.ingresar_temperatura(dia, temp)