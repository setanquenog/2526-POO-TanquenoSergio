# Clase base
# Aquí se aplica ENCAPSULACIÓN y HERENCIA

class Operacion:
    def __init__(self, numero1, numero2):
        # Atributos protegidos (encapsulación)
        self._numero1 = numero1
        self._numero2 = numero2

    # Método que será sobrescrito (POLIMORFISMO)
    def calcular(self):
        pass
