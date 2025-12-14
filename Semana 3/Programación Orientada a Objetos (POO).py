# ----------------------------------------------------
# Programa: Promedio semanal de temperaturas
# Lenguaje: Python
# Paradigma: Programación Orientada a Objetos (POO)
# ----------------------------------------------------

#### Clase base Clima (ABSTRACCIÓN) ####
class Clima:
    """
    Clase que representa información general del clima.
    Define la estructura común para registrar temperaturas.
    """

    def __init__(self):
        # ENCAPSULAMIENTO: atributo protegido
        self._temperaturas = []

    def ingresar_temperatura(self, dia, valor):
        """
        Método para ingresar la temperatura de un día específico.
        """
        self._temperaturas.append((dia, valor))

    def calcular_promedio(self):
        """
        Método para calcular el promedio de las temperaturas registradas.
        """
        suma = sum(temp for _, temp in self._temperaturas)
        return suma / len(self._temperaturas)


#### Clase derivada Clima Semanal (HERENCIA) ####
class ClimaSemanal(Clima):
    """
    Clase que hereda de Clima y gestiona los datos semanales.
    """

    def __init__(self):
        # Llamada al constructor de la clase padre
        super().__init__()
        self.dias = ["Lunes", "Martes", "Miércoles",
                     "Jueves", "Viernes", "Sábado", "Domingo"]

    # POLIMORFISMO: se redefine el método de ingreso de datos
    def ingresar_datos(self):
        """
        Método que solicita al usuario las temperaturas
        de todos los días de la semana.
        """
        for dia in self.dias:
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.ingresar_temperatura(dia, temp)


#### Clase principal de ejecución Aplicación Clima ####
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

# Inicio del programa
app = AplicacionClima()
app.ejecutar()
