# ----------------------------------------------------
# Programa: Promedio semanal de temperaturas
# Lenguaje: Python
# Paradigma: Programación tradicional (procedimental)
# ----------------------------------------------------

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    """
    Esta función solicita al usuario las temperaturas
    de cada día de la semana y las almacena en una lista.
    Retorna la lista de temperaturas.
    """
    temperaturas = []  # Lista vacía para guardar las temperaturas

    # Lista con los días de la semana
    dias = ["Lunes", "Martes", "Miércoles", "Jueves",
            "Viernes", "Sábado", "Domingo"]

    # Recorrido de la lista de días
    for dia in dias:
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas.append(temp)  # Se agrega la temperatura a la lista

    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    """
    Esta función recibe una lista de temperaturas
    y calcula el promedio semanal.
    Retorna el promedio.
    """
    suma = sum(temperaturas)                # Suma de las temperaturas
    promedio = suma / len(temperaturas)     # Cálculo del promedio
    return promedio


# Función principal que organiza la ejecución del programa
def main():
    """
    Función principal que controla el flujo del programa.
    """
    print("=== Registro de Temperaturas Semanales ===")

    # Entrada de datos
    temperaturas_semana = ingresar_temperaturas()

    # Cálculo del promedio
    promedio_semanal = calcular_promedio(temperaturas_semana)

    # Salida de resultados
    print(f"\nEl promedio semanal de temperaturas es: {promedio_semanal:.2f} °C")


# Ejecución del programa
main()