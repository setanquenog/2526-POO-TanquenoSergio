from modelos.operacion_basica import OperacionBasica

# Clase de servicio
# Contiene la lógica del sistema
class CalculadoraServicio:

    def ejecutar_calculo(self, num1, num2, operador):
        operacion = OperacionBasica(num1, num2)
        return operacion.calcular(operador)
