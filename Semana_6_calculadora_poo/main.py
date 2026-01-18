from servicios.calculadora_servicio import CalculadoraServicio

# Punto de entrada del programa
def main():
    print("=== CALCULADORA BÁSICA POO ===")

    # Entrada de datos
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    operador = input("Ingrese el operador (+, -, *, /): ")

    # Crear instancia del servicio
    calculadora = CalculadoraServicio()

    # Ejecutar cálculo
    resultado = calculadora.ejecutar_calculo(numero1, numero2, operador)

    # Mostrar resultado
    print("Resultado:", resultado)


# Ejecutar programa
if __name__ == "__main__":
    main()
