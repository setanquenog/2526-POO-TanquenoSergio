# ClaseAplicacionClima.py
# CLASE PRINCIPAL EJECUTA EL PROGRAMA

from clase_clima_semanal import ClimaSemanal

class AplicacionClima:
    """
    Clase que controla la ejecución del programa.
    """

    def ejecutar(self):
        print("=== Registro de Temperaturas Semanales (POO) ===")

        clima = ClimaSemanal()
        clima.ingresar_datos()

        promedio = clima.calcular_promedio()
        print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")


# Punto de inicio del programa
if __name__ == "__main__":
    app = AplicacionClima()
    app.ejecutar()