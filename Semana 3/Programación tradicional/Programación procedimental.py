# ----------------------------------------------------
# Programa: Promedio semanal de temperaturas
# Lenguaje: Python
# Paradigma: La Programación Tradicional o procedimental emplea funciones
# ----------------------------------------------------

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas de cada día
    y las almacena en una lista.
    """
    dias = ["Lunes", "Martes", "Miércoles",
            "Jueves", "Viernes", "Sábado", "Domingo"]

    temperaturas = []

    for dia in dias:
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)

    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    """
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


# Función principal que organiza la ejecución del programa
def ejecutar_programa():
    """
    Controla el flujo principal del programa.
    """
    print("=== Registro de Temperaturas Semanales (Programación Tradicional) ===")

    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)

    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")


# Punto de inicio del programa
ejecutar_programa()