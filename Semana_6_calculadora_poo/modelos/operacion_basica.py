from modelos.operacion import Operacion

# Clase derivada (HERENCIA)
class OperacionBasica(Operacion):

    # Método sobrescrito (POLIMORFISMO)
    def calcular(self, operador):
        if operador == "+":
            return self._numero1 + self._numero2
        elif operador == "-":
            return self._numero1 - self._numero2
        elif operador == "*":
            return self._numero1 * self._numero2
        elif operador == "/":
            if self._numero2 != 0:
                return self._numero1 / self._numero2
            else:
                return "Error: división por cero"
        else:
            return "Operador no válido"
